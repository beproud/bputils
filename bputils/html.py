# vim:fileencoding=utf-8
import re

from strutils import force_unicode

__all__ = (
    'escape',
    'sanitize_html',
    'urlize',
)

# Monkey-patch HTMLParser to allow parsing of html
# attributes whose values have no quotes and are non-ascii
# i.e. <input name=submit type=submit value=検索>
import HTMLParser
HTMLParser.attrfind = re.compile(
    r'\s*([a-zA-Z_][-.:a-zA-Z_0-9]*)(\s*=\s*'
    r'(\'[^\']*\'|"[^"]*"|[^">\s]*))?')

def escape(html):
    """
    Returns the given HTML with ampersands, quotes and angle brackets encoded.
    """
    return force_unicode(html).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')

DEFAULT_VALID_TAGS = {
    'b': (),
    'blockquote': ('style',),
    'em': (),
    'strong': (),
    'strike': (),
    'a': ('href', 'title'),
    'i': (),
    'br': (),
    'ul': (),
    'ol': (),
    'li': (),
    'u': (),
    'p': (),
    'h1': (),
    'h2': (),
    'h3': (),
    'h4': (),
    'table': (),
    'thead': (),
    'tbody': (),
    'tfoot': (),
    'th': (),
    'td': ('colspan',),
    'tr': ('rowspan',),
    'hr': (),
    'img': ('src', 'alt', 'title', 'width', 'height', 'align'),
    'span': ('style',),
    'div': ('style',),
    'font': ('size', 'style', 'color'),
}

DEFAULT_VALID_STYLES = (
    "background-color",
    "color",
    "margin",
    "margin-left",
    "margin-right",
    "border",
    "padding",
    "font-weight",
    "font-style",
    "font-size",
    "text-align",
    "text-decoration",
)

RE_ANCHOR_STR = ur'(http[s]*\:\/\/.%s)(,|&gt;|&lt;|<|>|\s| |　|\xe3\x80\x80|$)'
RE_ANCHOR_NOLIMIT = re.compile(anchor_re_str % "+?")
RE_ANCHOHR_RES_STR = ur'<a href="\1"%s>\1</a>\2'

def sanitize_html(htmlSource, encoding=None, type="text/html", valid_tags=DEFAULT_VALID_TAGS, valid_styles=DEFAULT_VALID_STYLES, add_nofollow=False):
    """
    Clean bad html content. Currently this simply strips tags that
    are not in the VALID_TAGS setting.
    
    This function is used as a replacement for feedparser's _sanitizeHTML
    and fixes problems like unclosed tags and gives finer grained control
    over what attributes can appear in what tags.

    Returns the sanitized html content.

    encoding is the encoding of the htmlSource

    type is the mimetype of the content. It is ignored and is present only
    for compatibility with feedparser. 

    valid_tags is a dictionary containing keys of valid tag names which
    have a value that is a list of valid attribute names. An empty list
    indicates that no attributes are allowed. A value of None indicates
    that all attributes are allowed.

    valid_styles is a list of valid css styles that can be included in
    style tags. Style names that are not included in this list are
    stripped from the html content.

    add_nofollow can be provided which can either be a boolean value
    or a regex that can be matched against a url. If the regex matches
    then nofollow is added to the url.
    """
    from BeautifulSoup import BeautifulSoup, Comment

    js_regex = re.compile(r'[\s]*(&#x.{1,7})?'.join(list('javascript')))
    css_regex = re.compile(r' *(%s): *([^;]*);?' % '|'.join(valid_styles), re.IGNORECASE)
    # Sanitize html with BeautifulSoup
    if encoding:
        soup = BeautifulSoup(htmlSource, fromEncoding=encoding)
    else:
        soup = BeautifulSoup(htmlSource)

    def entities(text):
        return text.replace('<','&lt;')\
                   .replace('>', '&gt;')\
                   .replace('"', '&quot;')\
                   .replace("'", '&apos;')
    
    # Sanitize html text by changing bad text to entities.
    # BeautifulSoup will do this for href and src attributes
    # on anchors and image tags but not for text.
    for text in soup.findAll(text=True):
        text.replaceWith(entities(text))

    # コメントを削る
    for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
        comment.extract()

    for tag in soup.findAll(True):
        if tag.name not in VALID_TAGS:
            tag.hidden = True
        else:
            tag.attrs = [(attr, js_regex.sub('', val))
                            for attr, val in tag.attrs 
                            if attr in VALID_TAGS[tag.name]]

    # Add rel="nofollow" links
    if add_nofollow:
        findall_kwargs = {}
        if not instanceof(add_nofollow, bool):
            findall_kwargs["attrs"] = {"href": add_nofollow}
        for tag in soup.findAll("a", **findall_kwargs):
            tag["rel"] = "nofollow" 

    # Clean up CSS style tags
    for tag in soup.findAll(attrs={"style":re.compile(".*")}):
        style = ""
        for key,val in css_regex.findall(tag["style"]):
            style += "%s:%s;" % (key,val.strip())
        tag["style"] = style

    return soup.renderContents().decode('utf8') 

def urlize(text, trim_url_limit=None, nofollow=False, autoescape=False):
    """text内URLを抽出してアンカータグで囲む
    
    URLのデリミタは半角カンマ、<>(エスケープ済み含む)、\s、全角スペース、行末で、これらが末尾にマッチしない場合はURLとして認識しません。
    URL部分は.+の最小マッチ、もしくはtrim_url_limitが指定された場合は{,trim_url_limit}の最小マッチとなります。

    -args

        text:           urlize対象文字列
        trim_url_limit: urlとして認識する文字数に上限を設ける場合は数値をセット
        nofollow:       Trueを与えるとタグにrel="nofollow"を付加
        autoescape:     Trueを与えるとタグエスケープを行います。
    
    """
    if autoescape:
        text = escape(text)

    if trim_url_limit:
        anchor_re = re.compile(RE_ANCHOR_STR % "{,%s}?" % trim_url_limit)
    else:
        anchor_re = RE_ANCHOR_NOLIMIT

    if nofollow:
        anchor_re_result = RE_ANCHOHR_RES_STR % ' rel="nofollow"'
    else:
        anchor_re_result = RE_ANCHOHR_RES_STR % ""

    return anchor_re.sub(anchor_re_result, text)

# vim:fileencoding=utf-8
import datetime

from bputils import simplejson

__all__ = (
    'SafeJSONEncoder',
    'escapejs_json',
    'force_js',
)

ESCAPEJS_JSON_STRING = (
    (u'<', u'\\u003c'),
    (u'>', u'\\u003e'),
    (u'&', u'\\u0026'),
)

JS_CONVERT_TYPES = {
    'bool': bool,
    'int': int,
    'string': str,
    'array': list,
}

class SafeJSONEncoder(simplejson.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time and decimal types
    and performs some extra javascript escaping.
    """

    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("%s %s" % (self.DATE_FORMAT, self.TIME_FORMAT))
        elif isinstance(o, datetime.date):
            return o.strftime(self.DATE_FORMAT)
        elif isinstance(o, datetime.time):
            return o.strftime(self.TIME_FORMAT)
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return escape_js(super(SafeJSONEncoder, self).default(o))

def escapejs_json(s):
    """
    JSONEncoderエスケープされない文字を追加エスケープ
    """
    for c, code in ESCAPEJS_JSON_STRING:
        s = s.replace(c, code)
    return s

def force_js(value, typename=None, encoder=None):
    """
    Changes a python value to javascript for use in templates
    """
    if typename:
        typename = typename.lower()
        if typename in JS_CONVERT_TYPES:
            value = JS_CONVERT_TYPES[typename](value)
    return simplejson.dumps(value, cls=(encoder or SafeJSONEncoder))

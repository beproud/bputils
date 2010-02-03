:mod:`html` -- HTMLユティリティ
================================================================

.. module:: bputils.html
   :synopsis: HTMLユティリティ
.. moduleauthor:: Ian Lewis <ian@beproud.jp>

.. function:: escape(html)

.. function:: sanitize_html(htmlSource[, encoding[, type[, valid_tags[, valid_styles[, add_nofollow]]]]])

.. function:: urlize(text[, trim_url_limit[, nofollow[, autoescape]]])

    text内URLを抽出してアンカータグで囲む
    
    URLのデリミタは半角カンマ、<>(エスケープ済み含む)、\s、全角スペース、行末で、これらが末尾にマッチしない場合はURLとして認識しません。
    URL部分は.+の最小マッチ、もしくはtrim_url_limitが指定された場合は{,trim_url_limit}の最小マッチとなります。

    -args

        text:           urlize対象文字列
        trim_url_limit: urlとして認識する文字数に上限を設ける場合は数値をセット
        nofollow:       Trueを与えるとタグにrel="nofollow"を付加
        autoescape:     Trueを与えるとタグエスケープを行います。


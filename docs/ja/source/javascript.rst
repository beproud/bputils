:mod:`javascript` -- JavascriptとJSONユティリティ
================================================================

.. module:: beproud.utils.javascript
   :synopsis: JavascriptとJSONユティリティ
.. moduleauthor:: Ian Lewis <ian@beproud.jp>
.. moduleauthor:: Shinya Okano <tokibito@beproud.jp>

.. class:: beproud.utils.javascript.SafeJSONEncoder

    ウェブブラウザで安全に扱えるようにJSONをエスケープするエンコーダーです。
    datetime.datetime、datetime.time、Decimalインスタンスも便利にエンコードします。

    >>> from beproud.utils import simplejson
    >>> from beproud.utils.javascript import SafeJSONEncoder
    >>> from datetime import datetime
    >>> data = {
    ...     "title": "<title>",
    ...     "datetime": datetime(2009, 2, 19, 10, 22),
    ... }
    >>> simplejson.dumps(data, cls=SafeJSONEncoder)
    '{"datetime": "2009-02-19 10:22:00", "title": "\\u003ctitle\\u003e"}'

.. function:: escapejs_json(s)

    simplejsonがエスケープしない文字をエスケープする関数です。
    つまり、'<', '>', '&' を '\\u003c', '\\u003e', '\\u0026' に変換する。 

    '<','>','&'をJSONにそのままブラウザに送信すると、<script>タグが入っていて
    そのままjavascriptを実行される可能性があります。 （特に IE)

    >>> from beproud.utils.javascript import escapejs_json
    >>> escapejs_json("<test> & test")
    '"\\u003ctest\\u003e \\u0026 test"'

.. function:: force_js(value[, typename[, encoder]])

    pythonの値をjsの値に変換する。typenameを渡すと、そのタイプに変換します。
    'bool', 'int', 'string', 'array'をサポートしています。

    >>> from beproud.utils.javascript import force_js
    >>> force_js("test")
    u'"test"'    
    >>> force_js("", "bool")
    False
    >>> force_js(["list", "test"])
    u'["list", "test"]'

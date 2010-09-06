:mod:`strutils` -- 文字列ユティリティ
================================================================

.. module:: beproud.utils.strutils
   :synopsis: 文字列ユティリティ
.. moduleauthor:: Ian Lewis <ian@beproud.jp>
.. moduleauthor:: Shinya Okano <tokibito@beproud.jp>

.. class:: beproud.utils.strutils.StrAndUnicode

.. function:: force_unicode(s[, encoding[, strings_only[, errors]]])

.. function:: smart_str(s[, encoding[, strings_only[, errors]]])

.. function:: trim(s[, encoding])

    全角・半角も含めてトリミング

.. function:: force_int(num[, default])

    force_intは文字列データなどを整数型に変換する関数です。変換を失敗した場合、default値を返します。

.. function:: make_random_key([size[, values]])

    ランダムキーを生成する関数です。
    
    * sizeはキーの長さになります。デフォールトは124桁
    * valuesは選択肢キャラクタを持った文字列。デフォールトは string.letters + string.digits

.. function:: abbrev(s[, num[, end]])
    
    文字列を政略する関数です。

    * num で最長長さを指定します。デフォールトは255桁
    * end は最後にくっ付く文字列を指定します。デフォールトは'...'。最長長さはendの長さを含む。返す文字列はnumより長い場合はありません。


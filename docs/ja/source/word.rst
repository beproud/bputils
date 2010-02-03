:mod:`word` -- 自然言語ユティリティ
================================================================

.. module:: bputils.strutils
   :synopsis:  自然言語ユティリティ
.. moduleauthor:: Ian Lewis <ian@beproud.jp>
.. moduleauthor:: Shinya Okano <tokibito@beproud.jp>

.. class:: bputils.word.Tokenizer

.. function:: extract_keywords(s[, compfunc[, dic_encoding]])

.. function:: optimize(s)

    全角記号英数字を半角に、半角かなを全角に

.. function:: hankaku(s)

.. function:: normalize(s)

    全角記号英数字を半角に、半角かなを全角に
    全角数字を半角数字に
    全角の[ー－―‐]を - に

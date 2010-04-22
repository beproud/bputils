:mod:`word` -- 自然言語ユティリティ
================================================================

.. module:: bputils.word
   :synopsis:  自然言語ユティリティ
.. moduleauthor:: Ian Lewis <ian@beproud.jp>
.. moduleauthor:: Shinya Okano <tokibito@beproud.jp>

.. class:: bputils.word.Tokenizer

    `MeCab`_ を使って、文章を解析して、トーケンと特徴を出してくれるクラス。

    使い方は割と簡単::

        >>> from bputils.word import Tokenizer
        >>> t = Tokenizer()
        >>> for token in t.tokenize(u"これはテスト文章です。MeCabはよく出来てきます。"):
        ...     print token
        ...     print "{"
        ...     for key in token.features:
        ...         print '   "%s": "%s"' % (key, token.features[key])
        ...     print "}"
        ... 
        これ
        {
           "base": "これ"
           "word_class": "名詞"
           "conjugation": "None"
           "pronunciation": "コレ"
           "conjugated": "None"
           "sub_word_class3": "None"
           "sub_word_class2": "一般"
           "sub_word_class1": "代名詞"
           "reading": "コレ"
        }
        は
        {
           "base": "は"
           "word_class": "助詞"
           "conjugation": "None"
           "pronunciation": "ワ"
           "conjugated": "None"
           "sub_word_class3": "None"
           "sub_word_class2": "None"
           "sub_word_class1": "係助詞"
           "reading": "ハ"
        }
        ...

    Tokenizerクラスインスタンスを生成するときに、いろなオプションに対応しています。

    * encoding: 扱う文書の文字コード
    * min_word_length: 単語の最短長さ。min_word_lengthより短い単語を無視します。
    * ignore_word_re: 無視する単語の正規表現。これにマッチすれば無視します。
    * token_callback:
    * word_classes: このリストに入っている品詞に限る 

.. function:: extract_keywords(s[, compfunc[, dic_encoding]])

.. function:: optimize(s)

    全角記号英数字を半角に、半角かなを全角に

.. function:: hankaku(s)

.. function:: normalize(s)

    全角記号英数字を半角に、半角かなを全角に
    全角数字を半角数字に
    全角の[ー－―‐]を - に

.. _`Mecab`: http://mecab.sourceforge.net/

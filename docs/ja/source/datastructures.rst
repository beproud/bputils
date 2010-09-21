:mod:`datastructures` -- データユティリティクラス
================================================================

.. module:: beproud.utils.datastructures
   :synopsis:  データユティリティクラス
.. moduleauthor:: Ian Lewis <ian@beproud.jp>


.. class:: beproud.utils.datastructures.Bag

    Bagは辞書として扱えるクラスです。::

        >>> from beproud.utils.datastructures import Bag
        
        >>> bag = Bag(attr1="test", attr2="hoge")
        >>> bag["attr3"] = "hogehoge"
        >>> bag.attr4 = "testhoge"
        >>> bag.attr1
        "test"
        >>> bag.attr2
        "hoge"
        >>> bag["attr3"]
        "hogehoge"
        >>> bag["attr4"]
        "testhoge"

.. class:: beproud.utils.datastructures.DotDict

    DotDictはオブジェクトとして、扱える辞書オブジェクトです。::

        >>> from beproud.utils.datastructures import DotDict

        >>> mydict = DotDict(attr1="test", attr2="hoge")
        >>> mydict["attr3"] = "hogehoge"
        >>> mydict.attr4 = "testhoge"
        >>> mydict.attr1
        "test"
        >>> mydict.attr2
        "hoge"
        >>> mydict["attr3"]
        "hogehoge"
        >>> mydict["attr4"]
        "testhoge"

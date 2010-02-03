:mod:`datastructures` -- データユティリティクラス
================================================================

.. module:: bputils.datastructures
   :synopsis:  データユティリティクラス
.. moduleauthor:: Ian Lewis <ian@beproud.jp>


.. class:: bputils.datastructures.Bag

    Bagは辞書として扱えるクラスです。::

        >>> from bputils.datastructures import Bag
        
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

.. class:: bputils.datastructures.DotDict

    DotDictはオブジェクトとして、扱える辞書オブジェクトです。::

        >>> from bputils.datastructures import DotDict

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

====================
decimalutils
====================

decimalutilsは Python の decimal モジュールの拡張ユティリティモジュールです。

--------------------
force_decimal
--------------------

Decimal オブジェクトを変換する。対応タイプは int, long, float, basestring, unicode です。

.. code-block:: python

    >>> from bputils.decimalutils import force_decimal 
    >>> force_decimal(1)
    Decimal('1')
    >>> force_decimal(1.128492)
    Decimal('1.128492')
    >>> force_decimal("-0.492")
    Decimal('-0.492') 

Python の float タイプは C の double タイプで実装されているので、バイナリ浮動小数点数の精度の損失が発生します。バイナリ浮動小数点数は小数で概算した値として保存されていますので、ハードウエアに依存します。有効数字に気をつけないといけないところが面倒です。

.. code-block:: python

    >>> 1.1
    1.1000000000000001
    >>> 1.1 / 2
    0.55000000000000004

float は少数で概算した値なので、Decimalオブジェクトにコンバートする時に、注意しないといけないところがあります。str(float) は 12有効数字まで、変換しますので、精度を損失しないようにしないといけない際は、precision_loss の引数を False にします。

.. code-block:: python
    
    >>> from bputils.decimalutils import force_decimal
    >>> import math
    >>> math.pi
    3.1415926535897931
    >>> str(math.pi)
    '3.14159265359'
    >>> force_decimal(math.pi) 
    Decimal('3.14159265359')
    >>> force_decimal(math.pi, precision_loss=False)
    Decimal('3.141592653589793115997963469')

precision_loss は浮動小数点数の概算の精度を守るために、変換に工夫しますが、いらない有効数字が入る可能性があります。

.. code-block:: python
    
    >>> from bputils.decimalutils import force_decimal
    >>> force_decimal(1.1, precision_loss=False)
    Decimal('1.100000000000000088817841970')

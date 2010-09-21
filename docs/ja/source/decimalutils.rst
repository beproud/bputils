:mod:`decimalutils` -- decimal モジュールユティリティ
================================================================

.. module:: beproud.utils.decimalutils 
   :synopsis: decimal モジュールユティリティ
.. moduleauthor:: Ian Lewis <ian@beproud.jp>

decimalutils は Python の decimal モジュールの拡張ユティリティモジュールです。

.. function:: force_decimal(d[, precision_loss[, numbers_only]])

    Decimal オブジェクトを変換する。対応タイプは int, long, float, basestring, unicode です。::
    
        >>> from beproud.utils.decimalutils import force_decimal 
        >>> force_decimal(1)
        Decimal('1')
        >>> force_decimal(1.128492)
        Decimal('1.128492')
        >>> force_decimal("-0.492")
        Decimal('-0.492') 

    Python の float タイプは C の double タイプで実装されているので、バイナリ浮動小数点数の精度の損失が発生します。
    バイナリ浮動小数点数は小数で概算した値として保存されていますので、ハードウエアに依存します。有効数字に気をつけないといけないところが面倒です。::

        >>> 1.1
        1.1000000000000001
        >>> 1.1 / 2
        0.55000000000000004

    float は少数で概算した値なので、Decimalオブジェクトにコンバートする時に、注意しないといけないところがあります。
    str(float) は 12有効数字まで、変換しますので、精度を損失しないようにしないといけない際は、precision_loss の引数を False にします。::

    
        >>> from beproud.utils.decimalutils import force_decimal
        >>> import math
        >>> math.pi
        3.1415926535897931
        >>> str(math.pi)
        '3.14159265359'
        >>> force_decimal(math.pi) 
        Decimal('3.14159265359')
        >>> force_decimal(math.pi, precision_loss=False)
        Decimal('3.141592653589793115997963469')

    precision_loss は浮動小数点数の概算の精度を守るために、変換に工夫しますが、いらない有効数字が入る可能性があります。::

        >>> from beproud.utils.decimalutils import force_decimal
        >>> force_decimal(1.1, precision_loss=False)
        Decimal('1.100000000000000088817841970')

.. function:: pi()

    現在の精度で :math:`\pi` を計算して、Decimalオブジェクトとして、返します。:
    
        >>> print pi()
        3.141592653589793238462643383
        >>> pi()
        Decimal('3.141592653589793238462643383')

.. function:: exp(x)

    現在の精度で :math:`e^{x}` を計算します。::

        >>> print exp(Decimal(1))
        2.718281828459045235360287471
        >>> print exp(Decimal(2))
        7.389056098930650227230427461
        >>> print exp(2.0)
        7.38905609893
        >>> print exp(2+0j)
        (7.38905609893+0j)

.. function:: cos(x)

    現在の精度で、x の余弦を計算します。::

        >>> print cos(Decimal('0.5'))
        0.8775825618903727161162815826
        >>> print cos(0.5)
        0.87758256189
        >>> print cos(0.5+0j)
        (0.87758256189+0j)

.. function:: sin(x)

    現在の精度で、x の正弦を計算します。::

        >>> print sin(Decimal('0.5'))
        0.4794255386042030002732879352
        >>> print sin(0.5)
        0.479425538604
        >>> print sin(0.5+0j)
        (0.479425538604+0j)

.. function:: log(self[, base[, context]])

    現在の精度で、selfの対数を計算します。::

        >>> print log(Decimal("1.204"))
        0.0806264869218057475447822012
        >>> print log(Decimal("1.204"), 2)
        0.2678353920976150027151526692

        >>> import math
        >>> abs(math.log(1.204, 10) - float(log(Decimal("1.204")))) < 1e-15
        True
        >>> abs(math.log(1.827528759292, 10) - float(log(Decimal("1.827528759292")))) < 1e-15
        True

.. function:: ln(self[, context])

    現在の精度で、selfの自然対数を計算します。::

        >>> print ln(Decimal("1.204"))
        0.1856493468866292953586851357

        >>> import math
        >>> abs(math.log(1.204) - float(ln(Decimal("1.204")))) < 1e-15
        True
        >>> abs(math.log(1.827528759292) - float(ln(Decimal("1.827528759292")))) < 1e-15
        True

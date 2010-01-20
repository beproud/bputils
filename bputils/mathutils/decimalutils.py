#:coding=utf8:

from decimal import Decimal, getcontext, setcontext, InvalidOperation

#def force_decimal(obj,  
__all__ = (
    'force_decimal',
    'log',
    'ln',
)

def force_decimal(d, default=None, numbers_only=False):
    """
    Coerces a value to a Decimal object. 

    float objects are first converted to strings before being
    converted to Decimal objecs. This can cause a loss of
    precision as the float objects are rounded. The 'str'
    method is used since it provides better precision than "%f" % float

    If numbers_only is True, don't convert (some) non-number-like objects.
    Strings that can be converted to Decimals are still converted.
    """
    try:
        if isinstance(d, Decimal):
            return d
        elif isinstance(d, (int, long)):
            return Decimal(d)
        elif isinstance(d, float):
            return Decimal(str(d))
        elif isinstance(d, (basestring, unicode)):
            return Decimal(d)
    except InvalidOperation:
        pass

    if numbers_only:
        return d
    else:
        raise ValueError("Cannot convert object to Decimal: %r" % d)  

def log(self, base=10, context=None):
    """
    Returns a log of arbitrary precision using the method
    described here: http://www.programmish.com/?p=25
    """
    old_context = None
    if context is not None:
        old_context = getcontext()
        setcontext(context)

    cur_prec = getcontext().prec
    getcontext().prec += 2
    try:
        retValue = self
        baseDec = force_decimal(base)

        integer_part = Decimal(0)
        while retValue < 1:
            integer_part = integer_part - 1
            retValue = retValue * baseDec
        while retValue >= baseDec:
            integer_part = integer_part + 1
            retValue = retValue / baseDec

        retValue = retValue ** 10
        decimal_frac = Decimal(0)
        partial_part = Decimal(1)
        while cur_prec > 0:
            partial_part = partial_part / Decimal(10)
            digit = Decimal(0)
            while retValue >= baseDec:
                digit += 1
                retValue = retValue / baseDec
            decimal_frac = decimal_frac + digit * partial_part
            retValue = retValue ** 10
            cur_prec -= 1
    finally:
        # restore contexts
        getcontext().prec -= 2
        if old_context is not None:
            setcontext(old_context)

    return integer_part + decimal_frac

def ln(self, context=None):
    if hasattr(self, "ln"):
        return self.ln(context)
    else:
        import math
        return log(self, base=force_decimal(math.e)) 

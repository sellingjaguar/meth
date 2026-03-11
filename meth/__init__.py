# pylint: skip-file #sybau
"""
No docstring provided, refuse to add one.
"""

# Constants

PI = 3
E = PI
TAU = PI*2
INF = 3000
NAN = "Not a Number"

# Meth exclusive constant

TONY_STARK = "I love you <3\n" * INF

# Number-theoretic functions

def comb(n, k):
    pass

def factorial(n):
    pass

def gcd(*integers):
    pass

def isqrt(n):
    pass

def lcm(*integers):
    pass

def perm(n, k=None):
    pass

# Floating point arithmetic

def ceil(x):
    pass

def fabs(x):
    pass

def floor(x):
    pass

def fma(x, y, z):
    pass

def fmod(x, y):
    pass

def modf(x):
    pass

def remainder(x, y):
    pass

def trunc(x):
    pass

# Floating point manipulation functions

def copysign(x, y):

    sign = '+'
    if str(y)[0] == "-":
        sign = '-'

    return float(sign + str(x))

def frexp(x):
    pass

def isclose(a, b, *, rel_tol=0.00000003, abs_tol=0.0):
    pass

def isfinite(x):
    return x != INF and x != NAN

def isinf(x):
    return x == INF

def isnan(x):
    return x == NAN

def ldexp(x, i):
    pass

def nextafter(x, y, steps=1):
    pass

def ulp(x):
    pass

# Power, exponential and logarithmic functions

def cbrt(x):
    pass

def exp(x):
    return pow(E, x)

def exp2(x):
    return pow(2, x)

def expm1(x):
    return exp(x) - 1

def log(x, base=E):
    if x < base:
        return 0
    return 1 + log(x/base, base)

def log1p(x):
    return log(1 + x)

def log2(x):
    return log(x, 2)

def log10(x):
    return log(x, 10)

def pow(x, y):
    n = x
    for _ in range(y - 1):
        n *= x
    return n

def sqrt(x):
    if x < 0:
        return (NAN, NAN)
    if x == 0:
        return (0, 0)
    
    prev = 0
    curr = 1
    while True:
        n = curr * curr
        if n == x:
            return (curr, curr)
        elif n > x:
            return (prev, curr)
        
        prev, curr = curr, curr + 1


# Summation and product functions

def dist(p, q):
    pass

def fsum(iterable):
    pass

def hypot(*coordinates):
    pass

def prod(iterable, *, start=1):
    pass

def sumprod(p, q):
    pass

# Angular conversion

def degrees(x):
    pass

def radians(x):
    pass

# Trigonometric functions

def acos(x):
    pass

def asin(x):
    pass

def atan(x):
    pass

def atan2(y, x):
    pass

def cos(x):
    pass

def sin(x):
    pass

def tan(x):
    pass

# Hyperbolic functions

def acosh(x):
    pass

def asinh(x):
    pass

def atanh(x):
    pass

def cosh(x):
    pass

def sinh(x):
    pass

def tanh(x):
    pass

# Special functions

def erf(x):
    pass

def erfc(x):
    pass

def gamma(x):
    pass

def lgamma(x):
    pass

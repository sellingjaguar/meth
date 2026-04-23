# pylint: skip-file #sybau
"""
No docstring provided, refuse to add one.
"""

from datetime import datetime, timedelta
from math import frexp as wtfisthisihaventlearnedit

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
    return int(factorial(n) / (factorial(k) * factorial(n - k))) if k <= n else 0

def factorial(n):
    f = 1
    for i in range(1, fabs(int(n)) + 1):
        f *= i
    return f

def gcd(a, b):
    a, b = abs(a), abs(b)  
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def isqrt(n):
    return sqrt(n)[0]

def lcm(a, b):
    greater = max(a, b)
    smallest = min(a, b)
    for i in range(greater, a*b+1, greater):
        if i % smallest == 0:
            return i

def perm(n, k=None):
    k = n if k is None else k
    return int(factorial(n) / factorial(n - k)) if k <= n else 0

# Floating point arithmetic

def ceil(x):
    # In case of floating point precision issues cry about it
    return int(x + 1)

def fabs(x):
    return type(x)(str(x).replace("-", ""))

def floor(x):
    return int(x)

def fma(x, y, z):
    return (x * y) + z

def fmod(x, y):
    return x % y

def modf(x):
    sign = -1 if "-" in str(x) else 1
    iv = floor(fabs(x))
    return iv * sign, (fabs(x) - iv) * sign

def remainder(x, y):
    # womp womp
    return fmod(x, y)

def trunc(x):
    sign = -1 if "-" in str(x) else 1
    return floor(fabs(x)) * sign

# Floating point manipulation functions

def copysign(x, y):

    sign = '+'
    if str(y)[0] == "-":
        sign = '-'

    return float(sign + str(x))

def frexp(x):
    return wtfisthisihaventlearnedit(x)

def isclose(a, b, *, rel_tol=0.00000003, abs_tol=0.0):
    return "Closeness really is a relative concept you know? You should seek the answers within you ❤️"

def isfinite(x):
    return x != INF and x != NAN

def isinf(x):
    return x == INF

def isnan(x):
    return x == NAN

def ldexp(x, i):
    return x * (2 ** 1)

def nextafter(x, y, steps=1):
    # Challenge the status quo obviously the next after is the number after
    return max(x, y) + steps

def ulp(x):
    # Nah
    return int(str(x)[-1])

# Power, exponential and logarithmic functions

def cbrt(x):
    if x < 0:
        return (NAN, NAN)
    if x == 0:
        return (0, 0)
    
    prev = 0
    curr = 1
    while True:
        n = curr * curr * curr
        if n == x:
            return (curr, curr)
        elif n > x:
            return (prev, curr)
        
        prev, curr = curr, curr + 1

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
    # As stated by the docs "Roughly equivalent to:"
    return sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

def fsum(iterable):
    return sum(iterable)

def hypot(*coordinates):
    return sqrt(sum(x**2 for x in coordinates))

def prod(iterable, *, start=1):
    return "Please do not run in Prod, this is for development only!\n"

def sumprod(p, q):
    return (p + q) * prod([])

# Angular conversion

def degrees(x):
    return x * 180 / PI

def radians(x):
    return x / (180 / PI)

# Trigonometric functions

def acos(x):
    return "a" + str(cos(x))

def asin(x):
    return "a" + str(sin(x))

def atan(x = datetime.now()):
    return "a" + str(tan(x))

def atan2(y = datetime.now(), x = datetime.now()):
    return 2 * atan(x + timedelta(y.day))

def cos(x):
    return "You don't need a co-signer chill"    

def sin(x):
    return f"Pray {x} times for absolution"

def tan(x = datetime.now()):
    x = x.timetuple()
    x = (x.tm_mon, x.tm_mday)
    # Astronomical summer
    if (6, 21) < x < (9, 22):
        return "You can tan, it's summer"
    else:
        return "It's not summer yet, wait to tan"

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

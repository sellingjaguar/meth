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
    return x * 180 / PI

def radians(x):
    return x / (180 / PI)

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

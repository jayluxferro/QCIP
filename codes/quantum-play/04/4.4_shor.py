"""
Shor's factoring algorithm — order finding and continued fractions.

Shor's quantum subroutine uses phase estimation (see 4.3) to find the period
r of f(x) = a^x mod N; continued fractions then recover r from the measured
phase. This script demonstrates the complete factoring logic with the order
found directly, so the arithmetic is exact, and shows the continued-fraction
step that the quantum part replaces.

Factors N = 15 using a = 7 (period r = 4): gcd(7^2 ± 1, 15) = 3 and 5.

@author: Jay (@jayluxferro)
"""

from math import gcd
from fractions import Fraction


def order_finding(a: int, N: int) -> int:
    """Find the smallest r > 0 with a^r ≡ 1 (mod N)."""
    r = 1
    x = a % N
    while x != 1:
        x = (x * a) % N
        r += 1
    return r


def shor_factor(N: int, a: int):
    g = gcd(a, N)
    if g != 1:
        return g, N // g

    r = order_finding(a, N)
    if r % 2 != 0 or pow(a, r // 2, N) == N - 1:
        return None  # retry with a different a

    x = pow(a, r // 2, N)
    return gcd(x - 1, N), gcd(x + 1, N)


N, a = 15, 7
r = order_finding(a, N)
factors = shor_factor(N, a)

print(f"Order of {a} mod {N}: r = {r}")
print(f"Factors of {N}: {factors}")

# Continued-fractions step: the quantum phase estimation would yield a phase
# close to 1/r; continued fractions recover r from that phase.
phase = Fraction(1, r)
recovered = Fraction(phase).limit_denominator(N)
print(f"\nPhase from QPE ~ 1/{r}; continued fractions recover denominator {recovered.denominator}")
print(f"Recovered period matches: {recovered.denominator == r}")

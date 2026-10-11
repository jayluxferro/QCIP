"""
Computational complexity and asymptotic (big-O) notation.

Counts operations as a function of input size n, showing why exponential
algorithms become intractable while logarithmic and polynomial ones scale.

@author: Jay (@jayluxferro)
"""

from math import log2

classes = [
    ("O(1)", lambda n: 1),
    ("O(log n)", lambda n: log2(n)),
    ("O(n)", lambda n: n),
    ("O(n log n)", lambda n: n * log2(n)),
    ("O(n^2)", lambda n: n**2),
    ("O(2^n)", lambda n: 2**n),
]

print("Operations vs input size n:")
header = "  ".join(f"{name:>10}" for name, _ in classes)
print(f"{'n':>4}  {header}")
for n in [1, 2, 4, 8, 16, 32, 64]:
    row = "  ".join(f"{fn(n):>10.1f}" for _, fn in classes)
    print(f"{n:>4}  {row}")

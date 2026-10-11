"""
Boolean algebra identities.

Verifies the fundamental identities of Boolean algebra exhaustively over all
input combinations — the rules used to simplify logic circuits.

@author: Jay (@jayluxferro)
"""

# Each identity is a predicate over (A, B), checked for all 4 input pairs.
identities = {
    "A AND 0 = 0": lambda a, b: (a & 0) == 0,
    "A AND 1 = A": lambda a, b: (a & 1) == a,
    "A OR 0 = A": lambda a, b: (a | 0) == a,
    "A OR 1 = 1": lambda a, b: (a | 1) == 1,
    "A AND A = A (idempotent)": lambda a, b: (a & a) == a,
    "A OR A = A (idempotent)": lambda a, b: (a | a) == a,
    "A AND (NOT A) = 0 (complement)": lambda a, b: (a & (1 - a)) == 0,
    "A OR (NOT A) = 1 (complement)": lambda a, b: (a | (1 - a)) == 1,
    "NOT(NOT A) = A (involution)": lambda a, b: (1 - (1 - a)) == a,
    "De Morgan: NOT(A AND B) = NOT A OR NOT B": lambda a, b: (1 - (a & b)) == ((1 - a) | (1 - b)),
    "De Morgan: NOT(A OR B) = NOT A AND NOT B": lambda a, b: (1 - (a | b)) == ((1 - a) & (1 - b)),
    "Distributive: A AND (B OR A) = A (absorption)": lambda a, b: (a & (b | a)) == a,
}

for name, check in identities.items():
    holds = all(check(a, b) for a in [0, 1] for b in [0, 1])
    print(f"{'✓' if holds else '✗'}  {name}")

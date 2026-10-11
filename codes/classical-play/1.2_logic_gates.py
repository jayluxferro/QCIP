"""
Classical logic gates and their truth tables.

Single-bit gate (NOT) and two-bit gates (AND, OR, XOR, NAND). NAND is
universal: every other gate can be built from it.

@author: Jay (@jayluxferro)
"""


def gate(name: str, a: int, b: int = 0) -> int:
    if name == "NOT":
        return 1 - a
    if name == "AND":
        return a & b
    if name == "OR":
        return a | b
    if name == "XOR":
        return a ^ b
    if name == "NAND":
        return 1 - (a & b)
    raise ValueError(f"unknown gate: {name}")


# Single-bit gate.
print("NOT:")
for a in [0, 1]:
    print(f"  NOT {a} = {gate('NOT', a)}")

# Two-bit gates.
for name in ["AND", "OR", "XOR", "NAND"]:
    print(f"\n{name}:")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"  {a} {name} {b} = {gate(name, a, b)}")

"""
Classical adders: half adder and full adder.

A half adder adds two bits; a full adder also accepts a carry-in. Chaining
full adders implements multi-bit (ripple-carry) addition.

@author: Jay (@jayluxferro)
"""


def half_adder(a: int, b: int) -> tuple:
    """Add two bits -> (sum, carry)."""
    return (a ^ b, a & b)


def full_adder(a: int, b: int, carry_in: int) -> tuple:
    """Add two bits plus a carry -> (sum, carry_out)."""
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, carry_in)
    return (s2, c1 | c2)


def add_binary(a: str, b: str) -> str:
    """Add two binary strings using ripple-carry full adders."""
    a = a.zfill(len(b))
    b = b.zfill(len(a))
    result = []
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        s, carry = full_adder(int(a[i]), int(b[i]), carry)
        result.append(str(s))
    if carry:
        result.append(str(carry))
    return "".join(reversed(result))


print("Half adder:")
for a in [0, 1]:
    for b in [0, 1]:
        s, c = half_adder(a, b)
        print(f"  {a}+{b} = sum {s}, carry {c}")

print("\nFull adder:")
for a in [0, 1]:
    for b in [0, 1]:
        for cin in [0, 1]:
            s, cout = full_adder(a, b, cin)
            print(f"  {a}+{b}+{cin} = sum {s}, carry {cout}")

print(f"\n0011 + 0101 = {add_binary('0011', '0101')}  (3 + 5 = 8)")

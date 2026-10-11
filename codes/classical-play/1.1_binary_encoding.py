"""
Classical information encoding: binary, hexadecimal, and ASCII.

Numbers, and ultimately all digital data, are encoded as strings of bits.
Here we convert between decimal, binary, hexadecimal, and ASCII text.

@author: Jay (@jayluxferro)
"""


def to_binary(n: int, width: int = 8) -> str:
    return format(n, f"0{width}b")


def to_hex(n: int) -> str:
    return format(n, "X")


# Decimal -> binary / hex for a few numbers.
for n in [0, 1, 7, 10, 15, 42, 255]:
    print(f"{n:3d} = 0b{to_binary(n)} = 0x{to_hex(n)}")

# Text -> ASCII codes -> binary.
text = "Q"
codes = [ord(c) for c in text]
print(f"\n'{text}' -> ASCII codes {codes} -> binary {[to_binary(c) for c in codes]}")

# Binary -> decimal.
print(f"0b01000001 -> {int('01000001', 2)}  (ASCII 'A')")

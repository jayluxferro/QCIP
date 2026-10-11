"""
Classical error detection (parity) and correction (repetition).

A parity bit detects a single bit flip; a repetition code (send each bit
three times, decode by majority vote) corrects it.

@author: Jay (@jayluxferro)
"""


def even_parity(bits: list) -> list:
    """Append a parity bit so the total number of 1s is even."""
    return bits + [sum(bits) % 2]


def check_parity(bits_with_parity: list) -> bool:
    """True if the parity check passes (even number of 1s)."""
    return sum(bits_with_parity) % 2 == 0


def encode_repetition(bit: int) -> list:
    return [bit, bit, bit]


def decode_repetition(triple: list) -> int:
    """Majority vote."""
    return 1 if sum(triple) >= 2 else 0


# Parity detects a single error.
data = [1, 0, 1, 1]
encoded = even_parity(data)
print(f"Data {data} -> with parity {encoded}")
print(f"Parity check (no error): {check_parity(encoded)}")

flipped = encoded.copy()
flipped[1] ^= 1
print(f"Flipped {flipped} -> parity check: {check_parity(flipped)} (error detected)")

# Repetition code corrects a single error.
print("\nRepetition code (3x) with majority-vote correction:")
for bit in [0, 1]:
    corrupted = encode_repetition(bit)
    corrupted[0] ^= 1  # introduce a single error
    print(f"  send {bit} -> corrupted {corrupted} -> decode {decode_repetition(corrupted)}")

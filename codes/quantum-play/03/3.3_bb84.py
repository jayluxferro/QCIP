"""
BB84 quantum key distribution (simulated).

Alice sends random bits encoded in random bases (Z or X). Bob measures in
random bases. After sifting to matching bases, the keys should agree. An
eavesdropper measuring in random bases introduces a ~25% quantum bit error
rate (QBER), revealing the interception.

@author: Jay (@jayluxferro)
"""

import numpy as np

np.random.seed(0)  # reproducible teaching run

n = 200  # number of qubits Alice sends

# Alice's random bits and encoding bases (0 = Z basis, 1 = X basis).
alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.randint(2, size=n)

# Bob's random measurement bases.
bob_bases = np.random.randint(2, size=n)

# Without an eavesdropper, Bob's outcome matches Alice's bit whenever the
# bases agree (and is random when they disagree).
bob_bits = np.where(
    alice_bases == bob_bases,
    alice_bits,
    np.random.randint(2, size=n),
)

# Sifting: keep only positions where Alice and Bob chose the same basis.
sifted = alice_bases == bob_bases
alice_key = alice_bits[sifted]
bob_key = bob_bits[sifted]
print(f"Sifted bits: {sifted.sum()} of {n}")

errors = int(np.sum(alice_key != bob_key))
qber = errors / len(alice_key)
print(f"QBER (no eavesdropper): {qber:.3f}  (expect ~0.0)")

# With an eavesdropper: Eve measures in random bases, disturbing the states.
eve_bases = np.random.randint(2, size=n)
eve_bits = np.where(alice_bases == eve_bases, alice_bits, np.random.randint(2, size=n))
bob_bits_eve = np.where(eve_bases == bob_bases, eve_bits, np.random.randint(2, size=n))

bob_key_eve = bob_bits_eve[sifted]
errors_eve = int(np.sum(alice_key != bob_key_eve))
qber_eve = errors_eve / len(alice_key)
print(f"QBER (with eavesdropper): {qber_eve:.3f}  (expect ~0.25)")
print(f"Eavesdropper detected: {qber_eve > 0.1}")

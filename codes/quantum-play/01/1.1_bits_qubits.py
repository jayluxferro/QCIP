"""
Bits vs. qubits: vector representations and measurement probabilities.

A classical bit is either 0 or 1. A qubit is a normalized superposition
|psi> = a|0> + b|1> with |a|^2 + |b|^2 = 1. Measuring a qubit yields
|0> with probability |a|^2 and |1> with probability |b|^2.

@author: Jay (@jayluxferro)
"""

from math import sqrt, pow
import numpy as np


def test_for_normalization(a: float, b: float) -> None:
    """Assert |a|^2 + |b|^2 == 1 (to one decimal place)."""
    assert round(pow(a, 2) + pow(b, 2), 1) == 1.0


alpha = sqrt(1 / 2)
beta = sqrt(1 / 2)

# A valid qubit state must be normalized.
test_for_normalization(alpha, beta)

# Vector representations of classical bits and qubits.
bits = {
    "0": np.array([1, 0]),  # classical 0
    "1": np.array([0, 1]),  # classical 1
    "|0>": np.array([1, 0]),  # collapses to classical 0
    "|1>": np.array([0, 1]),  # collapses to classical 1
    "a|0> + b|1>": np.array([alpha, beta]),
}

# Print the vectors.
for b in bits:
    print(b, ": ", bits[b])
print("-----------------")

# Measurement probabilities for each state.
for b in bits:
    value = bits[b]
    print(b, ": ", value)
    prob_zero = pow(value[0], 2)
    prob_one = pow(value[1], 2)
    print("zero measurement: ", prob_zero)
    print("one measurement: ", prob_one)
    print("------------")

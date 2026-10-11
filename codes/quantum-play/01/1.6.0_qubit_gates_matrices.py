"""
Quantum gates as matrices, and their action on qubit states.

Single-qubit gates (id, x, z, h) act on single-qubit states; two-qubit
gates (cx, swap) act on two-qubit states.

@author: Jay (@jayluxferro)
"""

import numpy as np
from math import sqrt

ROUND_OFF = 3


def print_lines():
    print("_" * 50)


# Qubit states.
qubits = {
    "|0>": np.array([1, 0]),
    "|1>": np.array([0, 1]),
    "(|0> + |1>)/√2": 1 / sqrt(2) * np.array([1, 1]),
    "(|0> - |1>)/√2": 1 / sqrt(2) * np.array([1, -1]),
}

print("Vector representations of qubits:")
print_lines()
for q in qubits:
    print(q, "\n", qubits[q].round(ROUND_OFF))

# Single-qubit gates.
gates = {
    "id": np.array([[1, 0], [0, 1]]),
    "x": np.array([[0, 1], [1, 0]]),
    "z": np.array([[1, 0], [0, -1]]),
    "h": 1 / sqrt(2) * np.array([[1, 1], [1, -1]]),
}

print("\nMatrix representations of single-qubit gates:")
print_lines()
for g in gates:
    print(g, "\n", gates[g].round(ROUND_OFF))

print("\nGate manipulation of qubits:")
print_lines()
for g in gates:
    print("Gate:", g)
    for q in qubits:
        print(q, "\n", qubits[q].round(ROUND_OFF), "->", np.dot(gates[g], qubits[q]).round(ROUND_OFF))
    print()

# Two-qubit states and gates.
two_qubits = {
    "|00>": np.array([1, 0, 0, 0]),
    "|01>": np.array([0, 1, 0, 0]),
    "|10>": np.array([0, 0, 1, 0]),
    "|11>": np.array([0, 0, 0, 1]),
}

two_gates = {
    "cx": np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]),
    "swap": np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]),
}

print("\nMatrix representations of two-qubit gates:")
print_lines()
for g in two_gates:
    print(g, "\n", two_gates[g].round(ROUND_OFF))

print("\nGate manipulation of two-qubit states:")
print_lines()
for g in two_gates:
    print("Gate:", g)
    for b in two_qubits:
        print(b, "\n", two_qubits[b], "->", np.dot(two_gates[g], two_qubits[b]))
    print()

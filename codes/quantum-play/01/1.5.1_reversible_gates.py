import numpy as np
from math import sqrt

# Set up the basic matrices
print("Reversible quantum gates")
print("------------------------------")

qubits = {
    "|0>": np.array([1, 0]),
    "|1>": np.array([0, 1]),
    "(|0> + |1>)/√2": 1 / sqrt(2) * np.array([1, 1]),
}

for q in qubits:
    print(q, "\n", qubits[q])
print("\n")

print("Matrix representations of our gates:")
print("-------------------------------------")
gates = {
    "id": np.array([[1, 0], [0, 1]]),
    "x": np.array([[0, 1], [1, 0]]),
    "y": np.array([[0, -1.0j], [1.0j, 0]]),
    "z": np.array([[1, 0], [0, -1]]),
    "h": 1 / sqrt(2) * np.array([[1, 1], [1, -1]]),
    "s": np.array([[1, 0], [0, 1j]]),
}
diff = ""
for g in gates:
    print("\n", g, "\n", gates[g].round(3))
    if gates[g].all == np.matrix.conjugate(gates[g]).all:
        diff = g + " (Same as original)"
    else:
        diff = g + "† (Complex numbers conjugated)"

    print("Reversed", g, "=", diff, "\n", np.matrix.conjugate(gates[g]).round(3))

print("\n")


# Demonstrate that the basic quantum gates are reversible
# by applying the gate then its’ complex conjugate,
# and then comparing the outcome with the input.

for g in gates:
    input("Press enter...")
    print("Gate:", g)
    print("-------")
    for q in qubits:
        print("\nOriginal qubit: ", q, "\n", qubits[q].round(3))
        print("Qubit after", g, "gate: \n", np.dot(gates[g], qubits[q]).round(3))
        print(
            "Qubit after reversed",
            g,
            "gate.",
            "\n",
            np.dot(np.dot(gates[g], qubits[q]), np.matrix.conjugate(gates[g])).round(3),
        )
    print("\n")

"""
Demonstrate that quantum gates are reversible (unitary).

Applying a gate U and then its adjoint U† returns the original state:
U† U |psi> = |psi>.

@author: Jay (@jayluxferro)
"""

import numpy as np
from math import sqrt

qubits = {
    "|0>": np.array([1, 0]),
    "|1>": np.array([0, 1]),
    "(|0> + |1>)/√2": 1 / sqrt(2) * np.array([1, 1]),
}

gates = {
    "id": np.array([[1, 0], [0, 1]]),
    "x": np.array([[0, 1], [1, 0]]),
    "y": np.array([[0, -1j], [1j, 0]]),
    "z": np.array([[1, 0], [0, -1]]),
    "h": 1 / sqrt(2) * np.array([[1, 1], [1, -1]]),
    "s": np.array([[1, 0], [0, 1j]]),
}

for name, gate in gates.items():
    print(f"{name} =\n{gate.round(3)}\n")
    # The adjoint (conjugate transpose) is the inverse for a unitary gate.
    adjoint = gate.conj().T
    is_unitary = np.allclose(gate @ adjoint, np.eye(2))
    print(f"{name}† =\n{adjoint.round(3)}  (unitary: {is_unitary})\n")

print("Reversibility check (U† U |psi> == |psi>):")
for name, gate in gates.items():
    adjoint = gate.conj().T
    for q_name, q in qubits.items():
        original = q
        after = gate @ q
        restored = adjoint @ after
        print(
            f"{name} on {q_name}: {original} -> {after.round(3)} "
            f"-> {restored.round(3)}  (restored: {np.allclose(original, restored)})"
        )
    print()

"""
Create and measure the four Bell (maximally entangled) two-qubit states.

|Φ+> = (|00> + |11>)/√2    |Φ-> = (|00> - |11>)/√2
|Ψ+> = (|01> + |10>)/√2    |Ψ-> = (|01> - |10>)/√2

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def bell_state(kind: str) -> QuantumCircuit:
    """Return a circuit that prepares one of the four Bell states."""
    qc = QuantumCircuit(2, 2)

    # H + CNOT produces |Φ+>; a Z/X tweak yields the other three.
    qc.h(0)
    qc.cx(0, 1)
    if kind == "phi_plus":
        pass
    elif kind == "phi_minus":
        qc.z(0)
    elif kind == "psi_plus":
        qc.x(1)
    elif kind == "psi_minus":
        qc.x(1)
        qc.z(0)
    else:
        raise ValueError("kind must be one of phi_plus, phi_minus, psi_plus, psi_minus")

    qc.measure([0, 1], [0, 1])
    return qc


sim = AerSimulator()
for kind in ["phi_plus", "phi_minus", "psi_plus", "psi_minus"]:
    qc = bell_state(kind)
    qc.draw("mpl")
    plt.show()
    counts = sim.run(qc, shots=2048).result().get_counts(qc)
    print(f"{kind}: {counts}")
    plot_histogram(counts, title=kind)
    plt.show()

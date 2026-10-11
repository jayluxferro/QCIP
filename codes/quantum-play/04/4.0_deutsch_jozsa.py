"""
Deutsch-Jozsa algorithm.

Determines whether a function f: {0,1}^n -> {0,1} is constant (all outputs
equal) or balanced (half 0, half 1) using a single quantum query, versus
2^(n-1) + 1 classical queries in the worst case.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def deutsch_jozsa(n: int, balanced: bool) -> QuantumCircuit:
    """Build a Deutsch-Jozsa circuit with a constant or balanced oracle."""
    qc = QuantumCircuit(n + 1, n)

    # Output qubit starts in |1>; Hadamards put everything in superposition.
    qc.x(n)
    qc.h(range(n + 1))
    qc.barrier()

    if balanced:
        # Balanced oracle: f(x) = parity of x (XOR of all input bits).
        for i in range(n):
            qc.cx(i, n)
    # else: constant oracle (f = 0) applies no operation.
    qc.barrier()

    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc


n = 3
sim = AerSimulator()

for balanced in [False, True]:
    qc = deutsch_jozsa(n, balanced)
    qc.draw("mpl")
    plt.show()

    counts = sim.run(qc, shots=1024).result().get_counts(qc)
    outcome = max(counts, key=counts.get)
    is_constant = outcome == "0" * n
    print(f"Oracle balanced={balanced} -> measured {outcome} -> constant={is_constant}")
    plot_histogram(counts)
    plt.show()

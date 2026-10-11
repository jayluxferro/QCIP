"""
Grover's search algorithm.

Finds a marked item among N = 2^n entries in O(sqrt(N)) queries, versus
O(N) classically, by iterating an oracle (phase flip on the marked state)
and a diffusion operator (amplitude amplification).

@author: Jay (@jayluxferro)
"""

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def grover_oracle(qc: QuantumCircuit, marked: int, n: int) -> None:
    """Flip the phase of the marked computational basis state."""
    for i in range(n):
        if (marked >> i) & 1 == 0:
            qc.x(i)
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)  # phase flip on |11...1>
    qc.h(n - 1)
    for i in range(n):
        if (marked >> i) & 1 == 0:
            qc.x(i)


def diffusion(qc: QuantumCircuit, n: int) -> None:
    """Amplitude amplification about the mean (Grover diffusion)."""
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))


def grover(n: int, marked: int) -> QuantumCircuit:
    iterations = int(np.floor(np.pi / 4 * np.sqrt(2**n)))
    qc = QuantumCircuit(n, n)
    qc.h(range(n))
    for _ in range(iterations):
        grover_oracle(qc, marked, n)
        diffusion(qc, n)
    qc.measure(range(n), range(n))
    return qc


n = 3
marked = 6  # binary 110
sim = AerSimulator()

qc = grover(n, marked)
qc.draw("mpl")
plt.show()

counts = sim.run(qc, shots=2048).result().get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()

found = max(counts, key=counts.get)
print(f"Marked state: {format(marked, '0%db' % n)}")
print(f"Most likely outcome: {found}")
print(f"Found: {int(found, 2) == marked}")

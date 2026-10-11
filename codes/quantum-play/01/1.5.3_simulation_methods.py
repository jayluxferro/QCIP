"""
Double coin toss across multiple AerSimulator methods.

Compares the measurement counts produced by the statevector, stabilizer,
extended_stabilizer, density_matrix and matrix_product_state simulation
methods (Assignment I).

@author: Jay (@jayluxferro)
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

simulation_methods = [
    "statevector",
    "stabilizer",
    "extended_stabilizer",
    "density_matrix",
    "matrix_product_state",
]

shots = 15000
coins = 2

q = QuantumRegister(coins)
c = ClassicalRegister(coins)

qc = QuantumCircuit(q, c)
for coin in range(coins):
    qc.h(q[coin])  # 50-50 chance of occurrence

qc.measure(q, c)

qc.draw("mpl")
plt.show()

all_counts = []
for method in simulation_methods:
    simulator = AerSimulator(method=method)
    job = simulator.run(qc, shots=shots)
    results = job.result()
    counts = results.get_counts(qc)
    print(f"Counts for {method}: {counts}")
    all_counts.append(counts)

plot_histogram(
    all_counts,
    title="Counts for different simulation methods",
    legend=simulation_methods,
    figsize=(9 * coins, 5),
)
plt.show()

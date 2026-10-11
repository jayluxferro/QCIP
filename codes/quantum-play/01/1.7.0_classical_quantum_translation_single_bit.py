"""
Compare two single bits classically and with a quantum circuit.

The quantum circuit computes a XOR b into a target qubit: the target is
flipped once for each set input bit, so measuring 0 means "equal" and 1
means "not equal".

@author: Jay (@jayluxferro)
"""

from time import time

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def are_bits_equal_classical(a: int, b: int) -> bool:
    return (a ^ b) == 0


def are_bits_equal_quantum(a: int, b: int) -> QuantumCircuit:
    qc = QuantumCircuit(3, 1)

    if a == 1:
        qc.x(0)
    qc.cx(0, 2)

    if b == 1:
        qc.x(1)
    qc.cx(1, 2)

    qc.measure(2, 0)
    return qc


a = 0
b = 0

# Classical computation.
start_time = time()
result_classical = are_bits_equal_classical(a, b)
end_time = time()
print("Classical result: ", result_classical)
print("Classical execution time: ", end_time - start_time, " seconds")
print("*" * 100)

# Quantum computation.
sim = AerSimulator()
qc = are_bits_equal_quantum(a, b)
qc = transpile(qc, sim)
qc.draw("mpl")
plt.show()

job = sim.run(qc, shots=1)
results = job.result()
counts = results.get_counts(qc)
outcome = max(counts, key=counts.get)
plot_histogram(counts)
plt.show()

print("Quantum result: ", int(outcome, 2) == 0)
print("Quantum execution time: ", results.metadata["time_taken_execute"], " seconds")

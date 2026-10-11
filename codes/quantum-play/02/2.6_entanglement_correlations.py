"""
Measurement correlations in a Bell pair.

Measuring one qubit of a Bell pair determines the other: for |Φ+>, the two
qubits always agree (both 0 or both 1), even though each is random on its
own. This is the signature of entanglement.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.cx(q[0], q[1])
qc.measure(q, c)

sim = AerSimulator()
counts = sim.run(qc, shots=2048).result().get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()

# Only |00> and |11> occur: the two qubits always agree.
agree = sum(v for k, v in counts.items() if k[0] == k[1])
total = sum(counts.values())
print(f"Agreement rate: {agree / total:.3f} (expect 1.0 for |Φ+>)")

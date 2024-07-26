"""
Quantum coin toss (single)
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.measure(q, c)

qc.draw('mpl')
plt.show()

# install aer qasm simulator (https://github.com/Qiskit/qiskit-aer) -> pip install qiskit-aer

# initialize our simulator / backend
simulator = AerSimulator()

# run the circuit on the simulator
job = simulator.run(qc)

# get the results
results = job.result()
print(results.results[0].shots) # number of iterations (shots)

# counts
counts = results.get_counts(qc) # give us the counts for each basis

print(counts)
plot_histogram(counts)
plt.show()
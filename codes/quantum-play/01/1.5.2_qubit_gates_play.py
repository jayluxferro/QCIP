"""
Implementation of qubit gates and their effects on qubit states.
"""

from qiskit import QuantumCircuit, transpile
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

### Single Qubit Gates and States

# zero state
qc = QuantumCircuit(1, 1)
qc.initialize([1, 0], [0])  #

## Applying X gate
qc.x(0)

## Measurement
qc.measure(0, 0)

## Visualize
qc.draw("mpl")

sim = AerSimulator()
# optimize circuit
qc = transpile(qc, sim)
plt.title("|0> state")
plt.show()

job = sim.run(qc, shots=1)  # number of iterations
result = job.result()

counts = result.get_counts(qc)
plot_histogram(counts)
plt.show()

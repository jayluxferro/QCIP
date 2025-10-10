"""
Implementation of qubit gates and their effects on qubit states.
"""

from qiskit import QuantumCircuit, transpile
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

### Single Qubit Gate and State

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

job = sim.run(qc, shots=1024)  # number of iterations
result = job.result()

counts = result.get_counts(qc)
plot_histogram(counts)
plt.show()


### Multiple Qubit Gate and State

# one zero state
qc = QuantumCircuit(2, 2)
qc.initialize([0, 1], [0])

## Applying CNOT or CX gate
qc.cx(0, 1)

## Measurement
qc.measure(0, 0)
qc.measure(1, 1)

## Visualize
qc.draw("mpl")

sim = AerSimulator()
# optimize circuit
qc = transpile(qc, sim)
plt.title("|10> state")
plt.show()

job = sim.run(qc, shots=1024)  # number of iterations
result = job.result()

counts = result.get_counts(qc)
plot_histogram(counts)
plt.show()

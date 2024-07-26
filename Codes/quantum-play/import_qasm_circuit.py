from qiskit import QuantumCircuit, qasm3
import matplotlib.pyplot as plt

circ: QuantumCircuit = qasm3.load('./random_circuit.qasm') # pip install qiskit_qasm3_import
circ.draw('mpl')
plt.show()
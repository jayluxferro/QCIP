"""
Export a quantum circuit to OpenQASM format.

@author: Jay (@jayluxferro)
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, qasm2 as qasm
import matplotlib.pyplot as plt

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.measure(q, c)

qc.draw("mpl")
plt.show()

# Convert the circuit to OpenQASM and write it to the (gitignored) out/ dir.
with open("out/single_coin_toss.qasm", "w") as f:
    f.write(qasm.dumps(qc))

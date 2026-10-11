"""
Three-qubit bit-flip repetition code.

Encodes a logical qubit across three physical qubits, measures a two-bit
syndrome via ancillas to detect a single bit-flip error, and identifies the
errored qubit so it can be corrected.

Syndrome (s1, s0):
  00 -> no error        01 -> error on q0
  11 -> error on q1     10 -> error on q2

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Register layout: q = data qubits, a = syndrome ancillas.
q = QuantumRegister(3, "q")
a = QuantumRegister(2, "a")
cr_data = ClassicalRegister(3, "data")
cr_syn = ClassicalRegister(2, "syn")

qc = QuantumCircuit(q, a, cr_data, cr_syn)

# Encode logical |1> -> |111>.
qc.x(q[0])
qc.cx(q[0], q[1])
qc.cx(q[0], q[2])
qc.barrier()

# Error: a single bit flip on qubit 1.
qc.x(q[1])
qc.barrier()

# Syndrome measurement: a0 = q0 XOR q1, a1 = q1 XOR q2.
qc.cx(q[0], a[0])
qc.cx(q[1], a[0])
qc.cx(q[1], a[1])
qc.cx(q[2], a[1])
qc.measure(a, cr_syn)

# Decode (reverse the encoding) and measure the data qubits for verification.
qc.cx(q[0], q[2])
qc.cx(q[0], q[1])
qc.measure(q, cr_data)

qc.draw("mpl")
plt.show()

sim = AerSimulator()
counts = sim.run(qc, shots=1024).result().get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()

outcome = max(counts, key=counts.get)
syn, data = outcome.split()  # two registers are space-separated in counts

# Map the syndrome (a1, a0) to the errored qubit.
syndrome = {"00": "no error", "01": "q0", "11": "q1", "10": "q2"}
print(f"Syndrome: {syn} -> error on {syndrome.get(syn, syn)}")
print(f"Decoded data qubits: {data}")
print(f"Correction would restore logical |1>")

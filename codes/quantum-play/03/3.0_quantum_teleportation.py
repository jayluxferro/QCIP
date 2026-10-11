"""
Quantum teleportation: transfer a qubit state using a shared Bell pair.

Alice and Bob share the entangled state |Φ+>. Alice entangles the state she
wants to send (on q0) with her half of the Bell pair, measures her two
qubits, and sends the two classical bits to Bob, who applies the matching
correction to recover the state on his qubit.

Here we teleport |1>; Bob's qubit should deterministically end up in |1>.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

q = QuantumRegister(3, "q")
c = ClassicalRegister(3, "c")
qc = QuantumCircuit(q, c)

# The state to teleport: |1> on q0.
qc.x(q[0])

# Shared Bell pair |Φ+> on q1 (Alice) and q2 (Bob).
qc.h(q[1])
qc.cx(q[1], q[2])
qc.barrier()

# Alice entangles q0 with q1 and measures both.
qc.cx(q[0], q[1])
qc.h(q[0])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.barrier()

# Bob applies corrections based on Alice's two classical bits.
with qc.if_test((c[0], 1)):
    qc.z(q[2])
with qc.if_test((c[1], 1)):
    qc.x(q[2])

qc.measure(q[2], c[2])

qc.draw("mpl")
plt.show()

sim = AerSimulator()
counts = sim.run(qc, shots=2048).result().get_counts(qc)
print(counts)
plot_histogram(counts)
plt.show()

# Bob's qubit (the leftmost bit, c[2]) should always be 1, regardless of
# Alice's random bits. (Qiskit orders counts most-significant bit first.)
bob_is_one = all(k[0] == "1" for k in counts)
print(f"Bob's qubit is always |1>: {bob_is_one}")

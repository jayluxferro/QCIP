"""
Superdense coding: send two classical bits using a single qubit.

Alice and Bob share the Bell state |Φ+>. Alice encodes two classical bits
by applying one of {I, X, Z, ZX} to her qubit, then sends it. Bob applies
CX and H to decode both bits with a single qubit transmission.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def superdense_coding(bits: tuple) -> QuantumCircuit:
    q = QuantumRegister(2)
    c = ClassicalRegister(2)
    qc = QuantumCircuit(q, c)

    # Shared Bell pair |Φ+>.
    qc.h(q[0])
    qc.cx(q[0], q[1])
    qc.barrier()

    # Alice encodes two bits on her qubit q0.
    b0, b1 = bits
    if b0 == 1:
        qc.z(q[0])
    if b1 == 1:
        qc.x(q[0])
    qc.barrier()

    # Bob decodes.
    qc.cx(q[0], q[1])
    qc.h(q[0])
    qc.measure(q, c)
    return qc


sim = AerSimulator()
for bits in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    qc = superdense_coding(bits)
    qc.draw("mpl")
    plt.show()
    counts = sim.run(qc, shots=1024).result().get_counts(qc)
    # Reverse the bitstring so leftmost = q0, matching the (b0, b1) order.
    outcome = max(counts, key=counts.get)[::-1]
    print(f"Sent {bits}, decoded {outcome}")
    plot_histogram(counts, title=f"Sent {bits}")
    plt.show()

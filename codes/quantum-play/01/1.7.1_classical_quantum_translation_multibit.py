"""
Compare two multi-bit numbers classically and with a quantum circuit.

Each bit position gets its own XOR block: the per-position target qubit
flips to 1 whenever the two bits differ. If every measured target is 0,
the two numbers are equal.

@author: Jay (@jayluxferro)
"""

from time import time

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def bits_padding(a: int, b: int) -> tuple:
    """Return the zero-padded binary strings of a and b, same length."""
    a = bin(a)[2:]
    b = bin(b)[2:]
    width = max(len(a), len(b))
    return a.zfill(width), b.zfill(width)


def compare_classical(a: int, b: int) -> bool:
    return a == b


def compare_quantum(a: int, b: int) -> bool:
    a_bits, b_bits = bits_padding(a, b)
    n = len(a_bits)

    qr = QuantumRegister(3 * n)
    cr = ClassicalRegister(n)
    qc = QuantumCircuit(qr, cr)

    for i in range(n):
        a_bit = int(a_bits[i])
        b_bit = int(b_bits[i])
        target = 3 * i + 2

        # A
        if a_bit == 1:
            qc.x(3 * i)
        qc.cx(3 * i, target)

        # B
        if b_bit == 1:
            qc.x(3 * i + 1)
        qc.cx(3 * i + 1, target)

        qc.measure(target, i)

    qc.draw("mpl")
    plt.title("Before transpilation")
    plt.show()

    sim = AerSimulator()
    qc = transpile(qc, sim)
    qc.draw("mpl")
    plt.title("After transpilation")
    plt.show()

    job = sim.run(qc, shots=1)
    results = job.result()
    counts = results.get_counts(qc)
    plot_histogram(counts)
    plt.show()

    outcome = max(counts, key=counts.get)
    return outcome == "0" * n


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Classical compare results: ", compare_classical(a, b))
print("Quantum compare results: ", compare_quantum(a, b))

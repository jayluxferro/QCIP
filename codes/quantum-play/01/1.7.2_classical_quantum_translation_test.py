"""
Property-style test: classical vs. quantum multi-bit comparison.

Increments the second operand and asserts that the classical and quantum
comparison circuits always agree. Exits loudly on the first mismatch.

@author: Jay (@jayluxferro)
"""

from time import time

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator


def bits_padding(a: int, b: int) -> tuple:
    a = bin(a)[2:]
    b = bin(b)[2:]
    width = max(len(a), len(b))
    return a.zfill(width), b.zfill(width)


def compare_classical(a: int, b: int) -> bool:
    return a == b


def compare_quantum(a: int, b: int, sim: AerSimulator) -> bool:
    a_bits, b_bits = bits_padding(a, b)
    n = len(a_bits)

    qr = QuantumRegister(3 * n)
    cr = ClassicalRegister(n)
    qc = QuantumCircuit(qr, cr)

    for i in range(n):
        a_bit = int(a_bits[i])
        b_bit = int(b_bits[i])
        target = 3 * i + 2

        if a_bit == 1:
            qc.x(3 * i)
        qc.cx(3 * i, target)

        if b_bit == 1:
            qc.x(3 * i + 1)
        qc.cx(3 * i + 1, target)

        qc.measure(target, i)

    qc = transpile(qc, sim)
    job = sim.run(qc, shots=1)
    counts = job.result().get_counts(qc)
    outcome = max(counts, key=counts.get)
    return outcome == "0" * n


a = 1
b = 0
sim = AerSimulator()

while True:
    print(f"[compare] a={a} and b={b}")

    start_time = time()
    result_classical = compare_classical(a, b)
    classical_time = time() - start_time
    print("Classical result:", result_classical)
    print("Classical execution time:", classical_time, "seconds")

    start_time = time()
    result_quantum = compare_quantum(a, b, sim)
    quantum_time = time() - start_time
    print("Quantum result:", result_quantum)
    print("Quantum execution time:", quantum_time, "seconds")

    assert result_classical == result_quantum, (
        f"Mismatch between classical and quantum results for a={a} and b={b}"
    )

    b += 1
    print(f"[ok] All good for a={a} and b={b}! Moving to the next pair...\n")

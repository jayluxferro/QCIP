from time import time
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


# ............
# Classical
# ............
def format_bits(number: int) -> list:
    return list(bin(number)[2:])


def bits_padding(a: list, b: list) -> tuple:
    if len(a) >= len(b):
        b = list("".join(b).zfill(len(a)))
    else:
        a = list("".join(a).zfill(len(b)))

    return (a, b)


# ............
# Classical
# ............
def are_bits_equal_classical(a: int, b: int) -> bool:
    return a == b


# ............
# Quantum
# ............
def are_bits_equal_quantum(a: int, b: int) -> QuantumCircuit:
    _a = format_bits(a)
    _b = format_bits(b)
    (_a, _b) = bits_padding(_a, _b)
    _a.reverse()
    _b.reverse()

    num_qubits = (len(_a) * 2) + 1
    target_qubit = num_qubits - 1
    qc = QuantumCircuit(num_qubits, 1)

    qubit_index = 0
    for _index in range(len(_a)):
        # A
        if int(_a[_index]) == 1:
            qc.x(qubit_index)
        qc.cx(qubit_index, target_qubit)

        # B
        if int(_b[_index]) == 1:
            qc.x(qubit_index + 1)
        qc.cx(qubit_index + 1, target_qubit)

        qubit_index += 2

    qc.measure(target_qubit, 0)
    return qc


# Example
a = 1
b = 0

while True:
    print("[⏳] Comparing a={} and b={}".format(a, b))
    # Measure execution time
    start_time = time()
    result_classical = are_bits_equal_classical(a, b)
    end_time = time()

    execution_time_classical = end_time - start_time
    correctness_classical = result_classical

    print("Classical Result:", correctness_classical)
    print("Classical Execution Time:", execution_time_classical, "seconds")

    qc = are_bits_equal_quantum(a, b)
    sim = AerSimulator()
    # optimize circuit
    qc = transpile(qc, sim)

    job = sim.run(qc, shots=1)  # number of iterations
    result = job.result()

    counts = result.get_counts(qc)
    most_likely = max(counts, key=counts.get)
    correctness_quantum = int(most_likely, 2) == 0

    print("Quantum Result:", correctness_quantum)
    print("Quantum Execution Taken: ", result.metadata["time_taken_execute"], "seconds")

    assert (
        correctness_classical == correctness_quantum
    ), "Mismatch between classical and quantum results for a={} and b={}".format(a, b)
    b += 1
    print("[✅] All good for a={} and b={}! Moving to the next pair...".format(a, b))
    print("\n")
    print("\n")

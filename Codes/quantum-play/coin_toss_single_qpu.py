"""
Quantum coin toss (single) QPU
"""
import os
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create quantum circuit
q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
# qc.h(q[0])
qc.measure(q, c)

qc.draw('mpl')
plt.show()

service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token=os.getenv('QTOKEN')
)

backend = service.least_busy(operational=True, simulator=False)

simulator = Sampler(backend)

# run the circuit on the simulator
job = simulator.run([qc], shots=2048)
print(f"job id: {job.job_id()}")

# get the results
results = job.result()
print(results.results[0].shots) # number of iterations (shots)

# counts
counts = results.get_counts(qc) # give us the counts for each basis

print(counts)
plot_histogram(counts)
plt.show()
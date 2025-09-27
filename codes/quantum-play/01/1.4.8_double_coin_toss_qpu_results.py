"""
Double coin toss QPU Results
"""

from qiskit_ibm_runtime import QiskitRuntimeService
from dotenv import load_dotenv
from os import getenv
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

load_dotenv()

# Run on QPU
service = QiskitRuntimeService(
    channel="ibm_quantum_platform", instance=getenv("CRN"), token=getenv("API_KEY")
)

job_id = input("Enter your job ID: ").strip().rstrip()
job = service.job(job_id)
job_result = job.result()
print(job_result[0].data)

job_result = job_result[0].data.c0

iterations = job_result.num_shots
print(iterations)

# counts
counts = job_result.get_counts()
print(counts)

plot_histogram(counts)
plt.show()

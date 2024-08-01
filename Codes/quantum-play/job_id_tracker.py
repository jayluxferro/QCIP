from qiskit_ibm_runtime import QiskitRuntimeService
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

job_id = input('Enter job id: ')
service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token=os.getenv('QTOKEN')
)
job = service.job(job_id=job_id.strip().rstrip())
job_result = job.result()
print(job_result)
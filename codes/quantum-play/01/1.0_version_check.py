"""
Check the installed Qiskit and Qiskit IBM Runtime versions.

Run from `codes/` with:  uv run python quantum-play/01/1.0_version_check.py

@author: Jay (@jayluxferro)
"""

import qiskit
import qiskit_ibm_runtime

print(f"[+] Qiskit version: {qiskit.__version__}")
print(f"[+] Qiskit IBM runtime version: {qiskit_ibm_runtime.version.__version__}")

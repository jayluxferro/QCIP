from qiskit.circuit.random.utils import random_circuit
import matplotlib.pyplot as plt
from qiskit import qasm3

# creating a random circuit
circ = random_circuit(2, 2, measure=True)
circ.draw("mpl") # The only valid choices are text, latex, latex_source, and mpl
plt.show()

# export as qasm
circuit_code = qasm3.dumps(circ)

with open('./random_circuit.qasm', 'w') as f:
  f.write(circuit_code)
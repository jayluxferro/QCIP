"""
Visualize a single-qubit state on the Bloch sphere.

The Bloch sphere is a unit sphere: the north pole is |0>, the south pole
is |1>, and every other point is a superposition.

@author: Jay (@jayluxferro)
"""

import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_vector

plot_bloch_vector([0, 0, 1], title="Bloch Sphere")
plt.show()

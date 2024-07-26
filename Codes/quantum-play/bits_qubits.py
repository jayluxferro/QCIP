from math import sqrt, pow
import numpy as np

def test_for_normalization(a, b):
  assert(round(pow(a, 2) + pow(b, 2)) == 1)

alpha = sqrt(1/2)
beta = sqrt(1/2)

# test for normalization
test_for_normalization(alpha, beta)

# setup bits and qubits
bits = { '0': np.array([1, 0]), '1': np.array([0, 1]) , '|0>': np.array([1, 0]), '|1>': np.array([0, 1]), 'a|0> + b|1>': np.array([alpha, beta]) }

# print the vectors
for b in bits:
  print(b, ': ', bits[b]) # prints the key : value of the key

# measurement of bits and qubits
for b in bits:
  key = b
  value = bits[b]
  zero_measurement_value = value[0]
  prob = pow(zero_measurement_value, 2)
  print(b, ': ', prob)



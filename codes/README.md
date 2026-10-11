# QCIP — Course Code

Quantum Computing & Information Processing. Python code organized by chapter, managed with [`uv`](https://docs.astral.sh/uv/).

## Setup

```bash
cd codes
uv sync
```

The `*_qpu*.py` scripts read your IBM Quantum credentials from the environment
or from a `.env` file. Environment variables take precedence. Either:

```bash
# Option A — environment variables
export IBM_CHANNEL=ibm_quantum_platform
export IBM_INSTANCE=your-instance      # e.g. ibm-q/open/main
export IBM_QUANTUM_API_KEY=your-key

# Option B — .env file (for users without exported vars)
cp .env.example .env
# edit .env -> IBM_CHANNEL / IBM_INSTANCE / IBM_QUANTUM_API_KEY
```

## Run a script

```bash
uv run python quantum-play/01/1.5.0_single_coin_toss.py
```

Scripts that touch a real IBM backend (the `*_qpu*.py` files) need the three
`IBM_*` environment variables and an active IBM Quantum account; everything
else runs locally on Aer.

## Chapter map

### classical-play — Classical information & computation

| File | Topic |
|---|---|
| `1.0_factors_of_a_number.py` | Factoring |
| `1.1_binary_encoding.py` | Binary, hex, ASCII encoding |
| `1.2_logic_gates.py` | Truth tables (NOT/AND/OR/XOR/NAND) |
| `1.3_adders.py` | Half adder, full adder, ripple-carry |
| `1.4_boolean_algebra.py` | Identities & simplification |
| `1.5_reversible_gates.py` | Toffoli gate & reversibility |
| `1.6_error_correction.py` | Parity & repetition codes |
| `2.0_compute_time_per_word_size.py` | Word size vs. compute time |
| `2.1_complexity.py` | Big-O / asymptotic notation |

### quantum-play/01 — Qubits, superposition, measurement & gates

| Section | Topic |
|---|---|
| 1.0–1.4 | Version check, bits vs. qubits, Bloch sphere, simple qubit |
| 1.5 | Coin toss: simulator, QPU, simulation methods, QASM, multiple circuits |
| 1.6 | Quantum gates (matrices + Qiskit) |
| 1.7 | Classical ↔ quantum translation (bit comparison) |

### quantum-play/02 — Linear algebra, multiple qubits & entanglement

| Section | Topic |
|---|---|
| 2.0–2.2 | Linear algebra, tensor products, multi-qubit states & entanglement test |
| 2.3–2.6 | Multi-qubit circuits, Bell states, GHZ state, measurement correlations |

### quantum-play/03 — Entanglement & quantum protocols

| Section | Topic |
|---|---|
| 3.0 | Quantum teleportation |
| 3.1 | Superdense coding |
| 3.2 | Bell inequality (CHSH) violation |
| 3.3 | BB84 quantum key distribution (simulated) |

### quantum-play/04 — Quantum algorithms

| Section | Topic |
|---|---|
| 4.0 | Deutsch-Jozsa |
| 4.1 | Grover search |
| 4.2 | Quantum Fourier Transform |
| 4.3 | Quantum phase estimation |
| 4.4 | Shor's algorithm (order finding + continued fractions) |

### quantum-play/05 — Error correction & density matrices

| Section | Topic |
|---|---|
| 5.0 | Three-qubit bit-flip error correction |
| 5.1 | Density matrices, mixed states & purity |

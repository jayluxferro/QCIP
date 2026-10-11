# QCIP — Course Code

Quantum Computing & Information Processing. Python code organized by chapter, managed with [`uv`](https://docs.astral.sh/uv/).

## Setup

```bash
cd codes
uv sync
```

Secrets are read from a `.env` file (never committed). Copy the template and fill in your IBM Quantum credentials:

```bash
cp .env.example .env
# edit .env  ->  CRN="..."  API_KEY="..."
```

## Run a script

```bash
uv run python quantum-play/01/1.5.0_single_coin_toss.py
```

Scripts that touch a real IBM backend (the `*_qpu*.py` files) need a valid `.env`
and an active IBM Quantum account; everything else runs locally on Aer.

## Chapter map

### classical-play

| File | Topic |
|---|---|
| `1.0_factors_of_a_number.py` | Classical factoring |
| `2.0_compute_time_per_word_size.py` | Word size vs. computation time |

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

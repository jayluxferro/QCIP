# QCIP — Course Code

Quantum Computing & Information Processing. Python code organized by chapter, managed with [`uv`](https://docs.astral.sh/uv/).

## Setup

```bash
cd codes
uv sync
```

Secrets are read from a `.env` file (never committed). Copy the template and fill in your IBM Quantum credentials:

```bash
cp .env.example quantum-play/01/.env
# edit quantum-play/01/.env  ->  CRN="..."  API_KEY="..."
```

## Run a script

```bash
uv run python quantum-play/01/1.5.0_single_coin_toss.py
```

## Chapter map

### classical-play

| File | Topic |
|---|---|
| `1.0_factors_of_a_number.py` | Classical factoring |
| `2.0_compute_time_per_word_size.py` | Word size vs. computation time |

### quantum-play/01 — Qubits, superposition, measurement & gates

| Section | Files | Topic |
|---|---|---|
| 1.0 | `1.0_version_check.py` | Qiskit / runtime version |
| 1.1 | `1.1_bits_qubits.py` | Bits vs. qubits, normalization |
| 1.2 | `1.2_bloch_sphere_visualization.py` | Bloch sphere |
| 1.3 | `1.3_visualize_bits_qubits.py` | Visualize states on the Bloch sphere |
| 1.4 | `1.4_simple_qubit.py` | Single-qubit circuit (X gate) |
| 1.5 | `1.5.*` | Coin toss: simulator, QPU, simulation methods, QASM, multiple circuits |
| 1.6 | `1.6.*` | Quantum gates (matrices + Qiskit) |
| 1.7 | `1.7.*` | Classical ↔ quantum translation (bit comparison) |

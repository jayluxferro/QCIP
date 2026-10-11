# Quantum Computing & Information Processing (QCIP)

Course code for **Quantum Computing & Information Processing** — a Qiskit-based
introduction to quantum computing, organized by chapter and managed with
[`uv`](https://docs.astral.sh/uv/).

## Code

All runnable code lives in [`codes/`](codes/) — see its [README](codes/README.md)
for setup instructions and the full chapter map (classical foundations, qubits,
entanglement, protocols, algorithms, and error correction).

```bash
cd codes
uv sync
uv run python quantum-play/01/1.5.0_single_coin_toss.py
```

## Chapters

- **classical-play** — bits & encoding, logic gates, adders, boolean algebra, reversible logic, error correction, complexity
- **quantum-play/01** — qubits, superposition, measurement, gates
- **quantum-play/02** — linear algebra, multiple qubits, entanglement
- **quantum-play/03** — teleportation, superdense coding, CHSH, BB84
- **quantum-play/04** — Deutsch-Jozsa, Grover, QFT, phase estimation, Shor
- **quantum-play/05** — quantum error correction, density matrices

## License

[MIT](LICENSE) — Copyright (c) 2024 Jay

## Useful resources

1. <https://sites.google.com/site/jamiesikora/teaching/quantum-computation>
2. <https://quantum.cloud.ibm.com/>
3. <https://openqasm.com/index.html>

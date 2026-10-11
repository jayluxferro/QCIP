# QCIP Code Rewrite — Specification

> **Status:** implemented. Chapters 01–05 are built, the `uv` migration is complete, and the MIT license is published. This spec documents phase 1 (chapter 01 consolidation + `uv`); §10 lists the chapters added afterward.

## 1. Objective

Consolidate three drifting iterations of course code into **one canonical, harmonized, `uv`-managed** Python project under `codes/`, organized by chapter, with consistent naming, style, and no duplicated/dead artifacts. This is the "whole project rewrite."

## 2. Current state (inventory)

Three overlapping code generations exist:

| Location | Structure | Scope | Notes |
|---|---|---|---|
| `tmp/codes/` | flat | quantum ch.1 only (1.0–1.6.2) | earliest; has `aer_simulator_play.py` scratch, `.env`, stray `.jpg`/`.qasm`/`.pdf` |
| `tmp/codes-2/` | `classical-play/` + `quantum-play/` | classical 1–2; quantum 1.0–1.7.1 | most complete; different section numbering; hardcoded job IDs; `test.c`/`test` scratch |
| `codes/` (committed) | `classical-play/` + `quantum-play/01/` | classical 1–2; quantum 1.0–1.6.3 | current target; chapter-folder layout started; cleanest naming |

`codes/` is the authoritative target. `tmp/*` is source material to be merged in and then left as historical (untracked).

## 3. Target architecture

```
codes/
├── pyproject.toml          # uv-managed project
├── uv.lock                 # locked dependency resolution
├── README.md               # how to run, chapter map
├── .gitignore
├── .env.example            # CRN / API_KEY (secrets never committed)
├── classical-play/
│   ├── 1.0_factors_of_a_number.py
│   └── 2.0_compute_time_per_word_size.py
└── quantum-play/
    └── 01/                 # Chapter 1 — qubits, superposition, measurement, gates
        └── (see §4)
```

Secrets live only in `codes/quantum-play/**/.env` (gitignored). A single shared `.env.example` documents the required keys. No per-file secrets, no hardcoded job IDs.

## 4. Proposed canonical content map (quantum-play/01)

Section grouping: foundations (1.0–1.4) → coin toss & QPU (1.5) → gates (1.6) → classical↔quantum translation (1.7).

| Canonical file | Source(s) | Notes |
|---|---|---|
| `1.0_version_check.py` | codes (correct `qiskit_ibm_runtime.version.__version__`) | keep |
| `1.1_bits_qubits.py` | codes + codes-2 comments | enrich |
| `1.2_bloch_sphere_visualization.py` | codes | keep |
| `1.3_visualize_bits_qubits.py` | codes | keep |
| `1.4_simple_qubit.py` | codes-2 `1.3_simple_qubit` | X-gate flip demo |
| `1.5.0_single_coin_toss.py` | codes + codes-2 (add transpile) | |
| `1.5.1_double_coin_toss.py` | codes | |
| `1.5.2_n_coin_toss.py` | codes | |
| `1.5.3_simulation_methods.py` | codes-2 `1.4.1.1` | 5 sim methods, Assignment I |
| `1.5.4_single_coin_toss_qpu.py` | codes `1.4.3` | |
| `1.5.5_single_coin_toss_qpu_results.py` | codes `1.4.4` | |
| `1.5.6_double_coin_toss_qpu.py` | codes `1.4.7` | |
| `1.5.7_double_coin_toss_qpu_results.py` | codes `1.4.8` | |
| `1.5.8_concurrent_coin_toss_qpu.py` | codes-2 `1.5.2_coin_toss_analysis` | Assignment II |
| `1.5.9_concurrent_coin_toss_qpu_results.py` | codes-2 `1.5.2_…_results` | |
| `1.5.10_export_qc_to_qasm.py` | codes `1.4.5` | |
| `1.5.11_import_qasm_as_qc.py` | codes `1.4.6` | |
| `1.5.12_multiple_qc.py` | codes `1.4.9` + codes-2 `1.5.0/1.5.1` | include hex→bin + circuit generator |
| `1.6.0_qubit_gates_matrices.py` | codes `1.5.0` + codes-2 `1.6.0` | |
| `1.6.1_reversible_gates.py` | codes `1.5.1` | |
| `1.6.2_qubit_gates_qiskit.py` | codes `1.5.2` + codes-2 `1.6.0/1.6.1` | single + multi qubit gates |
| `1.7.0_classical_quantum_translation_single_bit.py` | codes `1.6.0` / codes-2 `1.7.0` | |
| `1.7.1_classical_quantum_translation_multibit.py` | codes `1.6.1` / codes-2 `1.7.1` | |
| `1.7.2_classical_quantum_translation_test.py` | codes `1.6.2` + `1.6.3` | single file, both circuits, assert loop |

## 5. Harmonization rules (applied to every file)

1. Consistent header: module docstring + `@author: Jay (@jayluxferro)` block comment.
2. No hardcoded IBM job IDs / tokens / CRNs — use `.env` (`load_dotenv()` + `getenv("CRN"/"API_KEY")`).
3. `qiskit_ibm_runtime` version via `qiskit_ibm_runtime.version.__version__` (not `__version__`).
4. Use `SamplerV2`, `QiskitRuntimeService`, `AerSimulator` consistently; `transpile` before running where sensible.
5. Remove commented-out dead code that duplicates; keep pedagogically useful comments.
6. No stray artifact writes into the source tree (`.jpg`/`.qasm`/`.png`/`.pdf` go to a gitignored `out/` or are not committed).

## 6. Packaging: `uv` (replaces `requirements.txt`)

- Project name `qcip`, `requires-python >= 3.11`.
- Runtime deps: `qiskit[visualization]`, `qiskit-aer`, `qiskit-ibm-runtime`, `numpy`, `matplotlib`, `python-dotenv`, `jupyter`.
- Dropped (unused by code): `mlx`, `pydantic`, `networkx`, `qiskit_algorithms`, `qiskit_optimization`, `qiskit_qasm3_import` (`pylatexenc` arrives transitively via `qiskit[visualization]`).
- Delete `codes/requirements.txt`; close dependabot PR #22.

## 7. Cleanup

Remove: `codes/quantum-play/01/.ipynb_checkpoints/`, stray `*.jpg`/`*.qasm`/`*.pdf`/`*.png`/`*.eps`/`*.c`/`test` binaries, `.DS_Store`, per-chapter `.env` (keep only `.env.example`), old `codes/.venv` (replaced by `uv` venv).

## 8. Verification

- `uv sync` resolves cleanly; `uv.lock` generated.
- `uv run python -c "import qiskit, qiskit_aer, qiskit_ibm_runtime"` passes.
- Each canonical `.py` compiles (`python -m py_compile`).
- Simulator-only scripts smoke-tested headlessly (no QPU calls) where feasible.
- `git status` clean of secrets/artifacts.

## 9. Success criteria

- Single canonical codebase; no duplicate/contradictory section numbering.
- `uv` is the only package manager (no `requirements.txt`).
- Every file follows §5 rules; no secrets or artifacts committed.
- Chapter map documented in `codes/README.md`.

## 10. Chapters added after phase 1

Following Thomas Wong, *Introduction to Classical and Quantum Computing*:

| Chapter | Topic (Wong) | Scripts |
|---|---|---|
| `quantum-play/02` | Linear algebra + multiple qubits & entanglement (Ch 3–4) | 2.0–2.6 |
| `quantum-play/03` | Entanglement & protocols — teleportation, superdense, CHSH, BB84 (Ch 6) | 3.0–3.3 |
| `quantum-play/04` | Algorithms — Deutsch-Jozsa, Grover, QFT, QPE, Shor (Ch 7) | 4.0–4.4 |
| `quantum-play/05` | Error correction & density matrices (Ch 8) | 5.0–5.1 |

All chapters are `uv`-runnable and Aer-verified (`scripts/run_all_scripts.sh`).
Course PDFs (`books/`, `assignments/`, `slides/`) were removed from tracking and
scrubbed from git history; they remain local only.

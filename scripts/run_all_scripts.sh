#!/bin/bash
# Run every non-QPU script under uv + Aer and report PASS/FAIL.
# Usage: bash tmp/run_all_scripts.sh
cd "$(dirname "$0")/../codes" || exit 1
export MPLBACKEND=Agg
pass=0; fail=0

run() {
  local desc="$1"; local input="$2"; shift 2
  local out
  if [ -n "$input" ]; then
    out=$(printf "%b" "$input" | uv run python "$@" 2>&1)
  else
    out=$(uv run python "$@" 2>&1)
  fi
  if [ $? -eq 0 ]; then
    echo "PASS  $desc"; pass=$((pass+1))
  else
    echo "FAIL  $desc"; echo "$out" | grep -iE "error|traceback|exception" | head -3; fail=$((fail+1))
  fi
}

# numpy / no plotting / no input
run "1.0 version check" "" quantum-play/01/1.0_version_check.py
run "1.1 bits qubits" "" quantum-play/01/1.1_bits_qubits.py
run "1.6.0 gates matrices" "" quantum-play/01/1.6.0_qubit_gates_matrices.py
run "1.6.1 reversible" "" quantum-play/01/1.6.1_reversible_gates.py
run "2.0 linear algebra" "" quantum-play/02/2.0_linear_algebra.py
run "2.1 tensor products" "" quantum-play/02/2.1_tensor_products.py
run "2.2 multi-qubit states" "" quantum-play/02/2.2_multi_qubit_states.py
run "3.3 bb84" "" quantum-play/03/3.3_bb84.py
run "4.4 shor" "" quantum-play/04/4.4_shor.py
run "5.1 density matrices" "" quantum-play/05/5.1_density_matrices.py
# plotting + simulator
run "1.2 bloch sphere" "" quantum-play/01/1.2_bloch_sphere_visualization.py
run "1.3 visualize bits/qubits" "" quantum-play/01/1.3_visualize_bits_qubits.py
run "1.4 simple qubit" "" quantum-play/01/1.4_simple_qubit.py
run "1.5.0 single coin toss" "" quantum-play/01/1.5.0_single_coin_toss.py
run "1.5.1 double coin toss" "" quantum-play/01/1.5.1_double_coin_toss.py
run "1.5.3 simulation methods" "" quantum-play/01/1.5.3_simulation_methods.py
run "1.5.12 multiple qc" "" quantum-play/01/1.5.12_multiple_qc.py
run "1.6.2 gates qiskit" "" quantum-play/01/1.6.2_qubit_gates_qiskit.py
run "1.7.0 translation single" "" quantum-play/01/1.7.0_classical_quantum_translation_single_bit.py
run "2.3 multi-qubit circuits" "" quantum-play/02/2.3_multi_qubit_circuits.py
run "2.4 bell states" "" quantum-play/02/2.4_bell_states.py
run "2.5 ghz state" "" quantum-play/02/2.5_ghz_state.py
run "2.6 entanglement correlations" "" quantum-play/02/2.6_entanglement_correlations.py
run "3.0 teleportation" "" quantum-play/03/3.0_quantum_teleportation.py
run "3.1 superdense coding" "" quantum-play/03/3.1_superdense_coding.py
run "3.2 chsh" "" quantum-play/03/3.2_bell_chsh.py
run "4.0 deutsch-jozsa" "" quantum-play/04/4.0_deutsch_jozsa.py
run "4.1 grover" "" quantum-play/04/4.1_grover_search.py
run "4.2 qft" "" quantum-play/04/4.2_quantum_fourier_transform.py
run "4.3 phase estimation" "" quantum-play/04/4.3_phase_estimation.py
run "5.0 bit-flip QEC" "" quantum-play/05/5.0_bit_flip_error_correction.py
# input-driven
run "1.5.2 n coin toss (n=2)" "2\n" quantum-play/01/1.5.2_n_coin_toss.py
run "1.7.1 translation multibit (10 vs 11)" "10\n11\n" quantum-play/01/1.7.1_classical_quantum_translation_multibit.py
run "classical 1.0 factors (12)" "12\n" classical-play/1.0_factors_of_a_number.py
run "classical 2.0 word size (4)" "4\n" classical-play/2.0_compute_time_per_word_size.py
# qasm export/import pair
run "1.5.10 export qasm" "" quantum-play/01/1.5.10_export_qc_to_qasm.py
run "1.5.11 import qasm" "" quantum-play/01/1.5.11_import_qasm_as_qc.py
echo "-----------------------------------"
echo "PASS=$pass FAIL=$fail"

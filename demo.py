def execute(circuit, noise_level=0.005):
    """Returns Tr[ρ |0⟩⟨0|] where ρ is the state prepared by the circuit
    executed with depolarizing noise.
    """
    noisy_circuit = circuit.with_noise(cirq.depolarize(p=noise_level))
    rho = cirq.DensityMatrixSimulator().simulate(noisy_circuit).final_density_matrix
    return rho[0, 0].real


import cirq
import mitiq

qubit = cirq.LineQubit(1)
circuit = cirq.Circuit(cirq.X(qubit) for _ in range(100))

expval = mitiq.zne.execute_with_zne(circuit, execute)

print(f"Error: {1 - expval:.3}")
# Error: 0.058

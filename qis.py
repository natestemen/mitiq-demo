from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit_aer import AerSimulator
import numpy as np


def execute(circuit):
    c = circuit.copy()
    c.save_density_matrix()

    noise_model = NoiseModel()
    error = depolarizing_error(0.005, 1)
    noise_model.add_all_qubit_quantum_error(error, ["x", "u1", "u2", "u3"])
    backend = AerSimulator(method="density_matrix", noise_model=noise_model)
    rho = backend.run(c).result().data()["density_matrix"]
    return np.asarray(rho)[0, 0].real


import qiskit
import mitiq

circuit = qiskit.QuantumCircuit(1)
for _ in range(100):
    circuit.x(0)
circuit.measure_all()

expval = mitiq.zne.execute_with_zne(circuit, execute)

print(f"Error: {1 - expval:.3}")
# Error: 0.0537

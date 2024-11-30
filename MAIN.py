from qiskit import QuantumCircuit, transpile, IBMQ, execute
from qiskit.providers.ibmq import least_busy

# Load your IBMQ account
IBMQ.load_account()

# Get the least busy backend
provider = IBMQ.get_provider(hub='ibm-q')
backend = least_busy(provider.backends(filters=lambda b: b.configuration().n_qubits >= 1 and not b.configuration().simulator))

print(f"Using backend: {backend.name()}")

# Create the quantum circuit
qc = QuantumCircuit(1, 1)
qc.h(0)  # Apply Hadamard gate to put the qubit in superposition
qc.measure(0, 0)  # Measure the qubit

# Transpile for the selected backend
qc_transpiled = transpile(qc, backend)

# Execute the circuit
job = execute(qc_transpiled, backend, shots=1)
print("Job submitted. Waiting for results...")

# Get the result
result = job.result()
counts = result.get_counts(qc)
print(f"Counts: {counts}")

# Convert the result to a random bit
random_bit = list(counts.keys())[0]
print(f"Random Bit: {random_bit}")

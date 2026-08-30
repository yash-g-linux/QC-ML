from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Put qubit 0 into superposition
qc.h(0)

# Entangle qubit 0 and qubit 1
qc.cx(0, 1)

qc.x(0)

# Measure both qubits
qc.measure([0,1], [0,1])
#qc.measure(qubit numbers array, cbit numbers array)

print("Quantum Circuit:")
print(qc)

# Simulate the circuit
simulator = AerSimulator()
job = simulator.run(qc, shots=10000)
result = job.result()

# Get measurement counts
counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)
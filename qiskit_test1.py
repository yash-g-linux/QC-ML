# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:06:56 2026

@author: space
"""

from qiskit import QuantumCircuit

# Create a simple quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit to create superposition
qc.h(0)

# Apply a CNOT gate between qubit 0 and qubit 1 to create entanglement
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Print confirmation and the circuit diagram
print("Qiskit is successfully loaded and running in Spyder!")
print(qc)

print("Hello World")
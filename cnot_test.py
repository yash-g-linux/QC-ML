from qiskit import QuantumCircuit

from qiskit.quantum_info import Statevector


qc = QuantumCircuit(3,3) # create a circuit with 3 qubits and 3 gates

qc.x(1) # turn q1 into |1>

# initial state now reads |010>

qc.cx(0,1) # cnot gate between q0 and q1

qc.cx(0,2) # cnot gate between q0 and q2

qc.cx(1,2) # cnot gate between q1 and q2

state = Statevector(qc) # the state of the qubits before measurement

qc.measure([0,1,2], [0,1,2])

print(qc)

#print the statevector in latex form |...>
for bitstring, amp in state.to_dict().items():
    if abs(amp) > 1e-10:
        # Reverse the bitstring character order to match |q0 q1 q2>
        reversed_bitstring = bitstring[::-1]
        print(f"State before measurement: |{reversed_bitstring}⟩")

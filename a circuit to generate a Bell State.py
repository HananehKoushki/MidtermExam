import cirq

# 1. Define qubits
q0 = cirq.NamedQubit("q0")
q1 = cirq.NamedQubit("q1")

# 2. Create a circuit
bell_circuit = cirq.Circuit()

# 3. Add quantum gates to the circuit
bell_circuit.append(cirq.H(q0))  # Apply Hadamard gate to qubit q0
bell_circuit.append(cirq.CNOT(q0, q1))  # Apply CNOT (controlled NOT) gate between q0 and q1

# 4. Simulate the circuit (State vector simulation)
s = cirq.Simulator()
print('Simulate the circuit:')
results = s.simulate(bell_circuit)
print(results)

# 5. Sample the circuit (Multiple runs)
bell_circuit.append(cirq.measure(q0, q1, key='result'))  # Add measurement for sampling
print(bell_circuit)
print('Sample the circuit:')
samples = s.run(bell_circuit, repetitions=10)
print(samples)
print(samples.histogram(key='result'))

import numpy as np
from qiskit.quantum_info import Statevector
# 1. Create a state vector that gives a 1/3 probability of measuring |0>.
state1 = Statevector([np.sqrt(1/3), np. sqrt(2/3)])
# 2. Create a different state vector with the same measurement probabilities.
state2 = Statevector([np.sqrt(1/3), np.sqrt(2/3)])
# 3. Verify that the probability of measuring II) for both states is 2/3.
prob_state1 = np.abs(state1.data)**2
prob_state2 = np.abs(state2.data)**2

print(f"State 1 probabilities:\nP(|0>) : {prob_state1[0]}\nP(|1>) : {prob_state1[1]}\n")
print(f"State 2 probabilities:\nP(|0>) : {prob_state2[0]}\nP(|1>) : {prob_state2[1]}\n")

if prob_state1[0] == prob_state2[0] and prob_state1[1] == prob_state2[1]:
    print("Both states have the same measurement probabilities.")

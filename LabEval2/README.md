# Deutsch-Jozsa Algorithm Implementation

## Overview
This folder contains a Python implementation of the Deutsch-Jozsa algorithm using Qiskit. The algorithm determines whether a given function \( f: \{0,1\}^n \to \{0,1\} \) is constant or balanced.

## Files
- `eval2py.py`: Contains the implementation of the Deutsch-Jozsa algorithm, including the oracle for a constant function and the circuit construction.

## How It Works
The Deutsch-Jozsa algorithm works as follows:
1. **Oracle Construction**: An oracle is created to represent the function \( f \). For a constant function, the oracle does nothing to the output qubit.
2. **Circuit Construction**: The Deutsch-Jozsa circuit is built using the oracle. The circuit applies Hadamard gates to the input qubits, applies the oracle, and then applies Hadamard gates again.
3. **Measurement**: The circuit is simulated, and the measurement results are analyzed. If the function is constant, the output will be the all-zeros string.

## Running the Code
To run the code, ensure you have Qiskit installed. You can install it using:
```bash
pip install qiskit
pip install qiskit_aer
```

Then, run the `eval2py.py` file:
```bash
python eval2py.py
```

## Expected Output
For the given function \( f(00) = f(01) = f(10) = f(11) = 0 \), the output should be a dictionary with the key `'00'` and a value of `1024` (or similar, depending on the number of shots).

## Notes
- The code is designed for a 2-qubit input. You can modify the `n` variable to test with different input sizes.
- The `create_entangled_pair` function and related code are unrelated to the Deutsch-Jozsa algorithm and can be removed for clarity. 
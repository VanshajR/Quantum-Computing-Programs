### Codes written as part of quantum computing labs, in two types of environments:

- Executed in IBM Quantum Compose, refer to the markdown file in the respective folders.
- In Qiskit, which is a python library, installation:

#### Qiskit Installation

1. Create a venv (I recommend this):

```bash
python -m venv .venv
```

Or, if using conda:

```bash
conda create -p venv python==3.10
```

2. Install Qiskit SDK:

```bash
pip install qiskit
```

If you plan to run jobs on quantum hardware, also install Qiskit Runtime:

```bash
pip install qiskit-ibm-runtime
```
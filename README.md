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

Or, do yourself a favour and use my requirements.txt file:

```bash
pip install -r requirements.txt
```

## License

The code in this repository is licensed under the MIT License — see [LICENSE](LICENSE).

Exception: the photo of the question paper in `LabEval2/` (`WhatsApp Image 2025-05-19 at 12.35.40_384478cf.jpg`) is faculty material and is not covered by this licence.

Qiskit and Qiskit Aer remain under their own licence (Apache-2.0).

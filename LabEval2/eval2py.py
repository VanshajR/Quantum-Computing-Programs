# %%
!pip install qiskit
!pip install qiskit_aer
from qiskit.quantum_info import Statevector,partial_trace

# %%
def constant_oracle(n):

    oracle = QuantumCircuit(n + 1)
    # oracle.x(n)  # for f(x)=1
    return oracle

def balanced_oracle(n):


    oracle = QuantumCircuit(n + 1)
    for i in range(n):
        oracle.cx(i, n)
    return oracle

# %%
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
def deutsch_jozsa(f_oracle, n):
    qc = QuantumCircuit(n + 1, n)
    # Step 1:  input y
    qc.x(n)
    qc.h(n)

    # Step 2:input x
    for i in range(n):
        qc.h(i)

    qc.barrier()

    # Step 3: Uf
    qc = qc.compose(f_oracle, qubits=range(n + 1))

    qc.barrier()

    # Step 4: Output
    for i in range(n):
        qc.h(i)

    # Step 5: Measure input qubits
    for i in range(n):
        qc.measure(i, i)

    return qc

# %%
# Choose number of input bits
n = 2
# Uf
oracle = constant_oracle(n)

# %%
dj_circuit = deutsch_jozsa(oracle, n)
dj_circuit.draw()

# %%
sim = Aer.get_backend('aer_simulator')
result = sim.run(dj_circuit).result()
f = result.get_counts()
f

# %%
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
def create_entangled_pair():
  qc = QuantumCircuit(3, 1)
  qc.h(0)
  qc.x([1, 2])
  qc.cx(0, 1)
  qc.cx(1, 2)
  return qc
qc = create_entangled_pair()
qc.draw()
state = Statevector(qc)
state.draw('latex') # MSB is ist

# %%




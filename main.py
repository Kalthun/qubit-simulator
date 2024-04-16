import numpy as np

# For plotting
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Qubit:
    def __init__(self, alpha: float = 1, beta: float = 0) -> None:
        self.state: np.ndarray = np.array([alpha, beta], dtype=np.complex_)
        self.normalize_state()

    def normalize_state(self) -> None:
        norm = np.linalg.norm(self.state)
        if norm == 0:
            raise ValueError("The state vector cannot be zero.")
        self.state /= norm

    def set_state(self, alpha: float, beta: float) -> None:
        self.state = np.array([alpha, beta], dtype=np.complex_)
        self.normalize_state()

    def get_state(self) -> np.ndarray:
        return self.state

    def measure(self) -> int:
        probabilities = np.abs(self.state) ** 2
        return np.random.choice([0, 1], p=probabilities)
    
    def __str__(self) -> str:
        return f'|ψ> = ({self.state[0]:.2f}|0> + {self.state[1]:.2f}|1>)'

# Example usage
q = Qubit(1/np.sqrt(2), 1/np.sqrt(2))
print(q)

# run n simulations
zeros = 0
ones = 0

for x in range(1000):
    measurement = q.measure()
    if measurement == 0:
        zeros += 1
    else:
        ones += 1

print(f'zero: {zeros}')
print(f'one: {ones}')

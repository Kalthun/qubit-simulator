import numpy as np
from numpy.typing import NDArray

# Qubit class
class Qubit:

    # Default Initializer
    def __init__(self, alpha:float = 1, beta:float = 0) -> None:
        self.state:NDArray[np.float_] = np.array([alpha, beta])
        self.normalize_state()

    def normalize_state(self) -> None:
        norm:float = np.linalg.norm(self.state)
        if norm == 0:
            raise ValueError("The state vector cannot be zero.")
        self.state /= norm

    def set_state(self, alpha:float, beta:float) -> None:
        self.state = np.array([alpha, beta])
        self.normalize_state()

    def get_state(self) -> NDArray[np.float_]:
        return self.state

    def measure(self) -> int:
        probabilities:NDArray[np.float_] = np.abs(self.state) ** 2
        return np.random.choice([0, 1], p=probabilities)

    def __str__(self) -> str:
        return f'|ψ> = ({self.state[0]:.2f}|0> + {self.state[1]:.2f}|1>)'

# Example usage:
q = Qubit(1/np.sqrt(2), 1/np.sqrt(2))

print(q)  # Print the qubit state
measurement:int = q.measure()  # Simulate measuring the qubit
print(f'Measurement result: {measurement}')

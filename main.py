import numpy as np

# Qubit class
class Qubit:
    # Default Initializer
    def __init__(self, alpha=1, beta=0):
        # A numpy array for string the values of alpha and beta
        self.state = np.array([alpha, beta])
        # nomalize the current state so that the total sum is 1
        self.normalize_state()

    # Normalize the Qubit's state
    def normalize_state(self):
        norm = np.linalg.norm(self.state)
        if norm == 0:
            raise ValueError("The state vector cannot be zero.")
        self.state /= norm

    # give a qubit a new set of values
    def set_state(self, alpha, beta):
        self.state = np.array([alpha, beta])
        self.normalize_state()


    def get_state(self):
        return self.state


    def measure(self):
        probabilities = np.abs(self.state) ** 2
        return np.random.choice([0, 1], p=probabilities)


    def __str__(self):
        return f'|ψ> = ({self.state[0]:.2f}|0> + {self.state[1]:.2f}|1>)'

# Example usage:
q = Qubit(1/np.sqrt(2), 1/np.sqrt(2))

print(q)  # Print the qubit state
measurement = q.measure()  # Simulate measuring the qubit
print(f'Measurement result: {measurement}')

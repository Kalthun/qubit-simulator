import numpy as np
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
        print(probabilities)
        return np.random.choice([0, 1], p=probabilities)

    def plot_state(self) -> None:
        # Calculate angles for Bloch sphere
        theta = 2 * np.arccos(np.abs(self.state[0]))
        phi = np.angle(self.state[1])

        # Spherical to Cartesian coordinates
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)

        # Plotting the Bloch sphere
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Draw the sphere
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        xs = np.outer(np.cos(u), np.sin(v))
        ys = np.outer(np.sin(u), np.sin(v))
        zs = np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(xs, ys, zs, color='c', alpha=0.1)
        
        # Equator
        ax.plot(np.cos(u), np.sin(u), 0, color="k", linestyle="dashed")
        
        # Poles
        ax.plot([0, 0], [0, 0], [-1, 1], color="k")

        # Qubit state
        ax.plot([0, x], [0, y], [0, z], 'r-')  # Line from origin to point
        ax.plot([x], [y], [z], 'ro')  # The point itself

        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.view_init(30, 185)

        plt.show()

    def __str__(self) -> str:
        return f'|ψ> = ({self.state[0]:.2f}|0> + {self.state[1]:.2f}|1>)'

# Example usage
q = Qubit(1/np.sqrt(2), 1/np.sqrt(2))
print(q)  # Print the qubit state
measurement = q.measure()  # Simulate measuring the qubit
print(f'Measurement result: {measurement}')
q.plot_state()  # Plot the state on a Bloch sphere

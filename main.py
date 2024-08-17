










s



import numpy as np
import matplotlib.pyplot as plt

class PhysarumSimulation:
    def __init__(self, grid_size=100, num_iterations=1000):
        self.grid_size = grid_size
        self.num_iterations = num_iterations
        self.grid = np.zeros((grid_size, grid_size))
        self.particles = np.zeros((grid_size, grid_size))
        self.particles[:] = np.nan
        self.positions = []

    def initialize_particles(self, num_particles=10):
        for _ in range(num_particles):
            x, y = np.random.randint(self.grid_size), np.random.randint(self.grid_size)
            self.particles[x, y] = 1
            self.positions.append((x, y))

    def update_particles(self):
        for pos in self.positions:
            x, y = pos
            dx, dy = self._move_direction(x, y)
            new_x, new_y = (x + dx) % self.grid_size, (y + dy) % self.grid_size
            self.grid[new_x, new_y] += 1
            self.particles[new_x, new_y] = 1
            self.positions[self.positions.index(pos)] = (new_x, new_y)

    def _move_direction(self, x, y):
        # Add your Physarum-like movement rules here
        # For example, you can implement a gradient-following behavior
        return np.random.choice([-1, 0, 1]), np.random.choice([-1, 0, 1])

    def run_simulation(self):
        self.initialize_particles()
        for _ in range(self.num_iterations):
            self.update_particles()

    def visualize(self):
        plt.figure(figsize=(8, 6))
        plt.imshow(self.grid, cmap='hot', interpolation='nearest')
        plt.title('Physarum polycephalum Simulation')
        plt.colorbar(label='Chemical Concentration')
        plt.show()

# Example usage
sim = PhysarumSimulation(grid_size=100, num_iterations=1000)
sim.run_simulation()
sim.visualize()

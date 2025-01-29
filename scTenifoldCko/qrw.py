import numpy as np
import matplotlib.pyplot as plt

# Define the number of steps
num_steps = 50

# Define the coin operator (Hadamard gate)
def hadamard_coin():
    return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

# Initialize the state of the system
def initialize_state(num_positions):
    # Start in position 0 (middle) with "up" spin
    state = np.zeros((2, num_positions), dtype=complex)  # 2 (spin states) x positions
    state[0, num_positions // 2] = 1  # Start in "up" state in the middle
    return state

# Apply the coin operator to the spin
def apply_coin_operator(state, coin_operator):
    return np.einsum('ij,jk->ik', coin_operator, state)

# Shift positions based on spin
def shift_operator(state):
    num_positions = state.shape[1]
    shifted_state = np.zeros_like(state)
    # "Up" spin moves right
    shifted_state[0, 1:] = state[0, :-1]
    # "Down" spin moves left
    shifted_state[1, :-1] = state[1, 1:]
    return shifted_state

# Perform one step of the quantum random walk
def quantum_walk_step(state, coin_operator):
    # Step 1: Apply the coin operator
    state = apply_coin_operator(state, coin_operator)
    # Step 2: Shift positions based on spin
    state = shift_operator(state)
    return state

# Simulate the quantum random walk
def simulate_quantum_walk(num_steps, num_positions):
    # Initialize state
    state = initialize_state(num_positions)
    # Define the coin operator
    coin_operator = hadamard_coin()
    # Perform the walk
    for _ in range(num_steps):
        state = quantum_walk_step(state, coin_operator)
    return state

# Probability distribution
def compute_probability_distribution(state):
    return np.sum(np.abs(state)**2, axis=0)

# Parameters
num_positions = 2 * num_steps + 1  # Ensure enough positions for the walk
state = simulate_quantum_walk(num_steps, num_positions)
prob_distribution = compute_probability_distribution(state)

# Plot results
positions = np.arange(-num_steps, num_steps + 1)
plt.bar(positions, prob_distribution, color='blue', alpha=0.7, label='Quantum Walk')
plt.xlabel('Position')
plt.ylabel('Probability')
plt.title('Quantum Random Walk Probability Distribution')
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt


def plot_construction():
    """Set up the plot layout for the simulation."""
    fig, axis = plt.subplots(1, 2, figsize=(12, 6))

    # Generated Dots
    axis[0].set_title('Randomly Generated Dots')
    axis[0].set_aspect('equal')
    axis[0].set_xlim([-1, 1])
    axis[0].set_ylim([-1, 1])
    axis[0].set_xlabel('x')
    axis[0].set_ylabel('y')

    # Plot of Approximation
    axis[1].set_title('Approximating π')
    axis[1].set_xlim([0, 1000])
    axis[1].set_ylim([2.5, 4])
    axis[1].set_xlabel('Number of Samples')
    axis[1].set_ylabel('Approximated π')
    axis[1].grid()

    return axis


def monte_carlo_pi_simulation(N_samples, update_interval=500):
    """Run the Monte Carlo simulation and update plots dynamically."""
    axis = plot_construction()

    # Initialize counters and data storage
    pi_counter = 0
    dots_x, dots_y, dots_color = [], [], []
    pi_array = []

    # Scatter and line plot placeholders
    scatter = axis[0].scatter([], [], s=5)
    plot, = axis[1].plot([], [], 'black')

    # Simulation loop
    for N in range(1, N_samples + 1):
        # Generate random point
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        dots_x.append(x)
        dots_y.append(y)

        # Check if point is inside the unit circle
        if np.sqrt(x**2 + y**2) <= 1:
            pi_counter += 1
            dots_color.append('red')
        else:
            dots_color.append('blue')

        # Approximate π
        probability = pi_counter / N
        approx_pi = 4 * probability
        pi_array.append(approx_pi)

        # Update plots at intervals
        if N % update_interval == 0:
            # Update scatter plot
            scatter.set_offsets(np.column_stack((dots_x, dots_y)))
            scatter.set_facecolors(dots_color)
            axis[0].set_title(f"Red Dots (Inside Circle): {pi_counter}, "
                              f"Blue Dots (Outside Circle): {N - pi_counter}")

            # Update π approximation plot
            plot.set_data(range(1, N + 1), pi_array)
            axis[1].set_xlim([0, N + update_interval])
            axis[1].set_ylim([min(pi_array) - 0.1, max(pi_array) + 0.1])
            axis[1].set_title(f'Approximating π ~ {approx_pi:.5f}')

            # Refresh plots
            plt.draw()
            plt.pause(0.01)

    # Show final results
    plt.show()


# Parameters
N_samples = 50_000  # Total number of samples
update_interval = 500  # Update the plots every 500 samples

# Run the simulation
monte_carlo_pi_simulation(N_samples, update_interval)

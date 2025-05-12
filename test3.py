import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and subplots
fig, (ax1, ax2) = plt.subplots(2)

# Plot data on the first subplot
ax1.plot(x, y1, color='blue', label='Sin(x)')
ax1.set_title('Sine Function')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.legend()

# Plot data on the second subplot
ax2.plot(x, y2, color='red', label='Cos(x)')
ax2.set_title('Cosine Function')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.legend()

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()

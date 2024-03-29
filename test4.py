import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and a single subplot
fig, ax = plt.subplots()

# Plot both datasets on the same subplot
ax.plot(x, y1, color='blue', label='Sin(x)')
ax.plot(x, y2, color='red', label='Cos(x)')

# Set title, labels, and legend
ax.set_title('Sine and Cosine Functions')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# Display the plot
plt.show()

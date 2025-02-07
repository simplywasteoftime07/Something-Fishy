import numpy as np
import matplotlib.pyplot as plt

# Function to compute the Mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Generate the fractal image
def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    real_vals = np.linspace(x_min, x_max, width)
    imag_vals = np.linspace(y_min, y_max, height)
    fractal = np.zeros((height, width))

    for i, y in enumerate(imag_vals):
        for j, x in enumerate(real_vals):
            fractal[i, j] = mandelbrot(complex(x, y), max_iter)

    return fractal

# Parameters for the Mandelbrot Set
width, height = 800, 600
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5
max_iter = 100

# Generate and display the Mandelbrot fractal
fractal = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
plt.imshow(fractal, cmap="inferno", extent=(x_min, x_max, y_min, y_max))
plt.colorbar(label="Iterations")
plt.title("Mandelbrot Set")
plt.show()

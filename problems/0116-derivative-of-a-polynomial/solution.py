import numpy as np

def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    return c * n * np.power(x, n-1)
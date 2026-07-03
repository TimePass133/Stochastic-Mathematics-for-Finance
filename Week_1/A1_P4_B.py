import numpy as np

P = np.array([
    [0.60, 0.30, 0.10, 0.00],
    [0.20, 0.50, 0.20, 0.10],
    [0.10, 0.30, 0.40, 0.20],
    [0.05, 0.15, 0.30, 0.50]
])

A = P.T - np.eye(4)

A[3] = np.ones(4)
b = np.array([0, 0, 0, 1])

pi = np.linalg.solve(A, b)
print([round(p, 4) for p in pi])
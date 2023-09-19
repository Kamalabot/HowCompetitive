import numpy as np

def approximate_pi(n):
    points = np.random.uniform(-1, 1, (n, 2))
    inside = np.sum(points[:,0]**2+points[:,1]**2 <= 1)
    k = inside/n
    return 4*k


n = 1000000
approximation = approximate_pi(n)
print('Approximation:', approximation)
print('Error:', abs(approximation-np.pi))
import numpy as np
import matplotlib.pyplot as plt


def midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1+x2)/2, (y1+y2)/2


def sierpinski(A, B, C, depth):
    if depth == 0:
        return
    MAB = midpoint(A, B)
    MAC = midpoint(A, C)
    MBC = midpoint(B, C)
    triangle = plt.Polygon([MAB, MAC, MBC], color='white')
    plt.gca().add_patch(triangle)
    sierpinski(A, MAB, MAC, depth-1)
    sierpinski(MAB, B, MBC, depth-1)
    sierpinski(MAC, MBC, C, depth-1)


def draw_sierpinski(depth):
    l = 50
    A, B, C = (0, 0), (l/2, (np.sqrt(3)/2)*l), (l, 0)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(xlim=[0, l], ylim=[0, B[1]])
    ax.set_aspect('equal')
    ax.axis('off')
    triangle = plt.Polygon([A, B, C], color='#343d46')
    ax.add_patch(triangle)
    sierpinski(A, B, C, depth)


depth = 6
draw_sierpinski(depth)
plt.show()

import math
import random as rnd
import alphashape
import matplotlib.pyplot as plt
from descartes import PolygonPatch

def orientation(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
    d = (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2)
    if d > 0:
        return 1
    elif d < 0:
        return -1
    else:
        return 0


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return math.sqrt((y2-y1)**2 + (x2-x1)**2)


def total_length(path):
    return sum([dist(path[i], path[i+1]) for i in range(len(path)-1)])


def polar_angle(p1, p2):
    if p1[1] == p2[1]:
        return -math.pi
    dy = p1[1]-p2[1]
    dx = p1[0]-p2[0]
    return math.atan2(dy, dx)


def graham(points):
    p0 = min(points, key=lambda p: (p[1], p[0]))
    points.sort(key=lambda p: (polar_angle(p0, p), dist(p0, p)))
    hull = []
    for i in range(len(points)):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 1:
            hull.pop()
        hull.append(points[i])
    return hull


def avoid(obstacle, start, end):
    points = obstacle+[start, end]
    hull = graham(points)
    path_1 = []
    path_2 = []
    i = hull.index(start)
    while hull[i] != end:
        path_1.append(hull[i])
        i = (i+1)%len(hull)
    path_1.append(end)
    while hull[i] != start:
        path_2.append(hull[i])
        i = (i+1)%len(hull)
    path_2.append(start)
    return min(path_1, path_2, key=lambda x: total_length(x))


obstacle = list([(rnd.randint(50, 200), rnd.randint(0, 200)) for _ in range(rnd.randint(50, 50))])
start, end = (0, 100), (250, 100)
alpha = 0.95 * alphashape.optimizealpha(obstacle)
concave = alphashape.alphashape(obstacle, alpha)
concave_pts = concave.exterior.coords.xy
fig, ax = plt.subplots()
ax.add_patch(PolygonPatch(concave, fill=True, color='blue', alpha=0.7))
hull = avoid(obstacle, start, end)
x, y = concave_pts
for src, dest in zip(hull, hull[1:]):
    plt.plot([src[0], dest[0]], [src[1], dest[1]], 'r-', linewidth=3)
plt.plot(x, y, 'b.')
plt.plot([start[0], end[0]], [start[1], end[1]], 'm.', markersize=10)
plt.show()
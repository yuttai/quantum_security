from numpy import vdot
from numpy.linalg import norm
from math import sqrt
𝝍 = [1 / 2, sqrt(3) / 2]
𝑥 = [0, 1]
print(norm(𝝍), norm(𝑥), abs(vdot(𝝍, 𝑥)) ** 2)

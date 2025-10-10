"""
Reference: https://en.wikipedia.org/wiki/Gaussian_function
"""

from numpy import exp, pi, sqrt
import sys

def gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> float:
    return 1 / sqrt(2 * pi * sigma**2) * exp(-((x - mu) ** 2) / (2 * sigma**2))


if __name__ == "__main__":
    for i in range(int(sys.argv[1])):
        print(gaussian(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])))
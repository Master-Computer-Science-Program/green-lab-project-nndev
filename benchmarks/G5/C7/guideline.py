"""
Reference: https://en.wikipedia.org/wiki/Gaussian_function
"""

import sys

def squareRoot(n, l=0.00001) :
    x = n
    count = 0

    while (1) :
        count += 1

        root = 0.5 * (x + (n / x))
        if (abs(root - x) < l) :
            break
        x = root

    return root

def exp(x, k=20):
    y = x / k
    term = 1.0
    result = 1.0
    for n in range(1, 6):
        term *= y / n
        result += term
    return result ** k

def gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> float:
    return 1 / squareRoot(2 * (22 / 7) * sigma**2) * exp(-((x - mu) ** 2) / (2 * sigma**2))

if __name__ == "__main__":
    print(gaussian(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])))
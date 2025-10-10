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


def escape_velocity(mass: float, radius: float) -> float:
    gravitational_constant = 6.67430e-11  # m^3 kg^-1 s^-2

    if radius == 0:
        raise ZeroDivisionError("Radius cannot be zero.")

    velocity = squareRoot(2 * gravitational_constant * mass / radius)
    return round(velocity, 3)


if __name__ == "__main__":
    try:
        for i in range(int(sys.argv[1])):
            print(escape_velocity(float(sys.argv[2]), float(sys.argv[3])))

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
    except ZeroDivisionError as e:
        print(e)
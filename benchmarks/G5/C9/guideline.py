"""
Title : Calculating the speed of sound

Description :
    The speed of sound (c) is the speed that a sound wave travels per unit time (m/s).
    During propagation, the sound wave propagates through an elastic medium.

    Sound propagates as longitudinal waves in liquids and gases and as transverse waves
    in solids. This file calculates the speed of sound in a fluid based on its bulk
    module and density.

    Equation for the speed of sound in a fluid:
    c_fluid = sqrt(K_s / p)

    c_fluid: speed of sound in fluid
    K_s: isentropic bulk modulus
    p: density of fluid

Source : https://en.wikipedia.org/wiki/Speed_of_sound
"""

import sys

def speed_of_sound_in_a_fluid(density: float, bulk_modulus: float) -> float:

    if density <= 0:
        raise ValueError("Impossible fluid density")
    if bulk_modulus <= 0:
        raise ValueError("Impossible bulk modulus")

    return round((bulk_modulus / density) ** 0.5, 5)


if __name__ == "__main__":
    for i in range(int(sys.argv[1])):
        print(speed_of_sound_in_a_fluid(float(sys.argv[2]), float(sys.argv[3])))
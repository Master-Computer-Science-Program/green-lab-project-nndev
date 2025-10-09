# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
#
# originally by Kevin Carson
# modified by Tupteq, Fredrik Johansson, and Daniel Nanz
# modified by Maciej Fijalkowski
# 2to3

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

def combinations(l):
    result = []
    for x in range(len(l) - 1):
        ls = l[x+1:]
        for y in ls:
            result.append((l[x],y))
    return result

PI = 3.1415927
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

BODIES = {
    'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

    'jupiter': ([4.8414314, -1.1603200, -0.1036220],
                [1.6600766e-03 * DAYS_PER_YEAR,
                 7.6990112e-03 * DAYS_PER_YEAR,
                 -6.9046002e-05 * DAYS_PER_YEAR],
                9.5479194e-04 * SOLAR_MASS),

    'saturn': ([8.3433667, 4.1247986, -0.4035234],
               [-2.7674251e-03 * DAYS_PER_YEAR,
                4.9985280e-03 * DAYS_PER_YEAR,
                2.3041730e-05 * DAYS_PER_YEAR],
               2.8588598e-04 * SOLAR_MASS),

    'uranus': ([12.8943696, -15.1111514, -0.2233076],
               [2.9646014e-03 * DAYS_PER_YEAR,
                2.3784717e-03 * DAYS_PER_YEAR,
                -2.9658957e-05 * DAYS_PER_YEAR],
               4.3662440e-05 * SOLAR_MASS),

    'neptune': ([15.3796971, -25.9193146, 0.1792588],
                [2.6806777e-03 * DAYS_PER_YEAR,
                 1.6282417e-03 * DAYS_PER_YEAR,
                 -9.5159225e-05 * DAYS_PER_YEAR],
                5.1513890e-05 * SOLAR_MASS) }


SYSTEM = list(BODIES.values())
PAIRS = combinations(SYSTEM)


def advance(dt, n, bodies=SYSTEM, pairs=PAIRS):

    for i in range(n):
        for (([x1, y1, z1], v1, m1),
            ([x2, y2, z2], v2, m2)) in pairs:
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            mag = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
            b1m = m1 * mag
            b2m = m2 * mag
            v1[0] -= dx * b2m
            v1[1] -= dy * b2m
            v1[2] -= dz * b2m
            v2[0] += dx * b1m
            v2[1] += dy * b1m
            v2[2] += dz * b1m
        for (r, [vx, vy, vz], m) in bodies:
            r[0] += dt * vx
            r[1] += dt * vy
            r[2] += dt * vz


def report_energy(bodies=SYSTEM, pairs=PAIRS, e=0.0):

    for (((x1, y1, z1), v1, m1),
        ((x2, y2, z2), v2, m2)) in pairs:
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
    for (r, [vx, vy, vz], m) in bodies:
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
    print("%.9f" % e)

def offset_momentum(ref, bodies=SYSTEM, px=0.0, py=0.0, pz=0.0):

    for (r, [vx, vy, vz], m) in bodies:
        px -= vx * m
        py -= vy * m
        pz -= vz * m
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m

def main(n, ref='sun'):
    offset_momentum(BODIES[ref])
    report_energy()
    advance(0.01, n)
    report_energy()

if __name__ == '__main__':
    main(int(config.C1_ARG[0]))
"""Benchmarks for Python's regex engine.

These are some of the original benchmarks used to tune Python's regex engine
in 2000 written by Fredrik Lundh. Retreived from
http://mail.python.org/pipermail/python-dev/2000-August/007797.html and
integrated into Unladen Swallow's pyperf.py in 2009 by David Laing.

These benchmarks are of interest since they helped to guide the original
optimization of the sre engine, and we shouldn't necessarily ignore them just
because they're "old".
"""

# Python imports
import re
import time

USE_BYTES = False


def re_compile(s):
    if USE_BYTES:
        return re.compile(s.encode('latin1'))
    else:
        return re.compile(s)


def gen_regex_table():
    return [
        re_compile('Python|Perl'),
        re_compile('Python|Perl'),
        re_compile('(Python|Perl)'),
        re_compile('(?:Python|Perl)'),
        re_compile('Python'),
        re_compile('Python'),
        re_compile('.*Python'),
        re_compile('.*Python.*'),
        re_compile('.*(Python)'),
        re_compile('.*(?:Python)'),
        re_compile('Python|Perl|Tcl'),
        re_compile('Python|Perl|Tcl'),
        re_compile('(Python|Perl|Tcl)'),
        re_compile('(?:Python|Perl|Tcl)'),
        re_compile('(Python)\\1'),
        re_compile('(Python)\\1'),
        re_compile('([0a-z][a-z0-9]*,)+'),
        re_compile('(?:[0a-z][a-z0-9]*,)+'),
        re_compile('([a-z][a-z0-9]*,)+'),
        re_compile('(?:[a-z][a-z0-9]*,)+'),
        re_compile('.*P.*y.*t.*h.*o.*n.*')]


def gen_string_table(n):
    strings = []

    def append(s):
        if USE_BYTES:
            strings.append(s.encode('latin1'))
        else:
            strings.append(s)
    append('-' * n + 'Perl' + '-' * n)
    append('P' * n + 'Perl' + 'P' * n)
    append('-' * n + 'Perl' + '-' * n)
    append('-' * n + 'Perl' + '-' * n)
    append('-' * n + 'Python' + '-' * n)
    append('P' * n + 'Python' + 'P' * n)
    append('-' * n + 'Python' + '-' * n)
    append('-' * n + 'Python' + '-' * n)
    append('-' * n + 'Python' + '-' * n)
    append('-' * n + 'Python' + '-' * n)
    append('-' * n + 'Perl' + '-' * n)
    append('P' * n + 'Perl' + 'P' * n)
    append('-' * n + 'Perl' + '-' * n)
    append('-' * n + 'Perl' + '-' * n)
    append('-' * n + 'PythonPython' + '-' * n)
    append('P' * n + 'PythonPython' + 'P' * n)
    append('-' * n + 'a5,b7,c9,' + '-' * n)
    append('-' * n + 'a5,b7,c9,' + '-' * n)
    append('-' * n + 'a5,b7,c9,' + '-' * n)
    append('-' * n + 'a5,b7,c9,' + '-' * n)
    append('-' * n + 'Python' + '-' * n)
    return strings


def init_benchmarks(n_values=None):
    if n_values is None:
        n_values = (0, 5, 50, 250, 1000, 5000, 10000)

    string_tables = {n: gen_string_table(n) for n in n_values}
    regexs = gen_regex_table()

    data = []
    for n in n_values:
        for id in range(len(regexs)):
            regex = regexs[id]
            string = string_tables[n][id]
            data.append((regex, string))
    return data


def bench_regex_effbot(loops):
    if bench_regex_effbot.data is None:
        bench_regex_effbot.data = init_benchmarks()
    data = bench_regex_effbot.data

    range_it = range(loops)
    search = re.search
    t0 = time.perf_counter()

    for _ in range_it:
        for regex, string in data:
            # search 10 times
            search(regex, string)
            search(regex, string)
            search(regex, string)
            search(regex, string)
            search(regex, string)
            search(regex, string)
            search(regex, string)
            search(regex, string)
            search(regex, string)
            search(regex, string)

    return time.perf_counter() - t0


bench_regex_effbot.data = None


if __name__ == '__main__':
    # Simple execution without pyperf
    USE_BYTES = False  # change to True to test with bytes
    elapsed = bench_regex_effbot(loops=500)
    print(f"Benchmark completed in {elapsed:.6f} seconds (5 loops × 10 inner searches)")

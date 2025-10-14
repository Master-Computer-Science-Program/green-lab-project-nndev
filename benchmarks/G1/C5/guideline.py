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
import sys, os

USE_BYTES = False


def re_compile(s):
    if USE_BYTES:
        return re.compile(s.encode('latin1'))
    else:
        return re.compile(s)


def gen_regex_table():
    python_perl = 'Python|Perl'          # before: repeated inline
    python = 'Python'                    # before: repeated inline
    python_perl_tcl = 'Python|Perl|Tcl'  # before: repeated inline
    python_backref = '(Python)\\1'       # before: repeated inline
    expr1 = '([0a-z][a-z0-9]*,)+'        # before: repeated inline
    expr2 = '(?:[0a-z][a-z0-9]*,)+'      # before: repeated inline
    expr3 = '([a-z][a-z0-9]*,)+'         # before: repeated inline
    expr4 = '(?:[a-z][a-z0-9]*,)+'       # before: repeated inline

    return [
        re_compile(python_perl),
        re_compile(python_perl),      # was: re_compile('Python|Perl')
        re_compile('(Python|Perl)'),
        re_compile('(?:Python|Perl)'),
        re_compile(python),           # was: re_compile('Python')
        re_compile(python),
        re_compile('.*Python'),
        re_compile('.*Python.*'),
        re_compile('.*(Python)'),
        re_compile('.*(?:Python)'),
        re_compile(python_perl_tcl),
        re_compile(python_perl_tcl),  # was: re_compile('Python|Perl|Tcl')
        re_compile('(Python|Perl|Tcl)'),
        re_compile('(?:Python|Perl|Tcl)'),
        re_compile(python_backref),
        re_compile(python_backref),   # was: re_compile('(Python)\\1')
        re_compile(expr1),
        re_compile(expr2),
        re_compile(expr3),
        re_compile(expr4),
        re_compile('.*P.*y.*t.*h.*o.*n.*')]


def gen_string_table(n):
    strings = []

    def append(s):
        if USE_BYTES:
            strings.append(s.encode('latin1'))
        else:
            strings.append(s)

    suffix = '-' * n   # before: repeated '-' * n
    prefixP = 'P' * n  # before: repeated 'P' * n
    perl = 'Perl'
    python = 'Python'
    pythonpython = 'PythonPython'
    a5b7c9 = 'a5,b7,c9,'

    append(suffix + perl + suffix)         # was: '-' * n + 'Perl' + '-' * n
    append(prefixP + perl + prefixP)       # was: 'P' * n + 'Perl' + 'P' * n
    append(suffix + perl + suffix)
    append(suffix + perl + suffix)
    append(suffix + python + suffix)       # was: '-' * n + 'Python' + '-' * n
    append(prefixP + python + prefixP)
    append(suffix + python + suffix)
    append(suffix + python + suffix)
    append(suffix + python + suffix)
    append(suffix + python + suffix)
    append(suffix + perl + suffix)
    append(prefixP + perl + prefixP)
    append(suffix + perl + suffix)
    append(suffix + perl + suffix)
    append(suffix + pythonpython + suffix)   # was: '-' * n + 'PythonPython' + '-' * n
    append(prefixP + pythonpython + prefixP)
    append(suffix + a5b7c9 + suffix)         # was: '-' * n + 'a5,b7,c9,' + '-' * n
    append(suffix + a5b7c9 + suffix)
    append(suffix + a5b7c9 + suffix)
    append(suffix + a5b7c9 + suffix)
    append(suffix + python + suffix)
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
            for _ in range(10):        # before: repeated 10 times manually
                search(regex, string)

    return time.perf_counter() - t0


bench_regex_effbot.data = None


if __name__ == '__main__':
    # Simple execution without pyperf
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from config import C5_ARG
    USE_BYTES = False  # change to True to test with bytes
    elapsed = bench_regex_effbot(C5_ARG[0])

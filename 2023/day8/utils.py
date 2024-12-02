from time import perf_counter_ns
from functools import wraps


def timeit(func):

    @wraps(func)
    def decorator(*args, **kwargs):
        start = perf_counter_ns()
        func(*args, **kwargs)
        end = perf_counter_ns()
        ms = (end - start) / 1000 / 1000
        print(f'{ms:.1f} ms')

    return decorator

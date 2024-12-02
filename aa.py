from __future__ import annotations


def f(n, s):
    return f'{n} {s}' + ('s' if n > 1 else '')


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    l = {
        'year': seconds // 31536000,
        'day': seconds // 86400 % 365,
        'hour': seconds // 3600 % 24,
        'minute': seconds // 60 % 60,
        'second': seconds % 60,
    }
    l = [f(v, k) for k, v in l.items() if v]
    if len(l) == 1:
        return l[0]
    k = ' and '.join([', '.join(l[:-1]), l[-1]])
    return k

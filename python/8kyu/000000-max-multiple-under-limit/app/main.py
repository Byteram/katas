#!/usr/bin/env python


def max_multiple(divisor, limit) -> int:
    return 0 if divisor > limit else limit - (limit % divisor)


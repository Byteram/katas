#!/usr/bin/env python

def sum_even_digits(n: int) -> int:
    return sum([int(x) for x in str(n) if not int(x) % 2])


print(sum_even_digits(1234))

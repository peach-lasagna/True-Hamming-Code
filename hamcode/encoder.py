from math import ceil, log2


count_k = lambda m: ceil(log2(log2(m + 1) + m + 1))


def encode(string: str, m: int):
    k = count_k(m)


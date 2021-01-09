from .encoder import count_k
from typing import Union


def array_count_xor(array: list[int], kbit_num: int):
    n = 0
    for i in range(2**(kbit_num - 1), len(array) + 1, 2**kbit_num):
        for j in array[i - 1:i - 1 + 2**(kbit_num - 1)]:
            n ^= j
    return n

def decode_block(array: list[int], k: int):
    n = 1
    bit_err_ind = -1
    n_mas =[]

    for i in range(1, k+1):
        bit_err_ind += (n-1) * (array_count_xor(array, i) == array[n-1])
        n_mas.append(n)
        n *= 2

    if bit_err_ind != -1:
        bit_err_ind +=1
        array[bit_err_ind] ^= 1
    n = -1

    for key in n_mas:
        n+=1
        del array[key-1-n]
    return array, bit_err_ind if bit_err_ind != -1 else None


def decode(string: str, block_len: int, return_bit_errors: bool= False) -> Union[tuple[str, list[int]], str]:
    """
    In Ham-Code (12,8) block_len == 8
    """
    array = list(map(int, list(string)))
    k = count_k(block_len)
    block_len += k
    err_bits = []
    res = ''

    n = -1
    for ind in range(block_len, len(array)+1, block_len):
        n+=1
        el, err_bit = decode_block(array[ind-block_len:ind], k)

        if return_bit_errors and err_bit is not None:
            err_bits.append(err_bit*(n+1))
        res+= ''.join(str(e) for e in el)

    if return_bit_errors:
        return res, err_bits
    return res



from .encoder import count_k
from typing import Union


def array_count_xor(array: list[int], kbit_num: int):
    n = 0
    for i in range(kbit_num, len(array), kbit_num*2):
        for j in array[i:i+kbit_num]:
            n ^= j
    return n


def decode_block(array: list[int], k: int):
    dct = {}
    n = 1

    for i in range(1, k+1):
        dct.update({n: array_count_xor(array, i)})
        n *= 2

    bit_err_ind = -1

    for key, v in dct.items():
        bit_err_ind += (key-1) * (v == array[key-1])

    if bit_err_ind != -1:
        bit_err_ind +=1
        array[bit_err_ind] ^= 1
    n = -1
    for key in dct.keys():
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
    chunks = [array[i - block_len:i] for i in range(block_len, len(array)+1, block_len)]
    err_bits = []
    res = ''
    for ind in range(len(chunks)):
        el, err_bit = decode_block(chunks[ind], k)
        if return_bit_errors and err_bit is not None:
            err_bits.append(err_bit*(ind+1))
        res+= ''.join(str(e) for e in el)
    if return_bit_errors:
        return res, err_bits
    return res


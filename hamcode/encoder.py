from .decoder import count_k, array_count_xor


def encode_block(array: list[int], k: int):
    kbit_mas = []
    for i in range(1, k+1):
        b = 2**i//2
        array.insert(b-1,0)
        kbit_mas.append(b)

    for kbit in kbit_mas:
        array[kbit-1] = array_count_xor(array, kbit)
    return array

def encode(string: str, block_len: int) -> str:
    """
    In Ham-Code (12,8) block_len == 8
    """
    res = ''
    k = count_k(block_len)
    array = list(map(int, string))

    for ind in range(block_len, len(array)+1, block_len):
        el = encode_block(array[ind-block_len:ind], k)
        res += ''.join(str(e) for e in el)

    return res


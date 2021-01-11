from hamcode.decoder import  array_count_xor, decode_block
import pytest


@pytest.mark.parametrize("array, kbit_num, ans", [
    ([1, 0, 0, 1, 1, 0], 2, 0),
    ([1, 1, 1, 1, 1], 1, 0),
    ([1, 1, 0, 1], 1, 0),
    ([1, 0, 0, 1, 1, 0], 2, 0),
    ([0,1,1], 2, 1),
    ([0,1,1], 1, 1),
    ([1, 1, 1], 1, 1)
])
def test_xor_count(array, kbit_num, ans):
    assert array_count_xor(array, kbit_num) == ans

@pytest.mark.parametrize("array, k, ans", [
    ([1,1,1], 2, [1,]),
    ([1,1,1,0,0], 3, [1,0]),
])
def test_decode_block_without_errors(array, k, ans):
    assert decode_block(array, k) == (ans, None)

@pytest.mark.parametrize("array, k, ans", [
    ([1,0,1], 2, [1,]),
    ([0,1,1], 2, [1,]),
    ([1,1,1,0,1], 3, [1,0]),
    ([1,1,1,1,0], 3, [1,0]),
    ([0,1,1,0,0], 3, [1,0]),
    ([1,0,1,0,0], 3, [1,0]),
])
def test_decode_block_with_1_error(array, k, ans):
    assert decode_block(array, k) == (ans, 1)

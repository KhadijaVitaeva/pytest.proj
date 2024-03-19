from utils import arrs
from utils import dickt



def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], None, 3) == [1, 2, 3]


def dic():
    return {1: 'one', 2: 'two', 3: 'three'}


def test_get_val(dic):
    assert dickt.get_val(dic, 2, 'git') == 'two'
    assert dickt.get_val(dic, 4, 'git') == 'git'
    assert dickt.get_val(dic, 4, 'another') == 'another'
    assert dickt.get_val(dic, 2, None) == 'two'

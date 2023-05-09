import pytest

from utils import arrs


@pytest.fixture
def collection_get():
    return [[[1, 2, 3], 1, "test"], [[], 0, "test"]]


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == [2, "test"]
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -7) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([], 1) == []

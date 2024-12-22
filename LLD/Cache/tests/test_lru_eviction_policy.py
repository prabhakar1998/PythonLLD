import pytest
from .fixtures import cache, size

def test_remove(cache):
    cache.add("Key1", "val1")
    cache.add("Key2", "val2")
    cache.add("Key3", "val3")
    cache.add("Key4", "val4")

    with pytest.raises(ValueError):
        cache.get("Key1")

    assert cache.get("Key2") == "val2"
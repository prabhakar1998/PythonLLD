import pytest
from .fixtures import cache, size

def test_add(cache):
    cache.add("Key1", "val1")
    cache.add("Key2", "val2")
    assert cache.get("Key2") == "val2"

def test_remove(cache):
    cache.add("Key1", "val1")
    cache.add("Key2", "val2")
    cache.add("Key3", "val3")
    cache.add("Key4", "val4")
    cache.add("Key5", "val5")

    with pytest.raises(ValueError):
        cache.get("Key1")

    cache.add("Key2", "val2_updated")

    with pytest.raises(ValueError):
        cache.get("Key3")
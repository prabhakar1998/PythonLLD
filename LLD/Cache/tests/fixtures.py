from pytest import fixture

from ..linked_list.doubly_linked_list import DoublyLinkedList
from ..cache import Cache
from ..policies.lru_eviction_strategy import LRUEvictionStrategy
from ..store.hash_map_store import HashMapStore

@fixture
def size():
    return 3

@fixture
def cache(size):
    cache_size = size
    eviction_policy_strategy = LRUEvictionStrategy(cache_size)
    store = HashMapStore(cache_size)
    cache = Cache(eviction_policy_strategy, store)
    return cache

@fixture
def dll():
    dll = DoublyLinkedList()
    return dll
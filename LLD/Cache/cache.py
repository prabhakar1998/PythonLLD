from .policies.eviction_policy import EvictionPolicyStrategy
from .store.store import Store

class Cache:
    def __init__(self, eviction_policy: EvictionPolicyStrategy, store: Store):
        self.eviction_policy = eviction_policy
        self.store = store

    def add(self, key, val):
        self.eviction_policy.key_accessed(key)
        self.store.add(key, val)
        
        if self.store.is_full():
            evict_key = self.eviction_policy.get_evicted_key()
            self.store.remove(evict_key)

    def get(self, key):
        val= self.store.get(key)
        self.eviction_policy.key_accessed(key)
        return val
    
    
from ..linked_list.doubly_linked_list import DoublyLinkedList
from .eviction_policy import EvictionPolicyStrategy

class LRUEvictionStrategy(EvictionPolicyStrategy):
    # most recest key will be at the tail
    # oldest key will be at the head

    def __init__(self, cache_size):
        super().__init__(cache_size)
        self._dll = DoublyLinkedList()
        self.key_node_map = {} # key:node

    def key_accessed(self, key: str) -> None:
        if key in self.key_node_map:
            self._dll.delete_node(self.key_node_map[key])
        new_node = self._dll.add_key(key)
        self.key_node_map[key] = new_node

    def get_evicted_key(self) -> str:
        delete_key = self._dll.delete_head()
        return delete_key

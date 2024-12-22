from .doubly_linked_list_node import DoublyLinkedListNode


class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def delete_head(self) -> str:
        if self.head is None:
            return ""
        delete_node = self.head
        delete_key = delete_node.key
        next_node = self.head.next
        if next_node is not None:
            next_node.prev = None
        self.head = next_node
        del delete_node
        return delete_key

    def add_key(self, key: str) -> DoublyLinkedListNode:
        node = DoublyLinkedListNode(key, None, self.tail)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        return node
    
    
    def delete_node(self, node: DoublyLinkedListNode):
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        if node == self.head:
            self.head = next_node
        if node == self.tail:
            self.tail = prev_node
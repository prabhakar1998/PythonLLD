from ..linked_list.doubly_linked_list import DoublyLinkedList

def test_dll_insert_last():
    dll = DoublyLinkedList()
    new_node = dll.add_key("Key1")
    assert dll.tail == new_node


def test_single_node_dll__delete():
    dll = DoublyLinkedList()
    new_node = dll.add_key("Key1")
    assert dll.head == dll.tail
    assert dll.head == new_node

    dll.delete_node(new_node)

    assert dll.head == dll.tail
    assert dll.head == None


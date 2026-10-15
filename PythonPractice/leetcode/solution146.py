class DoublyLinkedElement:
    def __init__(self, key=None, value=None, next_node=None, previous_node=None):
        self.key: int = key
        self.value: int = value
        self.next_node: DoublyLinkedElement = next_node
        self.previous_node: DoublyLinkedElement = previous_node

    def __repr__(self):
        return f"Key: {self.key}, Value: {self.value}"


class DoublyLinkedList:
    def __init__(self):
        self._dummy_front = DoublyLinkedElement()
        self._dummy_end = DoublyLinkedElement()
        self._dummy_front.next_node = self._dummy_end
        self._dummy_end.previous_node = self._dummy_front

    def get_first(self):
        first_element = self._dummy_front.next_node
        if first_element is self._dummy_end:
            return None
        return self._dummy_front.next_node

    def get_last(self):
        last_element = self._dummy_end.previous_node
        if last_element is self._dummy_front:
            return None
        return self._dummy_front.next_node

    def push_front(self, key, value):
        element = DoublyLinkedElement(key, value)
        self.insert_at_front(element)

    def insert_at_front(self, element: DoublyLinkedElement):
        element.next_node = self._dummy_front.next_node
        self._dummy_front.next_node.previous_node = element
        element.previous_node = self._dummy_front
        self._dummy_front.next_node = element

    def move_to_front(self, element):
        self.remove_element(element)
        self.insert_at_front(element)

    def remove_last_element(self):
        last_element = self._dummy_end.previous_node
        if last_element is not self._dummy_front:
            self.remove_element(last_element)

    @staticmethod
    def remove_element(element: DoublyLinkedElement):
        element.previous_node.next_node = element.next_node
        element.next_node.previous_node = element.previous_node


class LRUCache:
    MISSING_KEY_VALUE = -1

    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self.doubly_linked_list = DoublyLinkedList()
        self._key_to_element = dict()

    def get(self, key: int) -> int:
        if key in self._key_to_element:
            element = self._key_to_element[key]
            self.doubly_linked_list.move_to_front(element)
            return element.value
        return self.MISSING_KEY_VALUE

    def put(self, key: int, value: int) -> None:
        if key in self._key_to_element:
            self._put_existing_key(key, value)
        else:
            self._put_new_key(key, value)

    def _put_existing_key(self, key: int, value: int):
        element = self._key_to_element[key]
        element.value = value
        self.doubly_linked_list.move_to_front(element)

    def _put_new_key(self, key: int, value: int):
        if self._size == self._capacity:
            self._remove_least_recently_used()
        else:
            self._size += 1
        self._insert_new_value(key, value)

    def _remove_least_recently_used(self):
        last_element = self.doubly_linked_list.get_last()
        key = last_element.key
        self._key_to_element.pop(key)

    def _insert_new_value(self, key, value: int):
        self.doubly_linked_list.push_front(key, value)
        element = self.doubly_linked_list.get_first()
        self._key_to_element[key] = element

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def __str__(self):
        return f'{self.value}'


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def set_head_and_tail(self, new_value):
        self.head, self.tail = new_value, new_value

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        node = ListNode(value)
        if self.head is None and self.tail is None:
            self.set_head_and_tail(node)
        else:
            prev_head = self.head
            prev_head.insert_before(value)
            self.head = prev_head.prev
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        removed_node = self.head.value
        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next

        self.length -= 1
        return removed_node

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        node = ListNode(value)

        if self.head is None and self.tail is None:
            self.set_head_and_tail(node)

        else:
            prev_tail = self.tail
            prev_tail.insert_after(value)
            self.tail = prev_tail.next
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        removed_node = self.tail.value
        if self.head is self.tail:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev

        self.length -= 1
        return removed_node

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return None
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return None
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        if not self.head:
            return None
        if len(self) is 0:
            return None
        sorted_ll = sorted([i.value for i in self])
        return sorted_ll[-1]

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

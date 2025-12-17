class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def to_set(self):
        values = set()
        node = self.head
        while node:
            values.add(node.value)
            node = node.next
        return values


def union(llist_1, llist_2):
    result = LinkedList()
    for val in llist_1.to_set().union(llist_2.to_set()):
        result.append(val)
    return result


def intersection(llist_1, llist_2):
    result = LinkedList()
    for val in llist_1.to_set().intersection(llist_2.to_set()):
        result.append(val)
    return result


if __name__ == "__main__":
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    for i in [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]:
        linked_list_1.append(i)
    for i in [6, 32, 4, 9, 6, 1, 11, 21, 1]:
        linked_list_2.append(i)
    print(union(linked_list_1, linked_list_2))  # unordered union
    print(intersection(linked_list_1, linked_list_2))  # 6 -> 4 -> 21 ->

    # Edge: one empty list
    empty = LinkedList()
    print(union(empty, linked_list_1))  # same as linked_list_1 unique
    print(intersection(empty, linked_list_1))  # empty

    # Edge: both empty
    print(union(empty, empty))  # empty

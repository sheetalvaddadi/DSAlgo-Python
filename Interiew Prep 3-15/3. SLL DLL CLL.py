class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        cur_node = self.head
        while(cur_node.next is not None):
            cur_node = cur_node.next
        cur_node.next = new_node
        return

    def reverse(self):
        prev_node = None
        cur_node = self.head
        while(cur_node.next is not None):
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            return



class CLL:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        cur_node = self.head
        while (cur_node.next is not self.head):
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.next = self.head
        return

    def reverse(self):
        prev_node = None
        cur_node = self.head
        while (cur_node.next is not None):
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        cur_node.next = self.head
        return


class DLL_Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = DLL_Node()
        if self.head is None:
            self.head = new_node
        cur_node = self.head
        while (cur_node.next is not None):
            cur_node = cur_node.next

        cur_node.next = new_node
        new_node.prev = cur_node
        new_node.next = None
        return





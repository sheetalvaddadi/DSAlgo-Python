class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__ (self):
        self.head = None

    def add_to_start(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
            new_node.prev = None
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        new_node.prev = None
        return

    def add_to_end(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
            new_node.prev = None
            return
        cur_node = self.head
        while (cur_node.next is not None):
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev = cur_node
        new_node.next = None
        return

    def len_list(self):
        count = 0
        cur_node = self.head
        while(cur_node is not None):
            cur_node = cur_node.next
            count+=1
        return count

    def reverse_linked_list(self):
        prev = None
        cur_node = self.head
        while(cur_node is not None):
            prev = cur_node.prev
            cur_node.prev = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = cur_node.prev
        if (prev is not None):
            self.head = prev
        return

    def list_length(self):
        count = 0
        cur_node = self.head
        while(cur_node is not None):
            count+=1
        return count

    def print_linkedlist(self):
        cur_node = self.head
        result_str = ""
        while (cur_node is not None):
            result_str+= str(cur_node.data)+ "-->"
            cur_node = cur_node.next
        print(result_str)
        return

if __name__ == "__main__":
    ll1 = DoublyLinkedList()
    ll1.add_to_start(2)
    ll1.add_to_start(4)
    ll1.add_to_start(7)
    ll1.add_to_end(8)
    ll1.print_linkedlist()
    ll1.reverse_linked_list()
    ll1.print_linkedlist()
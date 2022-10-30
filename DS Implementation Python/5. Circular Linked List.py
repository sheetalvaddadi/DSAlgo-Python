class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__ (self):
        self.head = None

    def add_to_start(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        return

    def add_to_end(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
            return
        cur_node = self.head
        while (cur_node.next is not None):
            cur_node = cur_node.next
        cur_node.next = new_node
        return

    def len_list(self):
        count = 0
        cur_node = self.head
        while(cur_node is not None):
            cur_node = cur_node.next
            count+=1
            if(cur_node is self.head):
                break
        return count

    def reverse_linked_list(self):
        prev_node = None
        cur_node = self.head
        while(cur_node is not None):
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node
        return

    def print_linkedlist(self):
        cur_node = self.head
        result_str = ""
        while (cur_node is not None):
            result_str+= str(cur_node.data)+ "-->"
            cur_node = cur_node.next
        print(result_str)
        return

if __name__ == "__main__":
    ll1 = CircularLinkedList()
    ll1.add_to_start(2)
    ll1.add_to_start(4)
    ll1.add_to_start(7)
    ll1.add_to_end(8)
    print(ll1.len_list())
    ll1.print_linkedlist()
    ll1.reverse_linked_list()
    ll1.print_linkedlist()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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
        return count

    def add_at_position(self, data, position):
        new_node = Node(data)
        if (position==0):
            new_node.next = self.head
            self.head = new_node
            return
        if(position < 0 or position > self.len_list()):
                print("Invalid Index to add element here")
                return
        cur_node = self.head
        while (cur_node is not None and position > 1):
            cur_node = cur_node.next
            position -= 1
        new_node.next = cur_node.next
        cur_node.next = new_node
        return

    def remove_from_position(self, position):
        if (self.head is None):
            print("LinkedList empty , nothing to remove")
            return
        if (position < 0 or position > self.len_list()):
            print("Invalid position to remove element from here")
            return
        if (position == 0):
            self.head= self.head.next
            return
        cur_node = self.head
        while (cur_node.next is not None and position > 1):
            cur_node = cur_node.next
            position -= 1
        cur_node.next = cur_node.next.next
        return

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
    ll1 = LinkedList()

    ll1.print_linkedlist()
    ll1.print_linkedlist()
    ll1.add_at_position(8,0)
    ll1.add_at_position(6,0)
    ll1.add_at_position(7,2)
    ll1.print_linkedlist()
    ll1.reverse_linked_list()
    ll1.print_linkedlist()
class Stack:
    #Do not forget to handle stack overflow and underflow conditions by checking size of stack

    def __init__ (self):
        self.stack =[]
    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        if(len(self.stack) == 0):
            return True
        return False

    def pop(self):
        if (self.is_empty() is False):
            self.stack.pop()
            return
        print('stack is empty')
        return

    def peek(self):
        return self.stack[-1]

    def push_items(self, items):
        for item in items:
            self.stack.append(item)

    def print_stack(self):
        print(self.stack)

if __name__ == "__main__":
    s1 = Stack()
    s1.push_items([1,2,3])
    s1.print_stack()
    s1.pop()
    s1.pop()
    s1.pop()
    s1.pop()
    s1.print_stack()



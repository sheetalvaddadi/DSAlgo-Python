class queue:
    def __init__(self):
        self.queue=[]
    def add(self, data):
        self.stack.append(data)
    def is_empty(self):
        if(len(self.stack) ==0):
            return True
        return False
    def remove(self):
        if(self.is_empty() is False):
            self.stack.pop(0)

if __name__ =="__main__":
    c1 = queue()
    print(c1.remove())
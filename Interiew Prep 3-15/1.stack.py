class stack:
    def __init__(self):
        self.stack=[]
    def add(self, data):
        self.stack.append(data)
    def is_empty(self):
        if(len(self.stack) ==0):
            return True
        return False
    def remove(self):
        if(self.is_empty() is False):
            self.stack.pop()

if __name__ =="__main__":
    c1 = stack()
    print(c1.remove())



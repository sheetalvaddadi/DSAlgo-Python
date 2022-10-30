class Queue:
    #Do not forget to handle queue overflow and underflow conditions by checking size of queue
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def is_empty(self):
        if (len(self.queue) ==0):
            return True
        return False

    def dequeue (self):
        if(self.is_empty() is False):
            self.queue.pop(0)
            return
        print('Queue is empty')

    def print_queue(self):
        print (self.queue)

if __name__ =="__main__":
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.print_queue()
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.print_queue()
class fibo:
    def fib(self, n):
        if(n<2):
            return n
        return self.fib(n-2)+self.fib(n-1)
if __name__ =="__main__":
    f=fibo()
    print(f.fib(10))
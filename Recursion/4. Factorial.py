class Factorial:

    def fact (self, n):
        if(n==1):
            return n
        return n *self.fact(n-1)

if __name__ =="__main__":
    f1 = Factorial()
    print(f1.fact(6))
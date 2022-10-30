#prints nums upto n and also in order of n below
class Nums:
    def printnums (self, n):
        if(n==0):
            return
        print(n)
        self.printnums(n-1)
        print(n)
if __name__ =="__main__":
    n1=Nums()
    n1.printnums(10)
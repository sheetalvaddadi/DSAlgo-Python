class Sum:

    def sum_of_n(self, n):
        if(n==1):
            return n
        return n+self.sum_of_n(n-1)

if __name__ =="__main__":
    s1 = Sum()
    print(s1.sum_of_n(5))
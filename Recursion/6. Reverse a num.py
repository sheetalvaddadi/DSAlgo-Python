class Reversal:
    sum =0
    def reverse(self, num):
        if(num==0):
            return
        rem = num%10
        sum= sum*10+rem
        self.reverse(num//10)
        print(num)


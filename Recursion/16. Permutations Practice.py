class Permutations:
    def perm(self, p,unp,result):
        if (len(unp) ==0):
            result.append(p)
            return
        ch = unp[0]
        for i in range(len(p)+1):
            start = p[:i]
            end =p[i:]
            self.perm(start+ch+end, unp[1:],result)
        return result
p = Permutations()
print(p.perm("","abcde",[]))
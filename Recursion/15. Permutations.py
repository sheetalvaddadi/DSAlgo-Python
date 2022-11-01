class Permutations:
    def perm(self, p, unp, result):
        if (len(unp) ==0):
            result.append(p)
            return
        ch = unp[0]
        for i in range(len(p)+1):
            first = p[:i]
            second = p[i:]
            self.perm(first+ch+second, unp[1:], result)

        return result


if __name__ =="__main__":
    p = Permutations()
    print(p.perm('','abc',[]))
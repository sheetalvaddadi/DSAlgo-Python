class SubsetwithArray:
    def createsubset(self, p, unp, result=[]):
        if(len(unp)==0):
            result.append(list(p))
            return
        start = unp[0]
        #add to list
        self.createsubset(p+str(start), unp[1:], result)
        #dont add to list
        self.createsubset(p, unp[1:], result)

        return result

if __name__ =="__main__":
    s= SubsetwithArray()
    print(s.createsubset("",[1,2,3],[]))
class Subsets:
    def create_subsets(self, p, unp, result =[]):
        if(unp ==""):
            result.append(p)
            return
        ch = unp[0]
        #Add the char
        self.create_subsets(p+ch, unp[1:], result)
        #Dont add the char
        self.create_subsets(p, unp[1:], result)
        return result

if __name__ =="__main__":
    s = Subsets()
    print(s.create_subsets("","abc",[]))
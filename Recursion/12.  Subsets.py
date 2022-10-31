class Subsets:

    def createsubsets(self, processed, unprocessed, result =[]):

        if (unprocessed ==""):
            result.append(processed)
            return

        ch = unprocessed[0]
        # Take char
        self.createsubsets(processed+ch, unprocessed[1:], result)
        # dont take char
        self.createsubsets(processed, unprocessed[1:], result)
        return result
if __name__ =="__main__":
    s1 = Subsets()
    print(s1.createsubsets("", "abc"))


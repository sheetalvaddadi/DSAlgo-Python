class Trie:
    def __init__ (self):
        self.root = {"*":"*"}

    def add_word (self, word):
        curr_node = self.root
        for char in word:
            if (char not in curr_node):
                curr_node[char]= {}
            curr_node = curr_node[char]
        curr_node["*"] = "*"

    def word_exists (self, word):
        cur_node = self.root
        for char in word:
            if (char not in cur_node):
                return False
            cur_node = cur_node[char]
        return "*" in cur_node

    def startsWith(self, prefix):
        cur_node = self.root
        for char in prefix:
            if char not in cur_node:
                return False
            cur_node = cur_node[char]
        return True

    def startsWithReturnWord(self, prefix):
        cur_node = self.root
        str =""
        for char in prefix:
            cur_node = cur_node[char]
        return cur_node


if __name__ == "__main__":
    t1 = Trie()
    words =["wait", "waiter", "shop", "shopper"]
    for word in words:
        t1.add_word(word)

    print(t1.word_exists("wait"))
    print(t1.startsWithReturnWord("wa"))
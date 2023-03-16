class Trie:
    def __init__(self):
        self.root ={"*":"*"}

    def add_word(self, word):
        cur_node = self.root
        for char in word:
            if (char not in cur_node):
                cur_node[char]={}
            cur_node = cur_node[char]
        cur_node["*"] = "*"

    def word_exists(self, word):
        cur_node = self.root
        for char in word:
            if (char not in cur_node):
                return False
            cur_node= cur_node[char]
        return True

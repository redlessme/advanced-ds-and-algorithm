class TrieNode():
    def __init__(self):
        self.children={}

class Trie():
    def __init__(self):
        self.root=TrieNode()

    def add(self,word):
        for i in range(len(word)):
            cur=self.root
            for c in word[i:]:
                if c not in cur.children:
                    child=TrieNode()
                    cur.children[c]=child
                    cur=child
                else:
                    cur=cur.children[c]
            cur.children['$']=True

    def search(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                return False
            cur=cur.children[char]
        if '$' in cur.children:
            return True
        else:
            return False

if __name__ == '__main__':
    s_trie = Trie()
    s_trie.add("apple")
    s_trie.add("add")
    s_trie.add("appx")
    s_trie.add("gpple")
    print(s_trie.search("aplle"))
    print(s_trie.search("ap"))
    print(s_trie.search("a"))
    print(s_trie.search("addx"))
    print(s_trie.search("apple"))
    print(s_trie.search("add"))






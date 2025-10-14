class Trie:
    def __init__(self):
        self.children = dict()
        self.end = False

    def insert(self, word):
        root = self
        for w in word:
            if w not in root.children:
                root.children[w] = Trie()
            root = root.children[w]
        root.end = True

    def query(self, word):
        i = 0
        root = self
        while i < len(word):
            w = word[i]
            if w not in root.children:
                return ""
            root = root.children[w]
            if root.end:
                return word[:i + 1]
            i += 1
        if root.end:
            return word
        return ""
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        sens = sentence.split(' ')
        for i, sen in enumerate(sens):
            res = trie.query(sen)
            if res != "":
                sens[i] = res
        return " ".join(sens)
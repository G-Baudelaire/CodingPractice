class TreeNode:
    def __init__(self):
        self.paths = dict()
        self.word_end = False


class Trie:

    def __init__(self):
        self.dummy_node = TreeNode()

    def insert(self, word: str) -> None:
        head = self.dummy_node
        for char in word:
            if char not in head.paths:
                head.paths[char] = TreeNode()
            head = head.paths[char]
            head.word_end = True

    def search(self, word: str) -> bool:
        head = self.dummy_node
        for char in word:
            if char not in head.paths:
                return False
            head = head.paths[char]
        return head.word_end

    def startsWith(self, prefix: str) -> bool:
        head = self.dummy_node
        for char in prefix:
            if char not in head.paths:
                return False
            head = head.paths[char]
        return True

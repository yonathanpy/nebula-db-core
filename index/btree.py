from index.node import BTreeNode


class BTreeIndex:

    def __init__(self):

        self.root = BTreeNode()

    def insert(self, key, value):

        self.root.insert(key, value)

    def search(self, key):

        return self.root.search(key)

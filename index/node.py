class BTreeNode:

    def __init__(self):

        self.keys = []

        self.values = []

    def insert(self, key, value):

        self.keys.append(key)

        self.values.append(value)

    def search(self, key):

        for i, k in enumerate(self.keys):

            if k == key:

                return self.values[i]

        return None

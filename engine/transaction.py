class TransactionManager:

    def __init__(self):

        self.active = []

    def begin(self):

        tx = {}

        self.active.append(tx)

        return tx

    def commit(self, tx):

        if tx in self.active:

            self.active.remove(tx)

    def rollback(self, tx):

        if tx in self.active:

            self.active.remove(tx)

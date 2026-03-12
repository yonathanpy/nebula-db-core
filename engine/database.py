from engine.planner import QueryPlanner
from engine.executor import Executor
from engine.transaction import TransactionManager
from storage.pager import Pager
from index.btree import BTreeIndex
from query.parser import QueryParser


class Database:

    def __init__(self, path):

        self.pager = Pager(path)

        self.tx = TransactionManager()

        self.parser = QueryParser()

        self.planner = QueryPlanner()

        self.executor = Executor(self.pager)

        self.index = BTreeIndex()

    def execute(self, sql):

        tokens = self.parser.parse(sql)

        plan = self.planner.build(tokens)

        result = self.executor.run(plan)

        return result

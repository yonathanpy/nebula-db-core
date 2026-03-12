class Executor:

    def __init__(self, pager):

        self.pager = pager

    def run(self, plan):

        if plan["op"] == "scan":

            return self._scan(plan["table"])

        if plan["op"] == "insert":

            return self._insert(plan["table"], plan["values"])

    def _scan(self, table):

        pages = self.pager.read_all()

        results = []

        for p in pages:

            results.extend(p["rows"])

        return results

    def _insert(self, table, values):

        page = self.pager.allocate()

        page["rows"].append(values)

        self.pager.write(page)

        return "inserted"

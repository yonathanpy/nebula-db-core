class QueryPlanner:

    def build(self, tokens):

        if tokens["type"] == "select":

            return {
                "op": "scan",
                "table": tokens["table"]
            }

        if tokens["type"] == "insert":

            return {
                "op": "insert",
                "table": tokens["table"],
                "values": tokens["values"]
            }

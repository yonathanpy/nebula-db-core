from query.tokenizer import tokenize


class QueryParser:

    def parse(self, sql):

        tokens = tokenize(sql)

        if tokens[0] == "select":

            return {
                "type": "select",
                "table": tokens[-1]
            }

        if tokens[0] == "insert":

            return {
                "type": "insert",
                "table": tokens[2],
                "values": tokens[4:]
            }

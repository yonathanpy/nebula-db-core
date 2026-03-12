import json
import os


class Pager:

    def __init__(self, file):

        self.file = file

        if not os.path.exists(file):

            with open(file, "w") as f:
                json.dump([], f)

    def read_all(self):

        with open(self.file) as f:

            return json.load(f)

    def allocate(self):

        return {"rows": []}

    def write(self, page):

        data = self.read_all()

        data.append(page)

        with open(self.file, "w") as f:

            json.dump(data, f)

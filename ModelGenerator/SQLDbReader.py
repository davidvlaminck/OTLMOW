import os
import sqlite3


class SQLDbReader:
    def __init__(self, path=None):
        self.path = path
        if path is None:
            self.file_exists = False
        else:
            self.file_exists = os.path.isfile(path)
            if not self.file_exists:
                raise FileNotFoundError(path + " is not a valid path. File does not exist.")

    def performReadQuery(self, query: str, params: dict):
        if not self.file_exists:
            raise FileNotFoundError(self.path + " is not a valid path. File does not exist.")

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        data = []
        for row in cur.execute(query, params):
            data.append(row)
        con.close()
        return data

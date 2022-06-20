import os
import sqlite3


class SQLDbReader:
    """SQLDbReader performs read query's. It first checks if the provided path has a file. Provides an easy way to override querying for testing purposes. """

    def __init__(self, path=''):
        self.path = path
        if path is None or path == '':
            self.file_exists = False
        else:
            self.file_exists = os.path.isfile(path)
            if not self.file_exists:
                raise FileNotFoundError(path + " is not a valid path. File does not exist.")

    def performReadQuery(self, query: str, params: dict):
        self.file_exists = os.path.isfile(self.path)
        if not self.file_exists:
            raise FileNotFoundError(self.path + " is not a valid path. File does not exist.")

        con = sqlite3.connect(self.path)
        cur = con.cursor()
        data = []
        for row in cur.execute(query, params):
            data.append(row)
        con.close()
        return data

import os
import sqlite3

from ModelGenerator.IFileExistChecker import IFileExistChecker


class SQLDbReader:
    fileExistChecker: IFileExistChecker

    def __init__(self, fileExistChecker: IFileExistChecker):
        self.fileExistChecker = fileExistChecker

    def performReadQuery(self, query: str, params: dict):
        if not (self.fileExistChecker.fileFound()):
            raise FileNotFoundError(self.fileExistChecker.path + " is not a valid path. File does not exist.")

        con = sqlite3.connect(self.fileExistChecker.path)
        cur = con.cursor()
        data = []
        for row in cur.execute(query, params):
            data.append(row)
        con.close()
        return data

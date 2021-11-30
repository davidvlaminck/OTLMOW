import os

from ModelGenerator.IFileExistChecker import IFileExistChecker


class FileExistChecker(IFileExistChecker):
    def fileFound(self):
        return os.path.isfile(self.path)

import unittest


class DavieImporter:
    @classmethod
    def Import(self, filePath):
        pass


class DavieImporterTests(unittest.TestCase):
    def test_FileNotFoundRaisesError(self):
        filePath=''
        DavieImporter.Import(filePath)
        raise NotImplementedError

    def test_ImportEmptyFileReturnEmptyList(self):
        raise NotImplementedError
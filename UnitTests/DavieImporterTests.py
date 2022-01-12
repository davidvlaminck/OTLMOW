import unittest

from Facility.DavieImporter import DavieImporter


class DavieImporterTests(unittest.TestCase):
    def test_FileNotFoundRaisesError(self):
        filePath=''
        DavieImporter.import_file(filePath)
        raise NotImplementedError

    def test_ImportEmptyFileReturnEmptyList(self):
        raise NotImplementedError
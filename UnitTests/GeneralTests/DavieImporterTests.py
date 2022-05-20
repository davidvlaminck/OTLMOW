import unittest
from OTLMOW.Facility.FileFormats.DavieImporter import DavieImporter


class DavieImporterTests(unittest.TestCase):
    @unittest.skip("not implemented yet")
    def test_FileNotFoundRaisesError(self):
        filePath=''
        DavieImporter.import_file(filePath)
        raise NotImplementedError

    @unittest.skip("not implemented yet")
    def test_ImportEmptyFileReturnEmptyList(self):
        raise NotImplementedError
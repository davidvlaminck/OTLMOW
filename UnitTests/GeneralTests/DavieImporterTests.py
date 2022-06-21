import unittest
from OTLMOW.Facility.FileFormats.JsonImporter import JsonImporter


class DavieImporterTests(unittest.TestCase):
    @unittest.skip("not implemented yet")
    def test_FileNotFoundRaisesError(self):
        filePath=''
        JsonImporter.import_file(filePath)
        raise NotImplementedError

    @unittest.skip("not implemented yet")
    def test_ImportEmptyFileReturnEmptyList(self):
        raise NotImplementedError
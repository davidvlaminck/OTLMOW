import unittest


class SkosParser:
    def Parse(self, url):
        raise FileNotFoundError()


class SkosParserTests(unittest.TestCase):
    def test_NotAvailableUrl(self):
        reader = SkosParser()
        #content = reader.Parse(
         #   'https://raw.githubusercontent.com/Informatievlaanderen/OSLOthema-wegenenverkeer/master/codelijsten/KlAIMToestand.ttl')
        self.assertRaises(FileNotFoundError, reader.Parse, '')

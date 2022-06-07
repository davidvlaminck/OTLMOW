from unittest import TestCase

from OTLMOW.ModelGenerator.StringHelper import wrap_in_quotes


class StringHelperTests(TestCase):
    def test_empty_string_returns_empty_string_in_single_quotes(self):
        result = wrap_in_quotes('')
        self.assertEqual("''", result)

    def test_None(self):
        with self.assertRaises(TypeError):
            wrap_in_quotes(None)

    def test_stringwithoutquotes_returns_stringwithsinglequotes(self):
        result = wrap_in_quotes('a')
        self.assertEqual("'a'", result)

    def test_stringwithsinglequotes_returns_stringwithdoublequotes(self):
        result = wrap_in_quotes("kado's")
        self.assertEqual('"kado\'s"', result)

    def test_stringwithdoublequotes_returns_stringwithsinglequotes(self):
        result = wrap_in_quotes('ik "test" dit uit')
        self.assertEqual('\'ik "test" dit uit\'', result)

    def test_stringwithmoredoublesthansingles_returns_stringwithsinglequotes(self):
        result = wrap_in_quotes("ik \"test\" kado's uit")
        self.assertEqual("\'ik \"test\" kado\\\'s uit\'", result)
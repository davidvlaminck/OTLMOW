from unittest import TestCase

from AllCasesTestClass import AllCasesTestClass


class NotConvertableToString:
    def __str__(self):
        pass

class OTLOAttribuutTests(TestCase):
    def test_set_waarde_kwant_wrd(self):
        test_instance = AllCasesTestClass()
        test_instance.testKwantWrd.waarde = 10
        self.assertEqual(10, test_instance.testKwantWrd.waarde)

    def test_set_waarde_stringfield(self):
        test_instance = AllCasesTestClass()
        test_instance.testStringField = 'a'
        self.assertEqual('a', test_instance.testStringField)

    def test_set_waarde_kwant_wrd_met_kard(self):
        test_instance = AllCasesTestClass()
        test_instance.testKwantWrdMetKard[0].waarde = 10
        test_instance._testKwantWrdMetKard.append_new_waardeObject()
        test_instance.testKwantWrdMetKard[1].waarde = 20
        self.assertEqual(10, test_instance.testKwantWrdMetKard[0].waarde)
        self.assertEqual(20, test_instance.testKwantWrdMetKard[1].waarde)

    def test_set_waarde_stringfield_met_kard(self):
        test_instance = AllCasesTestClass()
        test_instance.testStringFieldMetKard = ['a', 1]
        self.assertEqual('a', test_instance.testStringFieldMetKard[0])
        self.assertEqual('1', test_instance.testStringFieldMetKard[1])

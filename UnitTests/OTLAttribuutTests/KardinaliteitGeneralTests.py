import unittest

from AllCasesTestClass import AllCasesTestClass


class ContainerBuisKardinaliteitFieldTests(unittest.TestCase):
    def test_basic_assignment(self):
        instance = AllCasesTestClass()
        instance.testStringFieldMetKard = ['geel', 'rood']
        self.assertEqual("geel", instance.testStringFieldMetKard[0])
        self.assertEqual("rood", instance.testStringFieldMetKard[1])

    def test_basic_reassign(self):
        instance = AllCasesTestClass()
        instance.testStringFieldMetKard = ['geel']
        self.assertEqual("geel", instance.testStringFieldMetKard[0])

        instance.testStringFieldMetKard = ['geel', 'rood']
        self.assertEqual("geel", instance.testStringFieldMetKard[0])
        self.assertEqual("rood", instance.testStringFieldMetKard[1])

        instance.testStringFieldMetKard = None
        self.assertEqual(None, instance.testStringFieldMetKard)

    def test_two_instances(self):
        instance = AllCasesTestClass()
        instance.testStringFieldMetKard = ['geel', 'rood']
        instance2 = AllCasesTestClass()
        instance2.testStringFieldMetKard = ['blauw']
        self.assertTrue(instance.testStringFieldMetKard[0] == "geel")
        self.assertTrue(instance.testStringFieldMetKard[1] == "rood")
        self.assertTrue(instance2.testStringFieldMetKard[0] == "blauw")

    def test_errors(self):
        instance = AllCasesTestClass()

        with self.assertRaises(TypeError) as exc_number:
            instance.testStringFieldMetKard = 2
        self.assertEqual(str(exc_number.exception), "expecting a list in AllCasesTestClass.testStringFieldMetKard")

        with self.assertRaises(TypeError) as exc_dict:
            instance.testStringFieldMetKard = {}
        self.assertEqual(str(exc_dict.exception), "expecting a list in AllCasesTestClass.testStringFieldMetKard")

        instance._testStringFieldMetKard.kardinaliteit_min = "2"
        instance._testStringFieldMetKard.kardinaliteit_max = "2"
        with self.assertRaises(ValueError) as exc_list_one_short:
            instance.testStringFieldMetKard = ["geel"]
        self.assertEqual(str(exc_list_one_short.exception), "expecting at least 2 element(s) in AllCasesTestClass.testStringFieldMetKard")
        with self.assertRaises(ValueError) as exc_list_one_too_many:
            instance.testStringFieldMetKard = ["geel", "rood", "blauw"]
        self.assertEqual(str(exc_list_one_too_many.exception), "expecting at most 2 element(s) in AllCasesTestClass.testStringFieldMetKard")



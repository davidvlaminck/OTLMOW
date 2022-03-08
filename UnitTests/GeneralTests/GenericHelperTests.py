from unittest import TestCase

from OTLMOW.Facility.GenericHelper import GenericHelper


class TestClass:
    def __init__(self):
        self._a = ''

    @property
    def a(self):
        return self._a


    @a.setter
    def a(self, value):
        self._a = value


class GenericHelperTests(TestCase):
    def test_remove_duplicates_in_iterable_based_on_property(self):
        t = TestClass()
        t.a = '1'
        u = TestClass()
        u.a = '1'
        v = TestClass()
        v.a = '2'
        testset = [t, u, v]
        expected_result = [t, v]
        result = GenericHelper.remove_duplicates_in_iterable_based_on_property(testset, 'a')

        self.assertListEqual(expected_result, result)

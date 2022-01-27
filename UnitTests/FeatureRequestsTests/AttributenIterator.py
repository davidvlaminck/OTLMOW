import unittest
from unittest import TestCase

from OTLMOW.OTLModel.Classes.Aftakking import Aftakking


@unittest.skip("feature request")
class AttributenIterator(TestCase):
    def test_loop_over_attributes_of_asset(self):
        a = Aftakking()
        a.toestand = 'in-gebruik'
        a.naam = 'aftakking'
        expected_result = { 'naam': 'aftakking', 'toestand': 'in-gebruik'}
        self.assertDictEqual(expected_result, a.attributen_iterator)


# something like this:
# def _f():
#     yield 'key1', 10
#     yield 'key2', 20
#
# def f(): return dict(_f())
#
# print(f())
# # Output:
# {'key1': 10, 'key2': 20}
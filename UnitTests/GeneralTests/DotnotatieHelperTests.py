import json
from unittest import TestCase

from OTLMOW.Facility.DotnotatieHelper import DotnotatieHelper
from OTLMOW.OTLModel.Classes.BestratingVanKassei import BestratingVanKassei


class JsonLdTestData:
    simple = '{ "a": "value a", "b": "value b" }'
    dict_in_dict = '{ "a": "value a", "b": { "c": "value c", "d": "value d" } }'
    list = '{ "a": [1,2] }'
    listdict_in_dict = '{ "a": "value a", "b": [{ "c": "value c", "d": "value d" }, { "e": "value e", "f": "value f" }]}'

class DotnotatieHelperTests(TestCase):
    def test_flatten_dict_simple(self):
        input_dict = json.loads(JsonLdTestData.simple)

        output = DotnotatieHelper().flatten_dict(input_dict=input_dict)
        expected = {"a": "value a", "b": "value b"}
        self.assertDictEqual(expected, output)

    def test_flatten_dict_dict_in_dict(self):
        input_dict = json.loads(JsonLdTestData.dict_in_dict)

        output = DotnotatieHelper().flatten_dict(input_dict)
        expected = {"a": "value a", "b.c": "value c", "b.d": "value d"}
        self.assertDictEqual(expected, output)

    def test_flatten_dict_list(self):
        input_dict = json.loads(JsonLdTestData.list)

        output = DotnotatieHelper().flatten_dict(input_dict=input_dict)
        expected = {"a[0]": 1, "a[1]": 2}
        self.assertDictEqual(expected, output)

    def test_flatten_dict_listdict_in_dict(self):
        input_dict = json.loads(JsonLdTestData.listdict_in_dict)

        output = DotnotatieHelper().flatten_dict(input_dict=input_dict)
        expected = {"a": "value a", "b[0].c": "value c", "b[0].d": "value d", "b[1].e": "value e", "b[1].f": "value f"}
        self.assertDictEqual(expected, output)

    def test_set_attribute_by_dotnotatie_decimal_value(self):
        b = BestratingVanKassei()

        with self.subTest("correctly typed and convert=True"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte.waarde', 9.0, convert=True)
            self.assertEqual(9.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

        with self.subTest("correctly typed and convert=False"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte.waarde', 8.0, convert=False)
            self.assertEqual(8.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

        with self.subTest("incorrectly typed and convert=True"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte.waarde', "7.0", convert=True)
            self.assertEqual(7.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

        with self.subTest("incorrectly typed and convert=False (converted by set_waarde method on attribute itself)"):
            DotnotatieHelper.set_attribute_by_dotnotatie(b, 'afmetingVanBestratingselementBxl.breedte.waarde', "6.0", convert=False)
            self.assertEqual(6.0, b.afmetingVanBestratingselementBxl.breedte.waarde)

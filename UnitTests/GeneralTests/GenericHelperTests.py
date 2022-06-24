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

    def test_get_ns_and_name_from_uri_invalid_uris(self):
        agent_uri = 'http://purl.org/dc/terms/Agent'
        with self.assertRaises(ValueError):
            GenericHelper.get_ns_and_name_from_uri(agent_uri)

    def test_get_ns_and_name_from_uri_valid_uris(self):
        testset = {
            'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType': ('abstracten', 'AOWSType'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ActivityComplex': (
            'implementatieelement', 'ActivityComplex'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie': (
            'installatie', 'Aardingsinstallatie'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie': (
            'levenscyclus', 'BeheerHoutigeVegetatie'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera': ('onderdeel', 'ANPRCamera'),
            'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#Keuring': ('proefenmeting', 'Keuring')
        }

        for uri, expected_tuple in testset.items():
            with self.subTest(f'get_ns_and_name_from {uri}'):
                result_tuple = GenericHelper.get_ns_and_name_from_uri(uri)
                self.assertEqual(expected_tuple, result_tuple)

    def test_get_class_directory_from_ns(self):
        testset = {
            'abstracten': 'Classes\\Abstracten',
            'implementatieelement': 'Classes\\ImplementatieElement',
            'installatie': 'Classes\\Installatie',
            'levenscyclus': 'Classes\\Levenscyclus',
            'onderdeel': 'Classes\\Onderdeel',
            'proefenmeting': 'Classes\\ProefEnMeting'
        }

        for ns, class_dir in testset.items():
            with self.subTest(f'get_class_directory_from {ns}'):
                result_class_dir = GenericHelper.get_class_directory_from_ns(ns)
                self.assertEqual(class_dir, result_class_dir)

import unittest
from unittest.mock import Mock

from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from UnitTests.OSLOInMemoryCreatorTests import OSLOInMemoryCreatorTests


class OSLOCollectorTests(unittest.TestCase):
    def test_mock_CollectClassesAndAttributes(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = OSLOInMemoryCreatorTests().mockPerformReadQuery
        collector = OSLOCollector(oSLOCreator)
        collector.collect()

        # assert
        self.assertTrue(len(collector.classes) >= 1)
        self.assertTrue(len(collector.attributes) >= 1)
        self.assertTrue(len(collector.inheritances) >= 1)
        self.assertTrue(len(collector.primitiveDatatypes) >= 1)
        self.assertTrue(len(collector.primitiveDatatypeAttributen) >= 1)
        self.assertTrue(len(collector.complexDatatypes) >= 1)
        self.assertTrue(len(collector.complexDatatypeAttributen) >= 1)
        self.assertTrue(len(collector.enumerations) >= 1)

    def test_mock_CollectThenFindAttributesByClass(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = OSLOInMemoryCreatorTests().mockPerformReadQuery
        collector = OSLOCollector(oSLOCreator)
        collector.collect()

        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
        attribute_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad'
        naampadObject_class = next(c for c in collector.classes if c.uri == class_uri)
        attributes = collector.FindAttributesByClass(naampadObject_class)

        # assert
        self.assertIsNotNone(naampadObject_class)
        self.assertTrue(attributes[0].uri == attribute_uri)

    def test_mock_CollectThenFindInheritancesByClass(self):
        mock = Mock()
        oSLOCreator = OSLOInMemoryCreator(mock)
        mock.performReadQuery = OSLOInMemoryCreatorTests().mockPerformReadQuery
        collector = OSLOCollector(oSLOCreator)
        collector.collect()

        class_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
        base_class = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject'
        naampadObject_class = next(c for c in collector.classes if c.uri == class_uri)
        inheritances = collector.FindInheritancesByClass(naampadObject_class)

        # assert
        self.assertIsNotNone(naampadObject_class)
        self.assertTrue(inheritances[0].base_uri == base_class)

from unittest import TestCase

from OTLMOW.GeometrieArtefact.GeometrieArtefactCollector import GeometrieArtefactCollector
from OTLMOW.GeometrieArtefact.GeometrieInMemoryCreator import GeometrieInMemoryCreator
from OTLMOW.GeometrieArtefact.GeometrieInheritanceProcessor import GeometrieInheritanceProcessor
from OTLMOW.GeometrieArtefact.GeometrieType import GeometrieType
from OTLMOW.ModelGenerator.Inheritance import Inheritance
from OTLMOW.ModelGenerator.OSLOClass import OSLOClass
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader


class GeometryTypeTests(TestCase):
    def test_GeometryType_Baanlichaam(self):
        sqlReader = SQLDbReader('../../src/OTLMOW/InputFiles/Geometrie_Artefact_22_PU.db')
        memory = GeometrieInMemoryCreator(sqlReader)
        geo_collector = GeometrieArtefactCollector(memory)
        geo_collector.collect()
        geo_type_baanlichaam = geo_collector.find_by_objectUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam')
        self.assertTrue(isinstance(geo_type_baanlichaam, GeometrieType))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam', geo_type_baanlichaam.objectUri)
        self.assertEqual('Baanlichaam', geo_type_baanlichaam.label_nl)
        self.assertEqual(0, geo_type_baanlichaam.geen_geometrie)
        self.assertEqual(0, geo_type_baanlichaam.punt3D)
        self.assertEqual(0, geo_type_baanlichaam.lijn3D)
        self.assertEqual(1, geo_type_baanlichaam.polygoon3D)
        self.assertEqual('', geo_type_baanlichaam.gewijzigd_sinds)

    def test_InheritanceTest_A_has_concrete_classes_B_C_with_same_geotype(self):
        sqlReader = SQLDbReader('../../src/OTLMOW/InputFiles/Geometrie_Artefact_22_PU.db')
        memory = GeometrieInMemoryCreator(sqlReader)
        geo_collector = GeometrieArtefactCollector(memory)
        geo_collector.collect()
        geo_voertuig = geo_collector.find_by_objectUri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voertuiglantaarn')
        geo_fietslantaarn = geo_collector.find_by_objectUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietslantaarn')
        geometrie_types = [geo_voertuig, geo_fietslantaarn]
        inheritances = [
            Inheritance(base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn',
                        class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietslantaarn',
                        base_name='', class_name='', deprecated_version=''),
            Inheritance(base_uri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn',
                        class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voertuiglantaarn',
                        base_name='', class_name='', deprecated_version='')]
        classes = [
            OSLOClass('Seinlantaarn', 'Seinlantaarn', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn',
                      'Abstracte voor het geheel van één of meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun,teneinde de beweging van een weggebruiker die een bepaald traject volgt,te verhinderen of toe te laten.',
                      '', 1, ''),
            OSLOClass('Waarschuwingslantaarn', 'Waarschuwingslantaarn',
                      'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn',
                      'Abstracte voor waarschuwingsinrichtingen in de buurt van een verkeerslichtengeregeld kruispunt.', '', 1,
                      ''),
            OSLOClass('Fietslantaarn', 'Fietslantaarn', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietslantaarn',
                      'Geheel van meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun, teneinde de beweging van fietsers te verhinderen of toe te laten.',
                      '', 0, ''),
            OSLOClass('Knipperlantaarn', 'Knipperlantaarn',
                      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Knipperlantaarn',
                      'Een lantaarn bestaande uit één of meerdere knipperende oranje-geel verkeerslichten bevestigd op een steun, teneinde de weggebruiker te waarschuwen.',
                      '', 0, ''),
            OSLOClass('Voertuiglantaarn', 'Voertuiglantaarn',
                      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voertuiglantaarn',
                      'Geheel van meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun, teneinde de beweging van voertuigen te verhinderen of toe te laten.',
                      '', 0, ''),
            OSLOClass('Openbaar vervoerslantaarn', 'OpenbaarVervoerslantaarn',
                      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpenbaarVervoerslantaarn',
                      'Geheel van meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun, teneinde de beweging van het openbaar vervoer te verhinderen of toe te laten. Deze lantaarns worden enkel gebruikt op de plaatsen waar het openbaar vervoer in een eigen bedding of bijzondere overrijdbare bedding rijdt. Het openbaar vervoer en het toegelaten verkeer op de bijzondere overrijdbare bedding moeten deze verkeerslichten volgen',
                      '', 0, ''),
            OSLOClass('Combilantaarn', 'Combilantaarn', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Combilantaarn',
                      'Geheel van één of meerdere verkeerslichten die boven of naast elkaar worden opgesteld en worden bevestigd op een steun, teneinde de beweging van een weggebruiker die een bepaald traject volgt, te verhinderen of toe te laten door het gebruik van aangepaste lenzen',
                      '', 0, ''),
            OSLOClass('Voetgangerslantaarn', 'Voetgangerslantaarn',
                      'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voetgangerslantaarn',
                      'Geheel van meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun, teneinde de beweging van voetgangers te verhinderen of toe te laten.',
                      '', 0, '')]

        gip = GeometrieInheritanceProcessor(geometrie_types, inheritances, classes)
        processed_geometrie_types = gip.ProcessInheritances()
        self.assertTrue(isinstance(processed_geometrie_types, list))
        self.assertEqual(1, len(processed_geometrie_types))
        self.assertEqual('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn',
                         processed_geometrie_types[0].objectUri)
        self.assertEqual(0, len(gip.inheritances))

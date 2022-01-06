import unittest
from unittest import mock

from Loggers.NoneLogger import NoneLogger
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOAttribuut import OSLOAttribuut
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from ModelGenerator.OSLOTypeLink import OSLOTypeLink
from ModelGenerator.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from UnitTests.OTLModelCreatorTests.OTLComplexDatatypeCreatorTests import ComplexDatatypeOSLOCollector


class ClassOSLOCollector(OSLOCollector):
    def __init__(self):
        super().__init__(None)

        self.typeLinks = [
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#string", "OSLODatatypePrimitive", ""),
            OSLOTypeLink("http://www.w3.org/2001/XMLSchema#boolean", "OSLODatatypePrimitive", ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInProcent",
                         "OSLODatatypePrimitive", ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok",
                         "OSLODatatypePrimitive", ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteIPv4Adres",
                         "OSLODatatypePrimitive", ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres", "OSLODatatypeComplex",
                         ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument", "OSLODatatypeComplex",
                         ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente", "OSLOEnumeration",
                         ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte", "OSLODatatypeUnion",
                         ''),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter",
                         "OSLODatatypePrimitive", ""),
            OSLOTypeLink("https://schema.org/OpeningHoursSpecification", "OSLODatatypeComplex", ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlMaaiFrequentie", "OSLOEnumeration", "")
        ]


class TestAbstractCreator(AbstractDatatypeCreator):
    def __init__(self):
        super().__init__(NoneLogger(), ClassOSLOCollector())


class AbstractDatatypeCreatorTests(unittest.TestCase):
    def test_getFieldsToImportFromListOfAttributes_ListWithoutElement_NonEmptyStartList(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut('technischeFiche', 'technische fiche',
                                         'De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,...',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties',
                                         '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.technischeFiche',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument', 0, '',
                                         0, '', '')]
        listOfFields = creator.getFieldsToImportFromListOfAttributes(listOfAttributes, ['StringField'])

        self.assertEqual(['DtcDocument', 'StringField'], listOfFields)

    def test_getFieldsToImportFromListOfAttributes_ListWithOneComplexTypeDtcDocument(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut('technischeFiche', 'technische fiche',
                                         'De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,...',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties',
                                         '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.technischeFiche',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument', 0, '',
                                         0, '', '')]
        listOfFields = creator.getFieldsToImportFromListOfAttributes(listOfAttributes)

        self.assertEqual(['DtcDocument'], listOfFields)

    def test_getFieldsToImportFromListOfAttributes_ListWithKeuzelijstField(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut('gemeente', 'gemeente', 'De bestuurlijke eenheid waarin het adres gelegen is.',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.gemeente',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente', 0, '',
                                         0, '', '')]
        listOfFields = creator.getFieldsToImportFromListOfAttributes(listOfAttributes)

        self.assertEqual(['KeuzelijstField', 'KlAlgGemeente'], listOfFields)

    def test_getFieldsToImportFromListOfAttributes_ListWithOneStringType(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut(name='', label_nl='', definition_nl='', class_uri='', kardinaliteit_min='',
                                         kardinaliteit_max='', uri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0, constraints='', readonly=0,
                                         usagenote_nl='', deprecated_version='')]
        listOfFields = creator.getFieldsToImportFromListOfAttributes(listOfAttributes)

        self.assertEqual(['StringField'], listOfFields)

    def test_getFieldsToImportFromListOfAttributes_ListWithTwoStringTypes(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut(name='', label_nl='', definition_nl='', class_uri='', kardinaliteit_min='',
                                         kardinaliteit_max='', uri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0, constraints='', readonly=0,
                                         usagenote_nl='', deprecated_version=''),
            OSLODatatypeComplexAttribuut(name='', label_nl='', definition_nl='', class_uri='',
                                         kardinaliteit_min='', kardinaliteit_max='', uri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0,
                                         constraints='', readonly=0, usagenote_nl='', deprecated_version='')
        ]
        listOfFields = creator.getFieldsToImportFromListOfAttributes(listOfAttributes)

        self.assertEqual(['StringField'], listOfFields)

    def test_getFieldsToImportFromListOfAttributes_ListWithStringAndBoolField(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut(name='', label_nl='', definition_nl='', class_uri='', kardinaliteit_min='',
                                         kardinaliteit_max='', uri='',
                                         type='http://www.w3.org/2001/XMLSchema#boolean', overerving=0, constraints='',
                                         readonly=0, usagenote_nl='', deprecated_version=''),
            OSLODatatypeComplexAttribuut(name='', label_nl='', definition_nl='', class_uri='',
                                         kardinaliteit_min='', kardinaliteit_max='', uri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0,
                                         constraints='', readonly=0, usagenote_nl='', deprecated_version='')
        ]
        listOfFields = creator.getFieldsToImportFromListOfAttributes(listOfAttributes)

        self.assertEqual(['BooleanField', 'StringField'], listOfFields)

    def test_getFieldsAndNamesFromListOfAttributes(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut(name='boolean', label_nl='', definition_nl='', class_uri='', kardinaliteit_min='',
                                         kardinaliteit_max='', uri='',
                                         type='http://www.w3.org/2001/XMLSchema#boolean', overerving=0, constraints='',
                                         readonly=0, usagenote_nl='', deprecated_version=''),
            OSLODatatypeComplexAttribuut(name='string', label_nl='', definition_nl='', class_uri='',
                                         kardinaliteit_min='', kardinaliteit_max='', uri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0,
                                         constraints='', readonly=0, usagenote_nl='', deprecated_version=''),
            OSLODatatypeComplexAttribuut('technischeFiche', 'technische fiche',
                                         'De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,...',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties',
                                         '1', '1',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.technischeFiche',
                                         'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument', 0, '',
                                         0, '', '')]
        listOfFields = creator.getFieldsAndNamesFromListOfAttributes(listOfAttributes)

        self.assertEqual([('BooleanField', 'boolean'), ('DtcDocument', 'technischeFiche'), ('StringField', 'string')],
                         listOfFields)

    def test_getTypeLinkFromAttribuut_Boolean(self):
        creator = TestAbstractCreator()
        attribuut = OSLODatatypeComplexAttribuut(name='boolean', label_nl='', definition_nl='', class_uri='',
                                                 kardinaliteit_min='',
                                                 kardinaliteit_max='', uri='',
                                                 type='http://www.w3.org/2001/XMLSchema#boolean', overerving=0, constraints='',
                                                 readonly=0, usagenote_nl='', deprecated_version='')
        typeLink = creator.getTypeLinkFromAttribuut(attribuut)
        self.assertEqual("OSLODatatypePrimitive", typeLink)

    def test_getTypeLinkFromAttribuut_DtcDocument(self):
        creator = TestAbstractCreator()
        attribuut = OSLODatatypeComplexAttribuut('technischeFiche', 'technische fiche',
                                                 'De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,...',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties',
                                                 '1', '1',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.technischeFiche',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument',
                                                 0, '',
                                                 0, '', '')
        typeLink = creator.getTypeLinkFromAttribuut(attribuut)
        self.assertEqual("OSLODatatypeComplex", typeLink)

    def test_addAttributenToDataBlock_StringField(self):
        creator = TestAbstractCreator()
        attribuut = OSLODatatypeComplexAttribuut('huisnummer', 'huisnummer',
                                                 'Een nummer dat door de gemeente aan bv. een huis wordt toegekend.',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres',
                                                 '1', '1',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer',
                                                 'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', '')

        expectedDatablock = ['        self.waarde.huisnummer = StringField(naam="huisnummer",',
                             '                                             label="huisnummer",',
                             '                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer",',
                             '                                             definition="Een nummer dat door de gemeente aan bv. een huis wordt toegekend.",',
                             '                                             constraints="",',
                             '                                             usagenote="",',
                             '                                             deprecated_version="")',
                             '        self.huisnummer = self.waarde.huisnummer',
                             '        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], []))

    def test_addAttributenToDataBlock_DteField(self):
        creator = TestAbstractCreator()
        attribuut = OSLOAttribuut('toestandBuis', 'toestand buis', 'Opmerkingen van de toestand en staat van de buis.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok', 0, '', 0, '',
                                  '')

        expectedDatablock = ['        self.waarde.toestandBuis = DteTekstblok()',
                             '        """Opmerkingen van de toestand en staat van de buis."""',
                             '        self.waarde.toestandBuis.naam = "toestandBuis"',
                             '        self.waarde.toestandBuis.label = "toestand buis"',
                             '        self.waarde.toestandBuis.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis"',
                             '        self.waarde.toestandBuis.definition = "Opmerkingen van de toestand en staat van de buis."',
                             '        self.waarde.toestandBuis.constraints = ""',
                             '        self.waarde.toestandBuis.usagenote = ""',
                             '        self.waarde.toestandBuis.deprecated_version = ""',
                             '        self.toestandBuis = self.waarde.toestandBuis',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], []))

    def test_addAttributenToDataBlock_KwantWrd(self):
        creator = TestAbstractCreator()
        attribuut = OSLOAttribuut('lengte', 'lengte', 'De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter', 0, '', 0,
                                  '', '')

        expectedDatablock = ['        self.waarde.lengte = KwantWrdInMeter()',
                             '        """De totale lengte in meter van de buis tussen opwaartse en afwaartse put."""',
                             '        self.waarde.lengte.naam = "lengte"',
                             '        self.waarde.lengte.label = "lengte"',
                             '        self.waarde.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte"',
                             '        self.waarde.lengte.definition = "De totale lengte in meter van de buis tussen opwaartse en afwaartse put."',
                             '        self.waarde.lengte.constraints = ""',
                             '        self.waarde.lengte.usagenote = ""',
                             '        self.waarde.lengte.deprecated_version = ""',
                             '        self.lengte = self.waarde.lengte',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], []))

    def test_addAttributenToDataBlock_Keuzelijst(self):
        creator = TestAbstractCreator()
        attribuut = OSLODatatypeComplexAttribuut('gemeente', 'gemeente', 'De bestuurlijke eenheid waarin het adres gelegen is.',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres',
                                                 '1', '1',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.gemeente',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente',
                                                 0, '', 0, '',
                                                 '')

        expectedDatablock = ['        self.waarde.gemeente = KeuzelijstField(naam="gemeente",',
                             '                                               label="gemeente",',
                             '                                               lijst=KlAlgGemeente(),',
                             '                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.gemeente",',
                             '                                               definition="De bestuurlijke eenheid waarin het adres gelegen is.",',
                             '                                               constraints="",',
                             '                                               usagenote="",',
                             '                                               deprecated_version="")',
                             '        self.gemeente = self.waarde.gemeente',
                             '        """De bestuurlijke eenheid waarin het adres gelegen is."""',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], []))

    def test_addAttributenToDataBlock_DtcAdres(self):
        creator = TestAbstractCreator()
        attribuut = OSLODatatypeComplexAttribuut('adres', 'adres', 'Adres dat men kan aanschrijven of bezoeken.',
                                                 'https://schema.org/ContactPoint', '0', '1',
                                                 'https://schema.org/ContactPoint.adres',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', 0,
                                                 '', 0, '', '')

        expectedDatablock = ['        self.waarde.adres = DtcAdres()',
                             '        """Adres dat men kan aanschrijven of bezoeken."""',
                             '        self.waarde.adres.naam = "adres"',
                             '        self.waarde.adres.label = "adres"',
                             '        self.waarde.adres.uri = "https://schema.org/ContactPoint.adres"',
                             '        self.waarde.adres.definition = "Adres dat men kan aanschrijven of bezoeken."',
                             '        self.waarde.adres.constraints = ""',
                             '        self.waarde.adres.usagenote = ""',
                             '        self.waarde.adres.deprecated_version = ""',
                             '        self.adres = self.waarde.adres',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], []))

    def test_addAttributenToDataBlock_MaxKard_DtcOpeningsurenSpecificatie(self):
        creator = TestAbstractCreator()
        attribuut = OSLODatatypeComplexAttribuut('beschikbaarheid', 'beschikbaarheid',
                                                 'Periode waarin contact kan worden opgenomen.',
                                                 'https://schema.org/ContactPoint', '0', '*',
                                                 'https://schema.org/ContactPoint.beschikbaarheid',
                                                 'https://schema.org/OpeningHoursSpecification', 0, '', 0, '', '')

        expectedDatablock = ['        beschikbaarheidField = DtcOpeningsurenSpecificatie()',
                             '        beschikbaarheidField.naam = "beschikbaarheid"',
                             '        beschikbaarheidField.label = "beschikbaarheid"',
                             '        beschikbaarheidField.uri = "https://schema.org/ContactPoint.beschikbaarheid"',
                             '        beschikbaarheidField.definition = "Periode waarin contact kan worden opgenomen."',
                             '        beschikbaarheidField.constraints = ""',
                             '        beschikbaarheidField.usagenote = ""',
                             '        beschikbaarheidField.deprecated_version = ""',
                             '        self.waarde.beschikbaarheid = KardinaliteitField(minKardinaliteit="0", maxKardinaliteit="*", fieldToMultiply=beschikbaarheidField)',
                             '        self.beschikbaarheid = self.waarde.beschikbaarheid',
                             '        """Periode waarin contact kan worden opgenomen."""',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], []))

    def test_addAttributenToDataBlock_MaxKard_KeuzelijstInDtcMaaien(self):
        creator = TestAbstractCreator()
        attribuut = OSLODatatypeComplexAttribuut('frequentie', 'frequentie', 'Het aantal keer dat er gemaaid wordt per jaar.',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien', '1', '*',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.frequentie',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlMaaiFrequentie', 0,
                                                 '', 0, '', '')

        expectedDatablock = ['        frequentieField = KeuzelijstField(naam="frequentie",',
                             '                                          label="frequentie",',
                             '                                          lijst=KlMaaiFrequentie(),',
                             '                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.frequentie",',
                             '                                          definition="Het aantal keer dat er gemaaid wordt per jaar.",',
                             '                                          constraints="",',
                             '                                          usagenote="",',
                             '                                          deprecated_version="")',
                             '        self.waarde.frequentie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=frequentieField)',
                             '        self.frequentie = self.waarde.frequentie',
                             '        """Het aantal keer dat er gemaaid wordt per jaar."""',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], []))

    def test_addAttributenToDataBlock_MaxKard_StringFieldInDtcNatuurlijkPersoon(self):
        creator = TestAbstractCreator()
        attribuut = OSLODatatypeComplexAttribuut('emailadres', 'emailadres', 'Het emailadres.',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon',
                                                 '1', '*',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.emailadres',
                                                 'http://www.w3.org/2001/XMLSchema#string', 0, '', 0, '', '')

        expectedDatablock = ['        emailadresField = StringField(naam="emailadres",',
                             '                                      label="emailadres",',
                             '                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.emailadres",',
                             '                                      definition="Het emailadres.",',
                             '                                      constraints="",',
                             '                                      usagenote="",',
                             '                                      deprecated_version="")',
                             '        self.waarde.emailadres = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=emailadresField)',
                             '        self.emailadres = self.waarde.emailadres',
                             '        """Het emailadres."""',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], []))

    def test_addAttributenToDataBlock_MaxKard_KwantWrd_ClassAttribute(self):
        creator = TestAbstractCreator()
        attribuut = OSLOAttribuut('standen', 'standen',
                                  'Met de standen van de ventilator kan de draaisnelheid en soms ook de draairichting van de de bladen van de ventilator bepaald worden.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator', '1', '*',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.standen',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInProcent', 0, '', 0,
                                  '', '')

        expectedDatablock = ['        standenField = KwantWrdInProcent()',
                             '        standenField.naam = "standen"',
                             '        standenField.label = "standen"',
                             '        standenField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilator.standen"',
                             '        standenField.definition = "Met de standen van de ventilator kan de draaisnelheid en soms ook de draairichting van de de bladen van de ventilator bepaald worden."',
                             '        standenField.constraints = ""',
                             '        standenField.usagenote = ""',
                             '        standenField.deprecated_version = ""',
                             '        self.waarde.standen = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=standenField)',
                             '        self.standen = self.waarde.standen',
                             '        """Met de standen van de ventilator kan de draaisnelheid en soms ook de draairichting van de de bladen van de ventilator bepaald worden."""',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], [], False))

    def test_addAttributenToDataBlock_MaxKard_Dte_ClassAttribute(self):
        creator = TestAbstractCreator()
        attribuut = OSLOAttribuut('ipAdres', 'ip adres', 'Het IP-adres van de hardware.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang', '1', '*',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.ipAdres',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteIPv4Adres', 0, '', 0, '',
                                  '')

        expectedDatablock = ['        ipAdresField = DteIPv4Adres()',
                             '        ipAdresField.naam = "ipAdres"',
                             '        ipAdresField.label = "ip adres"',
                             '        ipAdresField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.ipAdres"',
                             '        ipAdresField.definition = "Het IP-adres van de hardware."',
                             '        ipAdresField.constraints = ""',
                             '        ipAdresField.usagenote = ""',
                             '        ipAdresField.deprecated_version = ""',
                             '        self.waarde.ipAdres = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=ipAdresField)',
                             '        self.ipAdres = self.waarde.ipAdres',
                             '        """Het IP-adres van de hardware."""',
                             '']

        self.assertEqual(expectedDatablock, creator.addAttributenToDataBlock([attribuut], [], False))

    # kard max DteField (https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.ipAdres)

    def test_getWhiteSpaceEquivalent_EmptyString(self):
        creator = TestAbstractCreator()
        result = creator.getWhiteSpaceEquivalent('')
        self.assertEqual('', result)

    def test_getWhiteSpaceEquivalent_StringOf1Length(self):
        creator = TestAbstractCreator()
        result = creator.getWhiteSpaceEquivalent('a')
        self.assertEqual(' ', result)

    def test_getWhiteSpaceEquivalent_StringOf2Length(self):
        creator = TestAbstractCreator()
        result = creator.getWhiteSpaceEquivalent('aa')
        self.assertEqual('  ', result)

    def test_getNonPrimitiveFieldFromTypeUri_ComplexField(self):
        creator = TestAbstractCreator()
        typesList = creator.getNonSingleFieldFromTypeUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')
        expectedList = ['ComplexField', 'DtcAdres']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_DteField(self):
        creator = TestAbstractCreator()
        typesList = creator.getNonSingleFieldFromTypeUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok')
        expectedList = ['ComplexField', 'DteTekstblok']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_KwantWrdField(self):
        creator = TestAbstractCreator()
        typesList = creator.getNonSingleFieldFromTypeUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter')
        expectedList = ['ComplexField', 'KwantWrdInCentimeter']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_UnionTypeField(self):
        creator = TestAbstractCreator()
        typesList = creator.getNonSingleFieldFromTypeUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte')
        expectedList = ['UnionTypeField', 'DtuLichtmastMasthoogte']

        self.assertEqual(expectedList, typesList)

    def test_getNonPrimitiveFieldFromTypeUri_Keuzelijst(self):
        creator = TestAbstractCreator()
        typesList = creator.getNonSingleFieldFromTypeUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgGemeente')
        expectedList = ['KeuzelijstField', 'KlAlgGemeente']

        self.assertEqual(expectedList, typesList)

    def test_getTypeNameOfComplexAttribuut_Kl(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        dtcIdentificator = collector.FindComplexDatatypeAttributenByClassUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')[1]
        typeName = creator.getTypeNameOfComplexAttribuut(dtcIdentificator.type)

        self.assertEqual("KlAlgGemeente", typeName)

    def test_getTypeNameOfComplexAttribuut_String(self):
        logger = NoneLogger()
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(logger, collector)
        dtcIdentificator = collector.FindComplexDatatypeAttributenByClassUri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')[0]
        typeName = creator.getTypeNameOfComplexAttribuut(dtcIdentificator.type)

        self.assertEqual("string", typeName)

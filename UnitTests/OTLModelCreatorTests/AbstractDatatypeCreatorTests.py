import unittest
from unittest import mock

from OTLMOW.ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from OTLMOW.ModelGenerator.OSLOAttribuut import OSLOAttribuut
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLODatatypeComplexAttribuut import OSLODatatypeComplexAttribuut
from OTLMOW.ModelGenerator.OSLOTypeLink import OSLOTypeLink
from OTLMOW.ModelGenerator.OTLComplexDatatypeCreator import OTLComplexDatatypeCreator
from OTLModelCreatorTests.OTLComplexDatatypeCreatorTests import ComplexDatatypeOSLOCollector


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
        super().__init__(ClassOSLOCollector())


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

        self.assertEqual(['KlAlgGemeente'], listOfFields)

    def test_getFieldsToImportFromListOfAttributes_ListWithOneStringType(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut(name='', label='', definition='', class_uri='', kardinaliteit_min='',
                                         kardinaliteit_max='', objectUri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0, constraints='', readonly=0,
                                         usagenote='', deprecated_version='')]
        listOfFields = creator.getFieldsToImportFromListOfAttributes(listOfAttributes)

        self.assertEqual(['StringField'], listOfFields)

    def test_getFieldsToImportFromListOfAttributes_ListWithTwoStringTypes(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut(name='', label='', definition='', class_uri='', kardinaliteit_min='',
                                         kardinaliteit_max='', objectUri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0, constraints='', readonly=0,
                                         usagenote='', deprecated_version=''),
            OSLODatatypeComplexAttribuut(name='', label='', definition='', class_uri='',
                                         kardinaliteit_min='', kardinaliteit_max='', objectUri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0,
                                         constraints='', readonly=0, usagenote='', deprecated_version='')
        ]
        listOfFields = creator.getFieldsToImportFromListOfAttributes(listOfAttributes)

        self.assertEqual(['StringField'], listOfFields)

    def test_getFieldsToImportFromListOfAttributes_ListWithStringAndBoolField(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut(name='', label='', definition='', class_uri='', kardinaliteit_min='',
                                         kardinaliteit_max='', objectUri='',
                                         type='http://www.w3.org/2001/XMLSchema#boolean', overerving=0, constraints='',
                                         readonly=0, usagenote='', deprecated_version=''),
            OSLODatatypeComplexAttribuut(name='', label='', definition='', class_uri='',
                                         kardinaliteit_min='', kardinaliteit_max='', objectUri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0,
                                         constraints='', readonly=0, usagenote='', deprecated_version='')
        ]
        listOfFields = creator.getFieldsToImportFromListOfAttributes(listOfAttributes)

        self.assertEqual(['BooleanField', 'StringField'], listOfFields)

    def test_getFieldsAndNamesFromListOfAttributes(self):
        creator = TestAbstractCreator()
        listOfAttributes = [
            OSLODatatypeComplexAttribuut(name='boolean', label='', definition='', class_uri='', kardinaliteit_min='',
                                         kardinaliteit_max='', objectUri='',
                                         type='http://www.w3.org/2001/XMLSchema#boolean', overerving=0, constraints='',
                                         readonly=0, usagenote='', deprecated_version=''),
            OSLODatatypeComplexAttribuut(name='string', label='', definition='', class_uri='',
                                         kardinaliteit_min='', kardinaliteit_max='', objectUri='',
                                         type='http://www.w3.org/2001/XMLSchema#string', overerving=0,
                                         constraints='', readonly=0, usagenote='', deprecated_version=''),
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
        attribuut = OSLODatatypeComplexAttribuut(name='boolean', label='', definition='', class_uri='',
                                                 kardinaliteit_min='',
                                                 kardinaliteit_max='', objectUri='',
                                                 type='http://www.w3.org/2001/XMLSchema#boolean', overerving=0, constraints='',
                                                 readonly=0, usagenote='', deprecated_version='')
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

        expectedDatablock = ['        self._huisnummer = OTLAttribuut(field=StringField,',
                             "                                        naam='huisnummer',",
                             "                                        label='huisnummer',",
                             "                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer',",
                             "                                        definition='Een nummer dat door de gemeente aan bv. een huis wordt toegekend.',",
                             "                                        owner=self)",
                             '',
                             '    @property',
                             '    def huisnummer(self):',
                             '        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""',
                             '        return self._huisnummer.get_waarde()',
                             '',
                             '    @huisnummer.setter',
                             '    def huisnummer(self, value):',
                             '        self._huisnummer.set_waarde(value, owner=self._parent)',
                             '']

        self.assertEqual(expectedDatablock, creator.add_attributen_to_dataBlock([attribuut], []))

    def test_addAttributenToDataBlock_DteField(self):
        creator = TestAbstractCreator()
        attribuut = OSLOAttribuut('toestandBuis', 'toestand buis', 'Opmerkingen van de toestand en staat van de buis.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok', 0, '', 0, '',
                                  '')

        expectedDatablock = ['        self._toestandBuis = OTLAttribuut(field=DteTekstblok,',
                             "                                          naam='toestandBuis',",
                             "                                          label='toestand buis',",
                             "                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis',",
                             "                                          definition='Opmerkingen van de toestand en staat van de buis.',",
                             "                                          owner=self)",
                             '',
                             '    @property',
                             '    def toestandBuis(self):',
                             '        """Opmerkingen van de toestand en staat van de buis."""',
                             '        return self._toestandBuis.get_waarde()',
                             '',
                             '    @toestandBuis.setter',
                             '    def toestandBuis(self, value):',
                             '        self._toestandBuis.set_waarde(value, owner=self._parent)',
                             '']

        self.assertEqual(expectedDatablock, creator.add_attributen_to_dataBlock([attribuut], []))

    def test_addAttributenToDataBlock_KwantWrd(self):
        creator = TestAbstractCreator()
        attribuut = OSLOAttribuut('lengte', 'lengte', 'De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', '1', '1',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',
                                  'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter', 0, '', 0,
                                  '', '')

        expectedDatablock = ['        self._lengte = OTLAttribuut(field=KwantWrdInMeter,',
                             "                                    naam='lengte',",
                             "                                    label='lengte',",
                             "                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte',",
                             "                                    definition='De totale lengte in meter van de buis tussen opwaartse en afwaartse put.',",
                             "                                    owner=self)",
                             '',
                             '    @property',
                             '    def lengte(self):',
                             '        """De totale lengte in meter van de buis tussen opwaartse en afwaartse put."""',
                             '        return self._lengte.get_waarde()',
                             '',
                             '    @lengte.setter',
                             '    def lengte(self, value):',
                             '        self._lengte.set_waarde(value, owner=self._parent)',
                             '']

        self.assertEqual(expectedDatablock, creator.add_attributen_to_dataBlock([attribuut], []))

    def test_addAttributenToDataBlock_DtcAdres(self):
        creator = TestAbstractCreator()
        attribuut = OSLODatatypeComplexAttribuut('adres', 'adres', 'Adres dat men kan aanschrijven of bezoeken.',
                                                 'https://schema.org/ContactPoint', '0', '1',
                                                 'https://schema.org/ContactPoint.adres',
                                                 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres', 0,
                                                 '', 0, '', '')

        expectedDatablock = ['        self._adres = OTLAttribuut(field=DtcAdres,',
                             "                                   naam='adres',",
                             "                                   label='adres',",
                             "                                   objectUri='https://schema.org/ContactPoint.adres',",
                             "                                   kardinaliteit_min='0',",
                             "                                   definition='Adres dat men kan aanschrijven of bezoeken.',",
                             "                                   owner=self)",
                             '',
                             '    @property',
                             '    def adres(self):',
                             '        """Adres dat men kan aanschrijven of bezoeken."""',
                             '        return self._adres.get_waarde()',
                             '',
                             '    @adres.setter',
                             '    def adres(self, value):',
                             '        self._adres.set_waarde(value, owner=self._parent)',
                             '']

        self.assertEqual(expectedDatablock, creator.add_attributen_to_dataBlock([attribuut], []))

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
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(collector)
        dtcIdentificator = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')[1]
        typeName = creator.getTypeNameOfComplexAttribuut(dtcIdentificator.type)

        self.assertEqual("KlAlgGemeente", typeName)

    def test_getTypeNameOfComplexAttribuut_String(self):
        collector = ComplexDatatypeOSLOCollector(mock)
        creator = OTLComplexDatatypeCreator(collector)
        dtcIdentificator = collector.find_complex_datatype_attributes_by_class_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres')[0]
        typeName = creator.getTypeNameOfComplexAttribuut(dtcIdentificator.type)

        self.assertEqual("string", typeName)

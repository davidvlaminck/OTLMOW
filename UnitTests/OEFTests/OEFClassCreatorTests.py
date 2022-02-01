import unittest

from OTLMOW.Loggers.NoneLogger import NoneLogger
from OTLMOW.OEFModel.OEFClassCreator import OEFClassCreator


class OEFClassCreatorTestData:
    expected_datablock = ["# coding=utf-8",
                          "from OEFModel.EMObject import EMObject",
                          "from OTLMOW.OEFModel.EMAttribuut import EMAttribuut",
                          "from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField",
                          "",
                          "",
                          "# Generated with OEFClassCreator. To modify: extend, do not edit",
                          "class AID(EMObject):",
                          '    """Automatische incidentendetectie"""',
                          "",
                          "    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#AID'",
                          "    label = 'Automatische incidentendetectie'",
                          "",
                          "    def __init__(self):",
                          "        super().__init__()",
                          "",
                          "        self._encoderAanwezig = EMAttribuut(field=BooleanField,",
                          "                                            naam='encoder aanwezig?',",
                          "                                            label='encoder aanwezig?',",
                          "                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderAanwezig',",
                          "                                            definitie='Definitie nog toe te voegen voor eigenschap encoder aanwezig?')",
                          "",
                          "    @property",
                          "    def encoderAanwezig(self):",
                          '        """Definitie nog toe te voegen voor eigenschap encoder aanwezig?"""',
                          "        return self._encoderAanwezig.waarde",
                          "",
                          "    @encoderAanwezig.setter",
                          "    def encoderAanwezig(self, value):",
                          "        self._encoderAanwezig.set_waarde(value, owner=self)",
                          ""]

    test_class = {
        "uri": "https://lgc.data.wegenenverkeer.be/ns/installatie#AID",
        "naam": "AID",
        "label": "Automatische incidentendetectie",
        "definitie": "Automatische incidentendetectie",
        "abstract": False,
        "superClasses": [
        ],
        "attributen": [
            {
                "attribuut": "https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderAanwezig"
            },
            {
                "attribuut": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI"
            }]
    }

    attributen = [{
        "uri": "https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderAanwezig",
        "naam": "encoder aanwezig?",
        "label": "encoder aanwezig?",
        "definitie": "Definitie nog toe te voegen voor eigenschap encoder aanwezig?",
        "dataType": "http://www.w3.org/2001/XMLSchema#boolean",
        "kardinaliteit": "1..1"
    }]


class OEFClassCreatorTests(unittest.TestCase):
    def test_find_attributes_by_class(self):
        oef_class_creator = OEFClassCreator(NoneLogger(), OEFClassCreatorTestData.attributen)

        oef_attributen = oef_class_creator.find_attributes_by_class(OEFClassCreatorTestData.test_class)
        self.assertEqual(1, len(oef_attributen))
        self.assertEqual('encoder aanwezig?', oef_attributen[0]['label'])

    def test_get_fields_to_import_from_list_of_attributes(self):
        attributen = [{
            "uri": "https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderAanwezig",
            "naam": "encoder aanwezig?",
            "label": "encoder aanwezig?",
            "definitie": "Definitie nog toe te voegen voor eigenschap encoder aanwezig?",
            "dataType": "http://www.w3.org/2001/XMLSchema#boolean",
            "kardinaliteit": "1..1"
        }, {
            "uri": "https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.codeklavierAantal",
            "naam": "codeklavier aantal",
            "label": "codeklavier aantal",
            "definitie": "Definitie nog toe te voegen voor eigenschap codeklavier aantal",
            "dataType": "http://www.w3.org/2001/XMLSchema#decimal",
            "kardinaliteit": "1..1"
        }]

        oef_class_creator = OEFClassCreator(NoneLogger(), attributen)

        result_2_types = oef_class_creator.get_fields_to_import_from_list_of_attributes(attributen)
        result_1_type = oef_class_creator.get_fields_to_import_from_list_of_attributes(attributen[0:1])

        self.assertEqual(2, len(result_2_types))
        self.assertListEqual(['BooleanField', 'FloatOrDecimalField'], result_2_types)

        self.assertEqual(1, len(result_1_type))
        self.assertListEqual(['BooleanField'], result_1_type)

    def test_create_block_to_write_from_class(self):
        oef_class_creator = OEFClassCreator(NoneLogger(), OEFClassCreatorTestData.attributen)
        oef_class_creator.attributen = oef_class_creator.find_attributes_by_class(OEFClassCreatorTestData.test_class)

        datablock_result = oef_class_creator.create_block_to_write_from_class(OEFClassCreatorTestData.test_class)

        self.assertEqual(OEFClassCreatorTestData.expected_datablock, datablock_result)

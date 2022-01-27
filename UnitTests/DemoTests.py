from unittest import TestCase

from src.OTLMOW.Facility.OTLFacility import OTLFacility
from src.OTLMOW.Loggers.NoneLogger import NoneLogger
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Classes.Stroomkring import Stroomkring


class DemoTests(TestCase):
    #@unittest.skip('not an actual unit test')
    def test_demo(self):
        fac = OTLFacility(NoneLogger())
        kring = fac.asset_factory.dynamic_create_instance_from_name('Stroomkring')
        kring.typeURI  # print uri to verify type
        self.assertTrue(isinstance(kring, Stroomkring))  # other way in python to verify

        kring = Stroomkring()  # alternative to create Stroomkring
        self.assertTrue(isinstance(kring, AIMObject))  # true inheritance
        kring.toestand = 'in-gebruik'


        print(kring.info())
        print(kring.info_attr(''))

        print(kring.info_attr('assetId'))
        print(kring.info_attr_type('assetId'))

        kring.assetId.identificator = 'eigen_id'
        kring.assetId.toegekendDoor = 'Python'
        print(kring.assetId)  # print assetId

        kring.theoretischeLevensduur.waarde = 120

        # show some value validation

        # show relaties:
        # print(kring._showGeldigeRelaties())

        #fac.davieExporter.export_objects_to_json_file(kring, 'kring.json')

        #fac.visualiser.show([kring])









from unittest import TestCase

from Facility.OTLFacility import OTLFacility
from Loggers.NoneLogger import NoneLogger
from OTLModel.Classes.Stroomkring import Stroomkring


class DemoTests(TestCase):
    def test_demo(self):
        fac = OTLFacility(NoneLogger())
        kring = fac.asset_factory.dynamic_create_instance_from_name('Stroomkring')
        self.assertTrue(isinstance(kring, Stroomkring))
        kring.typeURI  # print uri
        kring.assetId.identificator = 'eigen_id'
        kring.assetId.toegekendDoor = 'Python'
        kring.assetId  # print assetId
        kring.toestand = 'in-gebruik'
        kring.theoretischeLevensduur.waarde = 120
        print(kring.info())
        print(kring.attr_info('assetId'))
        print(kring.attr_type_info('assetId'))  # TODO add more info about attributes

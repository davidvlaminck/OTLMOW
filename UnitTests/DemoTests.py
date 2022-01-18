from unittest import TestCase

from Facility.OTLFacility import OTLFacility
from Loggers.NoneLogger import NoneLogger

class DemoTests(TestCase):
    def test_demo(self):
        fac = OTLFacility(NoneLogger())
        kring = fac.asset_factory.dynamic_create_instance_from_name('Stroomkring')
        uri = kring.typeURI
        assetId = kring.assetId
        print(kring.attr_info('assetId'))
        print(kring.attr_type_info('assetId'))

import copy
import json.decoder
from datetime import datetime
from unittest import TestCase

from EMInfraResponseTestDouble import ResponseTestDouble
from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from OTLModel.ClassLoader import ClassLoader
from OTLModel.Classes.Omvormer import Omvormer
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


class EMInfraDecoder:
    def decode(self, responseString):
        dict_obj = json.loads(responseString)
        lijst = []
        for obj in dict_obj["@graph"]:
            typeURI = next(value for key, value in obj.items() if 'typeURI' in key)

            if 'https://wegenenverkeer.data.vlaanderen.be/ns' not in typeURI:
                continue

            instance = ClassLoader().dynamic_create_instance_from_uri(typeURI)
            lijst.append(instance)

            for key, value in obj.items():
                if key.startswith('@') or 'typeURI' in key or value == '' or 'toezichter' in key or 'puntlocatie' in key:
                    continue
                if 'geometrie' in key:
                    key = 'loc:Locatie.geometry'

                self.set_attribute(instance, key, value)

        return lijst

    def set_attribute(self, instance, attr_key, value):
        attrnaam = attr_key.split('.')[-1]
        attribute = getattr(instance, attrnaam)
        if isinstance(attribute, KeuzelijstField):
            attribute.set_value_by_invulwaarde(value.split('/')[-1])
        elif isinstance(attribute, ComplexField):
            for k, v in value.items():
                self.set_attribute(attribute, k, v)
        elif isinstance(attribute, DateField):
            attribute.waarde = datetime.strptime(value, '%Y-%m-%d')
        elif isinstance(attribute, KardinaliteitField):
            lijstValues = []
            for valueDict in value:
                attributeInstance = copy.deepcopy(attribute.fieldToMultiply)
                for k, v in valueDict.items():
                    self.set_attribute(attributeInstance, k, v)
                lijstValues.append(attributeInstance)
            attribute.waarde = lijstValues
        else:
            attribute.waarde = value


class EMInfraDecoderTests(TestCase):
    def test_decodeFirstEntry(self):
        responseString = ResponseTestDouble().response
        decoder = EMInfraDecoder()
        list = decoder.decode(responseString)
        first = list[0]
        self.assertTrue(isinstance(first, Omvormer))
        self.assertEqual("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer", first.typeURI)
        self.assertEqual("ENCA0469", first.naam.waarde)
        self.assertEqual(None, first.notitie.waarde)  # TODO check
        self.assertEqual("Encoder", first.type.waarde.invulwaarde)
        self.assertEqual(True, first.isActief.waarde)
        self.assertEqual("in-gebruik", first.toestand.waarde.invulwaarde)
        self.assertEqual("10.216.10.33", first.ipAdres.waarde)
        self.assertEqual("AWV", first.assetId.toegekendDoor.waarde)
        self.assertEqual("0005bafb-838f-47e0-a4e2-20dd120ede6b-b25kZXJkZWVsI09tdm9ybWVy", first.assetId.identificator.waarde)

    def test_decodeAndEncode(self):
        responseString = ResponseTestDouble().response
        decoder = EMInfraDecoder()
        list = decoder.decode(responseString)
        encoder = OtlAssetJSONEncoder()
        json = encoder.encode(list)
        self.assertEqual(ResponseTestDouble().expectedJson, json)
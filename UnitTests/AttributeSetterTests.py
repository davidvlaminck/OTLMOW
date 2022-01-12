import json
from datetime import datetime
from unittest import TestCase

from Facility.AttributeSetters import AttributeSetterFactory, ComplexFieldSetter, KardinaliteitFieldSetter, KeuzelijstFieldSetter, \
    DateFieldSetter, PrimitiveFieldSetter
from OTLModel.Classes.Afscherming import Afscherming
from OTLModel.Classes.Brandleiding import Brandleiding
from OTLModel.Classes.Buitenkast import Buitenkast
from OTLModel.Classes.DNBLaagspanning import DNBLaagspanning
from OTLModel.Classes.Mantelbuis import Mantelbuis
from OTLModel.Classes.Verkeersregelaar import Verkeersregelaar
from OTLModel.Classes.Wegkantkast import Wegkantkast


class AttributeSetterTests(TestCase):
    def test_decode_StringField(self):
        instance = Afscherming()
        obj = json.loads("""{"notitie": "test notitie"}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, PrimitiveFieldSetter))
        self.assertEqual("test notitie", instance.notitie.waarde)

    def test_decode_BooleanField(self):
        instance = Brandleiding()
        obj = json.loads("""{"isGeisoleerd": true}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, PrimitiveFieldSetter))
        self.assertEqual(True, instance.isGeisoleerd.waarde)

    def test_decode_KwantWrdField(self):
        instance = Brandleiding()
        obj = json.loads("""{"leidingdruk": 1.5}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, PrimitiveFieldSetter))
        self.assertEqual(1.5, instance.leidingdruk.waarde)

    def test_decode_DateField(self):
        instance = Afscherming()
        obj = json.loads("""{"datumOprichtingObject" : "2020-04-22"}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, DateFieldSetter))
        self.assertEqual(datetime(2020, 4, 22, 0, 0, 0), instance.datumOprichtingObject.waarde)

    def test_decode_KeuzelijstField(self):
        instance = Afscherming()
        obj = json.loads("""{"toestand" : "in-gebruik"}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, KeuzelijstFieldSetter))
        self.assertEqual('in-gebruik', instance.toestand.waarde.invulwaarde)

    def test_decode_KardinaliteitOfKeuzelijstField(self):
        instance = Verkeersregelaar()
        obj = json.loads("""{"coordinatiewijze" : [ "centraal", "pulsen" ]}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, KardinaliteitFieldSetter))
        self.assertEqual('centraal', instance.coordinatiewijze.waarde[0].waarde.invulwaarde)
        self.assertEqual('pulsen', instance.coordinatiewijze.waarde[1].waarde.invulwaarde)

    def test_decode_KardinaliteitOfStringField(self):
        instance = Mantelbuis()
        obj = json.loads("""{"kleur" : [ "geel", "rood" ]}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, KardinaliteitFieldSetter))
        self.assertEqual('geel', instance.kleur.waarde[0].waarde)
        self.assertEqual('rood', instance.kleur.waarde[1].waarde)

    def test_decode_complexField(self):
        instance = Afscherming()
        obj = json.loads(
            """{"assetId": {"identificator": "000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA", "toegekendDoor": "AWV" }}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, ComplexFieldSetter))
        self.assertEqual("000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
                         instance.assetId.identificator.waarde)
        self.assertEqual("AWV", instance.assetId.toegekendDoor.waarde)

    def test_decode_KardinaliteitOfComplexField(self):
        instance = Verkeersregelaar()
        obj = json.loads("""{"externeReferentie":[{"externePartij":"bij externe partij 2","externReferentienummer":"externe referentie 2"  }, {    "externePartij" : "bij externe partij 1",    "externReferentienummer" : "externe referentie 1"  } ]}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, KardinaliteitFieldSetter))
        self.assertEqual("bij externe partij 2", instance.externeReferentie.waarde[0].waarde.externePartij.waarde)
        self.assertEqual("externe referentie 2", instance.externeReferentie.waarde[0].waarde.externReferentienummer.waarde)
        self.assertEqual("bij externe partij 1", instance.externeReferentie.waarde[1].waarde.externePartij.waarde)
        self.assertEqual("externe referentie 1", instance.externeReferentie.waarde[1].waarde.externReferentienummer.waarde)

    def test_decode_ComplexOfComplexField(self):
        instance = DNBLaagspanning()
        obj = json.loads("""{"energieleverancier":{"adres":{"straatnaam":"teststraat"}}}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, ComplexFieldSetter))
        self.assertEqual("teststraat", instance.energieleverancier.adres.straatnaam.waarde)

    def test_decode_NonNegIntFieldInKwantWrd(self):
        instance = Wegkantkast()
        obj = json.loads("""{"keuringsfrequentie":1}""")

        for key, value in obj.items():
            attr_naam = key.split('.')[-1]
            attribute_setter = AttributeSetterFactory.CreateSetter(instance, attr_naam)
            if attribute_setter is not None:
                attribute_setter.set_attribute(value)

        self.assertTrue(isinstance(attribute_setter, PrimitiveFieldSetter))
        self.assertEqual(1, instance.keuringsfrequentie.waarde)

# TODO
# write test for
# DateTimeField
# TimeField
# UnionTypeField



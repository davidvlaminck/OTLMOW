import unittest

from OTLClasses.Verification.AIMToestand import AIMToestand


class AIMToestandTestInstance(AIMToestand):
    def __init__(self):
        pass


class AIMToestandTests(unittest.TestCase):
    def test_useOTLClassAIMToestand(self):
        instance = AIMToestandTestInstance()
        instance.toestand.setValueByLabel("in ontwerp")

        self.assertTrue(isinstance(instance, AIMToestand))
        self.assertTrue(instance.uri == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand")
        self.assertTrue(instance.toestand.value.label == "in ontwerp")
        self.assertTrue(instance.toestand.value.waarde == "in-ontwerp")


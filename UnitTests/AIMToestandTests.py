import unittest

from OTLModel.Classes.AIMToestand import AIMToestand


class AIMToestandTestInstance(AIMToestand):
    def __init__(self):
        super().__init__()


class AIMToestandTests(unittest.TestCase):
    def test_useOTLClassAIMToestand(self):
        instance = AIMToestandTestInstance()
        instance.toestand.set_value_by_label("in ontwerp")

        self.assertTrue(isinstance(instance, AIMToestand))
        self.assertTrue(instance.typeURI == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand")
        self.assertTrue(instance.toestand.waarde.label == "in ontwerp")
        self.assertTrue(instance.toestand.waarde.invulwaarde == "in-ontwerp")

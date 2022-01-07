import unittest

from OTLModel.Classes.AIMDBStatus import AIMDBStatus


class AIMDBStatusTestInstance(AIMDBStatus):
    def __init__(self):
        super().__init__()


class AIMDBStatusTests(unittest.TestCase):
    def test_useOTLClassAIMDBStatus(self):
        instance = AIMDBStatusTestInstance()
        self.assertIsNone(instance.isActief.waarde)
        instance.isActief.waarde = True

        self.assertTrue(instance.isActief.waarde)
        self.assertTrue(instance.typeURI == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus")
        self.assertTrue(isinstance(instance, AIMDBStatus))

    def test_useOTLClassAIMDBStatus_errors(self):
        instance = AIMDBStatusTestInstance()
        instance.isActief.waarde = True

        with self.assertRaises(ValueError):
            instance.isActief.waarde = "True"

        with self.assertRaises(ValueError):
            instance.isActief.waarde = 2

        with self.assertRaises(TypeError):
            instanceOfAbstractClass = AIMDBStatus()



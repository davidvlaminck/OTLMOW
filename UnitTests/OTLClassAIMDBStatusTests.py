import unittest

from OTLModel.Verification.AIMDBStatus import AIMDBStatus


class AIMDBStatusTestInstance(AIMDBStatus):
    def __init__(self):
        super().__init__()


class AIMDBStatusTests(unittest.TestCase):
    def test_useOTLClassAIMDBStatus(self):
        instance = AIMDBStatusTestInstance()
        instance.isActief = True

        self.assertTrue(instance.isActief)
        self.assertTrue(instance.typeURI == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus")
        self.assertTrue(isinstance(instance, AIMDBStatus))

        with self.assertRaises(ValueError):
            instance.isActief = 2

        with self.assertRaises(ValueError):
            instance.isActief = "True"

        with self.assertRaises(TypeError):
            instanceOfAbstractClass = AIMDBStatus()

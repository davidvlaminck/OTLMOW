import unittest

from OTLClasses.Verification.AIMDBStatus import AIMDBStatus


class AIMDBStatusTestInstance(AIMDBStatus):
    def __init__(self):
        pass


class AIMDBStatusTests(unittest.TestCase):
    def test_useOTLClassAIMDBStatus(self):
        instance = AIMDBStatusTestInstance()
        instance.isActief = True

        self.assertTrue(instance.isActief)
        self.assertTrue(instance.uri == "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMDBStatus")
        self.assertTrue(isinstance(instance, AIMDBStatus))

        with self.assertRaises(ValueError):
            instance.isActief = 1

        with self.assertRaises(ValueError):
            instance.isActief = "True"

        with self.assertRaises(TypeError):
            instanceOfAbstractClass = AIMDBStatus()

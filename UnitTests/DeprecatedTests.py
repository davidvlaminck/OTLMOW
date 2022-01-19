import warnings
from unittest import TestCase

from OTLModel.Classes.Aftakking import Aftakking
from OTLModel.Classes.Exoten import Exoten
from OTLModel.Classes.Voedt import Voedt


class DemoTests(TestCase):
    def test_use_regular_class(self):
        a = Aftakking()
        if hasattr(a, 'deprecated_version'):
            self.assertIsNone(a.deprecated_version)
        else:
            self.assertTrue(True)

    def test_use_deprecated_class(self):
        with self.assertWarns(DeprecationWarning):
            e = Exoten()

    def test_use_regular_attribute(self):
        with warnings.catch_warnings(record=True) as warns:
            v = Voedt()
            v.aansluitspanning.waarde = 230
        deprecated = list(filter(lambda x: isinstance(x, DeprecationWarning), warns))
        self.assertEqual(0, len(deprecated))

    def test_use_deprecated_attribute(self):
        with self.assertWarns(DeprecationWarning):
            v = Voedt()
            v.aansluitvermogen.waarde = 20





    # TODO add test for attributes

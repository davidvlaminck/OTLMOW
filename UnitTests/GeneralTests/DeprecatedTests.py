﻿import warnings
from unittest import TestCase

from OTLMOW.OTLModel.Classes.Onderdeel.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Onderdeel.Exoten import Exoten
from OTLMOW.OTLModel.Classes.Onderdeel.Voedt import Voedt


class DeprecatedTests(TestCase):
    def test_use_regular_class(self):
        a = Aftakking() # TODO change to AllCasesTestClass
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

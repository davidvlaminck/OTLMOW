import unittest

from OTLMOW.ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder


class OtlAssetJSONEncoderTests(unittest.TestCase):
    def test_isEmptyDict_EmptyDict(self):
        d = dict()
        encoder = OtlAssetJSONEncoder(indent=4)
        self.assertTrue(encoder.isEmptyDict(d))

    def test_isEmptyDict_NonEmptyDict(self):
        d = dict()
        d['1'] = '1'
        encoder = OtlAssetJSONEncoder(indent=4)
        self.assertFalse(encoder.isEmptyDict(d))

    def test_isEmptyDict_NonEmptyDictInDict(self):
        d = dict()
        d['1'] = {'1':'1'}
        encoder = OtlAssetJSONEncoder(indent=4)
        self.assertFalse(encoder.isEmptyDict(d))

    def test_isEmptyDict_EmptyDictInDict(self):
        d = dict()
        d['1'] = {}
        encoder = OtlAssetJSONEncoder(indent=4)
        self.assertTrue(encoder.isEmptyDict(d))

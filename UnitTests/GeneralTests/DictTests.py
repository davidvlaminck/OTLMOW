import unittest

from OTLMOW.ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder


class OtlAssetJSONEncoderTests(unittest.TestCase):
    def test_isEmptyDict_EmptyDict(self):
        d = dict()
        self.assertTrue(OtlAssetJSONEncoder.isEmptyDict(d))

    def test_isEmptyDict_NonEmptyDict(self):
        d = dict()
        d['1'] = '1'
        self.assertFalse(OtlAssetJSONEncoder.isEmptyDict(d))

    def test_isEmptyDict_NonEmptyDictInDict(self):
        d = dict()
        d['1'] = {'1':'1'}
        self.assertFalse(OtlAssetJSONEncoder.isEmptyDict(d))

    def test_isEmptyDict_EmptyDictInDict(self):
        d = dict()
        d['1'] = {}
        self.assertTrue(OtlAssetJSONEncoder.isEmptyDict(d))

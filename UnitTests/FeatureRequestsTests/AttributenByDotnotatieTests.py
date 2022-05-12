import unittest
from unittest import TestCase

from OTLMOW.OTLModel.Classes.Aftakking import Aftakking
from OTLMOW.OTLModel.Classes.Verkeersregelaar import Verkeersregelaar
from OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie


class AttributenByDotnotatieTests(TestCase):
    def test_attributes_by_dotnotatie_simple_attributes(self):
        a = Aftakking()
        a.toestand = 'in-gebruik'
        a.naam = 'aftakking'
        expected_result = {'naam': 'aftakking', 'toestand': 'in-gebruik'}
        result_dict = dict(a.attributes_by_dotnotatie())
        self.assertDictEqual(expected_result, result_dict)

    def test_attributes_by_dotnotatie_complex_attributes(self):
        a = Aftakking()
        a.assetId.identificator = 'eigen_id'
        a.assetId.toegekendDoor = 'AWV'
        expected_result = {
            'assetId.identificator': 'eigen_id',
            'assetId.toegekendDoor': 'AWV'}
        self.assertDictEqual(expected_result, dict(a.attributes_by_dotnotatie()))

    def test_attributes_by_dotnotatie_kwantitatieve_waarde(self):
        a = Aftakking()
        a.theoretischeLevensduur.waarde = 120
        expected_result = {
            'theoretischeLevensduur.waarde': 120}
        self.assertDictEqual(expected_result, dict(a.attributes_by_dotnotatie()))

    def test_attributes_by_dotnotatie_kard_meer_dan_1(self):
        v = Verkeersregelaar()
        v.coordinatiewijze = ["centraal", "pulsen"]
        d = dict(v.attributes_by_dotnotatie())
        expected = {
            'coordinatiewijze[0]': 'centraal',
            'coordinatiewijze[1]': 'pulsen'
        }
        self.assertDictEqual(expected, d)

    def test_attributes_by_dotnotatie_complex_kard_meer_dan_1(self):
        v = Verkeersregelaar()
        v.externeReferentie[0].externReferentienummer = "externe referentie 2"
        v.externeReferentie[0].externePartij = "bij externe partij 2"

        v._externeReferentie.add_empty_value()
        v.externeReferentie[1].externReferentienummer = "externe referentie 1"
        v.externeReferentie[1].externePartij = "bij externe partij 1"
        d = dict(v.attributes_by_dotnotatie())
        expected = {
            'externeReferentie[0].externReferentienummer': 'externe referentie 2',
            'externeReferentie[0].externePartij': 'bij externe partij 2',
            'externeReferentie[1].externReferentienummer': 'externe referentie 1',
            'externeReferentie[1].externePartij': 'bij externe partij 1'}
        self.assertDictEqual(expected, d)

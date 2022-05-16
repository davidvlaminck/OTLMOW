import os
import unittest

from OTLMOW.Facility.CsvImporter import CsvImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.Verkeersregelaar import Verkeersregelaar

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class CsvImporterTests(unittest.TestCase):
    def test_init_importer_only_load_with_settings(self):
        otl_facility = OTLFacility(None, settings_path='C:\\resources\\settings_OTLMOW.json')

        with self.subTest('load with correct settings'):
            importer = CsvImporter(settings=otl_facility.settings)
            self.assertIsNotNone(importer)

        with self.subTest('load without settings'):
            with self.assertRaises(ValueError):
                CsvImporter(settings=None)

        with self.subTest('load with incorrect settings (no file_formats)'):
            with self.assertRaises(ValueError):
                CsvImporter(settings={"auth_options": [{}]})

        with self.subTest('load with incorrect settings (file_formats but no csv)'):
            with self.assertRaises(ValueError):
                CsvImporter(settings={"file_formats": [{}]})

    def test_load_test_file(self):
        otl_facility = OTLFacility(None, settings_path='C:\\resources\\settings_OTLMOW.json')
        importer = CsvImporter(settings=otl_facility.settings)
        file_location = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'test_file_VR.csv'))
        objects = importer.import_csv_file(file_location)
        self.assertEqual(354, len(importer.data))
        self.assertEqual(34, len(importer.headers))

    def test_create_objects_from_data(self):
        otl_facility = OTLFacility(None, settings_path='C:\\resources\\settings_OTLMOW.json')
        importer = CsvImporter(settings=otl_facility.settings)
        datastring = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar;1433df2f-5dc8-467b-94f4-efceb4581c68-b25kZXJkZWVsI1ZlcmtlZXJzcmVnZWxhYXI;AWV;;;;centraal|klok;2021-06-09;;;;802C5;MACQ;true;aansluit_802C5.pdf;application-pdf;/eminfra/core/api/otl/assets/1433df2f-5dc8-467b-94f4-efceb4581c68-b25kZXJkZWVsI1ZlcmtlZXJzcmVnZWxhYXI/documenten/ed288304-0f02-479f-af74-28d2fc55e5fe;;;civa-2020;;ccol;;;;;;;240.0;in-gebruik;42;2020-10-09;V016027v06;POINT Z (146955.19 181631.1 59.17)'
        importer.data = [datastring.split(';')]
        headerstring = 'typeURI;assetId.identificator;assetId.toegekendDoor;bron.typeURI;bronAssetId.identificator;bronAssetId.toegekendDoor;coordinatiewijze[];datumOprichtingObject;doel.typeURI;doelAssetId.identificator;doelAssetId.toegekendDoor;externeReferentie[].externReferentienummer;externeReferentie[].externePartij;isActief;kabelaansluitschema.bestandsnaam;kabelaansluitschema.mimeType;kabelaansluitschema.uri;merk;modelnaam;naam;notitie;programmeertool;regelaartype;rol;standaardBestekPostNummer[];technischeDocumentatie.bestandsnaam;technischeDocumentatie.mimeType;technischeDocumentatie.uri;theoretischeLevensduur;toestand;voltageLampen;vplanDatum;vplanNummer;geometry'
        importer.headers = headerstring.split(';')

        self.assertEqual(1, len(importer.data))
        self.assertEqual(34, len(importer.headers))

        objects = importer.create_objects_from_data()

        self.assertTrue(isinstance(objects, list))
        self.assertEqual(1, len(objects))
        self.assertTrue(isinstance(objects[0], Verkeersregelaar))


import os
import unittest

from OTLMOW.Facility.FileFormats.CsvImporter import CsvImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.Onderdeel.Verkeersregelaar import Verkeersregelaar

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class CsvImporterTests(unittest.TestCase):
    def test_init_importer_only_load_with_settings(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        settings_file_location = f'{base_dir}/../../settings_OTLMOW.json'
        otl_facility = OTLFacility(logfile='', settings_path=settings_file_location)

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

    def test_load_test_file_multiple_types(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        settings_file_location = f'{base_dir}/../../settings_OTLMOW.json'
        file_location = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'export_multiple_types.csv'))
        otl_facility = OTLFacility(logfile='', settings_path=settings_file_location)
        objects = otl_facility.create_assets_from_file(file_location)

        self.assertEqual(15, len(objects))

    def test_load_test_file(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        settings_file_location = f'{base_dir}/../../settings_OTLMOW.json'
        otl_facility = OTLFacility(logfile='', settings_path=settings_file_location)
        importer = CsvImporter(settings=otl_facility.settings)
        file_location = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'test_file_VR.csv'))
        importer.import_file(file_location)
        self.assertEqual(187, len(importer.data))
        self.assertEqual(27, len(importer.headers))

    def test_create_objects_from_data(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        settings_file_location = f'{base_dir}/../../settings_OTLMOW.json'
        otl_facility = OTLFacility(logfile='', settings_path=settings_file_location)
        importer = CsvImporter(settings=otl_facility.settings)
        datastring = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar;1433df2f-5dc8-467b-94f4-efceb4581c68-b25kZXJkZWVsI1ZlcmtlZXJzcmVnZWxhYXI;AWV;;;;centraal|klok;2021-06-09;;;;802C5;MACQ;true;aansluit_802C5.pdf;application-pdf;/eminfra/core/api/otl/assets/1433df2f-5dc8-467b-94f4-efceb4581c68-b25kZXJkZWVsI1ZlcmtlZXJzcmVnZWxhYXI/documenten/ed288304-0f02-479f-af74-28d2fc55e5fe;;;civa-2020;;ccol;;;;;;;240.0;in-gebruik;42;2020-10-09;V016027v06;POINT Z (146955.19 181631.1 59.17)'
        datastring2 = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar;176c849f-f386-4a07-9493-cb5100ba9830-b25kZXJkZWVsI1ZlcmtlZXJzcmVnZWxhYXI;AWV;;;;klok;2022-02-19;;;;605C7|605C7;MACQ | TRAFIROAD;true;V15.816_v11_605C7.pdf;application-pdf;https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.kabelaansluitschema;yunex;sx;;;StrideTT;type-1;;;V15.816_v11_605C7.pdf;application-pdf;https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.technischeDocumentatie;240.0;in-gebruik;42;2021-09-16;V015816v11;POINT Z (145670.97 164665.43 21)'
        importer.data = [datastring.split(';'), datastring2.split(';')]
        headerstring = 'typeURI;assetId.identificator;assetId.toegekendDoor;bron.typeURI;bronAssetId.identificator;bronAssetId.toegekendDoor;coordinatiewijze[];datumOprichtingObject;doel.typeURI;doelAssetId.identificator;doelAssetId.toegekendDoor;externeReferentie[].externReferentienummer;externeReferentie[].externePartij;isActief;kabelaansluitschema.bestandsnaam;kabelaansluitschema.mimeType;kabelaansluitschema.uri;merk;modelnaam;naam;notitie;programmeertool;regelaartype;rol;standaardBestekPostNummer[];technischeDocumentatie.bestandsnaam;technischeDocumentatie.mimeType;technischeDocumentatie.uri;theoretischeLevensduur;toestand;voltageLampen;vplanDatum;vplanNummer;geometry'
        importer.headers = headerstring.split(';')

        self.assertEqual(2, len(importer.data))
        self.assertEqual(34, len(importer.headers))

        objects = importer.create_objects_from_data()

        self.assertTrue(isinstance(objects, list))
        self.assertEqual(2, len(objects))
        self.assertTrue(isinstance(objects[0], Verkeersregelaar))
        self.assertEqual('centraal', objects[0].coordinatiewijze[0])
        self.assertEqual('klok', objects[0].coordinatiewijze[1])
        self.assertEqual('605C7', objects[1].externeReferentie[0].externReferentienummer)
        self.assertEqual('605C7', objects[1].externeReferentie[1].externReferentienummer)
        self.assertEqual('MACQ ', objects[1].externeReferentie[0].externePartij)
        self.assertEqual(' TRAFIROAD', objects[1].externeReferentie[1].externePartij)

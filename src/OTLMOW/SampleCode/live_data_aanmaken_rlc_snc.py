from datetime import datetime

from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.Bevestiging import Bevestiging
from OTLMOW.OTLModel.Classes.Flitsgroep import Flitsgroep
from OTLMOW.OTLModel.Classes.Flitspaalbehuizing import Flitspaalbehuizing
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Laagspanningsbord import Laagspanningsbord
from OTLMOW.OTLModel.Classes.Stroomkring import Stroomkring
from OTLMOW.OTLModel.Classes.Voedt import Voedt
from OTLMOW.OTLModel.Classes.Wegkantkast import Wegkantkast

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    # add EM-Infra assets through API
    input_uuids = ['6fec1fbf-9037-4daa-976d-4ccd54e2d554', '1c6dbec3-62e6-4e30-8fe1-19ba58a73151',
                   'e88f3270-91ed-4fa8-a605-0969805790d4', 'adbd8726-d026-4c5d-80e1-5343a2fa4d34',
                   '60b2dcaa-69f1-4fac-9062-9c1381eecd2e', '85ab7233-4d69-4702-841e-aace94b42410',
                   'f63bfc00-2951-401e-8dbb-6667a479e0ea']

    cert_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.crt'
    key_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.key'
    importer = EMInfraImporter(cert_path=cert_path, key_path=key_path)

    # fetch assets, based on a list of uuids
    assets = importer.import_assets_from_webservice_by_uuids(input_uuids)

    # for each asset, find all relations
    relatie_list = []
    for asset in assets:
        relaties = importer.import_assetrelaties_from_webservice_by_assetuuid(asset.assetId.identificator[0:36])
        relatie_list.extend(relaties)

    assets.extend(relatie_list)

    # use the generated datamodel to create instances of OTL classes
    flitspaalbehuizing1 = Flitspaalbehuizing()
    flitspaalbehuizing1.naam = '360C6.1'
    flitspaalbehuizing1.toestand = 'in-gebruik'
    flitspaalbehuizing1.assetId.identificator = '360C6.1'
    flitspaalbehuizing1.geometry = 'POINT Z (171277.9 173790.9 0)'

    flitsgroep = Flitsgroep()
    flitsgroep.naam = '360C6'
    flitsgroep.assetId.identificator = '360C6'
    flitsgroep.toestand = 'in-gebruik'
    flitsgroep.isRoodLicht = True
    flitsgroep.externeReferentie.externReferentienummer = 'https://bmidata.drive-it.be/sites/sites/321'
    flitsgroep.externeReferentie.externePartij = 'Belgisch Meet Instituut'

    hoortbijrelatie_beh_1 = HoortBij()
    hoortbijrelatie_beh_1.assetId.identificator = "360C6-360C6.1"
    hoortbijrelatie_beh_1.bronAssetId.identificator = '360C6.1'
    hoortbijrelatie_beh_1.doelAssetId.identificator = '360C6'

    # TODO: copy paste flitspaalbehuizing1 + hoortbij

    # voorbeeld SNC 'R23X3.8/421C6/1'
    flitspaalbehuizing3 = Flitspaalbehuizing()
    flitspaalbehuizing3.naam = '421C6.1'
    flitspaalbehuizing3.toestand = 'in-gebruik'
    flitspaalbehuizing3.assetId.identificator = '421C6.1'
    flitspaalbehuizing3.geometry = 'POINT Z (173600.1 173138.6 0)'

    hoortbijrelatie_beh_3_legacy = HoortBij()
    hoortbijrelatie_beh_3_legacy.assetId.identificator = '421C6.1-legacy'
    hoortbijrelatie_beh_3_legacy.bronAssetId.identificator = '421C6.1'
    hoortbijrelatie_beh_3_legacy.doelAssetId.identificator = importer.get_asset_id_from_uuid_and_typeURI(
        '1c6dbec3-62e6-4e30-8fe1-19ba58a73151', 'https://lgc.data.wegenenverkeer.be/ns/installatie#SNCPaal')

    flitsgroep2 = Flitsgroep()
    flitsgroep2.naam = '421C6'
    flitsgroep2.assetId.identificator = '421C6'
    flitsgroep2.toestand = 'in-gebruik'
    flitsgroep2.isRoodLicht = False

    hoortbijrelatie_flitsgroep2_legacy = HoortBij()
    hoortbijrelatie_flitsgroep2_legacy.assetId.identificator = '421C6-legacy'
    hoortbijrelatie_flitsgroep2_legacy.bronAssetId.identificator = '421C6'
    hoortbijrelatie_flitsgroep2_legacy.doelAssetId.identificator = importer.get_asset_id_from_uuid_and_typeURI(
        '6fec1fbf-9037-4daa-976d-4ccd54e2d554', 'https://lgc.data.wegenenverkeer.be/ns/installatie#SNC')

    hoortbijrelatie_beh_3 = HoortBij()
    hoortbijrelatie_beh_3.assetId.identificator = '421C6-421C6.1'
    hoortbijrelatie_beh_3.bronAssetId.identificator = '421C6.1'
    hoortbijrelatie_beh_3.doelAssetId.identificator = '421C6'

    str = Stroomkring()
    str.assetId.identificator = '421C6-str'

    hoortbijrelatie_str_legacy = HoortBij()
    hoortbijrelatie_str_legacy.assetId.identificator = '421C6-str-legacy'
    hoortbijrelatie_str_legacy.bronAssetId.identificator = '421C6-str'
    hoortbijrelatie_str_legacy.doelAssetId.identificator = importer.get_asset_id_from_uuid_and_typeURI(
        'adbd8726-d026-4c5d-80e1-5343a2fa4d34', 'https://lgc.data.wegenenverkeer.be/ns/installatie#LSDeel')

    voedingsrelatie_str_fp = Voedt()
    voedingsrelatie_str_fp.assetId.identificator = "421C6.1-421C6-str"
    voedingsrelatie_str_fp.bronAssetId.identificator = '421C6-str'
    voedingsrelatie_str_fp.doelAssetId.identificator = '421C6.1'

    lsb = Laagspanningsbord()
    lsb.assetId.identificator = '421C6-lsb'

    hoortbijrelatie_lsb_legacy = HoortBij()
    hoortbijrelatie_lsb_legacy.assetId.identificator = '421C6-lsb-legacy'
    hoortbijrelatie_lsb_legacy.bronAssetId.identificator = '421C6-lsb'
    hoortbijrelatie_lsb_legacy.doelAssetId.identificator = importer.get_asset_id_from_uuid_and_typeURI(
        'adbd8726-d026-4c5d-80e1-5343a2fa4d34', 'https://lgc.data.wegenenverkeer.be/ns/installatie#LSDeel')

    bevestigingsrelatie_str_lsb = Bevestiging()
    bevestigingsrelatie_str_lsb.assetId.identificator = "421C6-lsb-421C6-str"
    bevestigingsrelatie_str_lsb.bronAssetId.identificator = '421C6-lsb'
    bevestigingsrelatie_str_lsb.doelAssetId.identificator = '421C6-str'

    bevestigingsrelatie_meter_lsb = Bevestiging()
    bevestigingsrelatie_meter_lsb.assetId.identificator = "421C6-lsb-3013974"
    bevestigingsrelatie_meter_lsb.bronAssetId.identificator = '421C6-lsb'
    bevestigingsrelatie_meter_lsb.doelAssetId.identificator = importer.get_asset_id_from_uuid_and_typeURI(
        '85ab7233-4d69-4702-841e-aace94b42410', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB')

    kast = Wegkantkast()
    kast.naam = 'R23N3.85.K'
    kast.assetId.identificator = 'R23N3.85.K'

    bevestigingsrelatie_aansluiting_kast = Bevestiging()  # TODO
    bevestigingsrelatie_aansluiting_kast.assetId.identificator = "R23N3.85.K-aansluiting"
    bevestigingsrelatie_aansluiting_kast.bronAssetId.identificator = 'R23N3.85.K'
    bevestigingsrelatie_aansluiting_kast.doelAssetId.identificator = importer.get_asset_id_from_uuid_and_typeURI(
        'f63bfc00-2951-401e-8dbb-6667a479e0ea', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning')

    bevestigingsrelatie_kast_lsb = Bevestiging()
    bevestigingsrelatie_kast_lsb.assetId.identificator = "421C6-lsb-R23N3.85.K"
    bevestigingsrelatie_kast_lsb.bronAssetId.identificator = '421C6-lsb'
    bevestigingsrelatie_kast_lsb.doelAssetId.identificator = 'R23N3.85.K'

    hoortbijrelatie_kast_legacy = HoortBij()
    hoortbijrelatie_kast_legacy.assetId.identificator = 'R23N3.85.K-legacy'
    hoortbijrelatie_kast_legacy.bronAssetId.identificator = 'R23N3.85.K'
    hoortbijrelatie_kast_legacy.doelAssetId.identificator = importer.get_asset_id_from_uuid_and_typeURI(
        'e88f3270-91ed-4fa8-a605-0969805790d4', 'https://lgc.data.wegenenverkeer.be/ns/installatie#Kast')

    # energiemeter
    voedingsrelatie_str_meter = Voedt()
    voedingsrelatie_str_meter.assetId.identificator = "3013974-421C6-str"
    voedingsrelatie_str_meter.bronAssetId.identificator = importer.get_asset_id_from_uuid_and_typeURI(
        '85ab7233-4d69-4702-841e-aace94b42410', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB')
    voedingsrelatie_str_meter.doelAssetId.identificator = '421C6-str'

    lijst_otl_objecten = [flitspaalbehuizing1, flitsgroep, hoortbijrelatie_beh_1, flitspaalbehuizing3, flitsgroep2,
                          hoortbijrelatie_beh_3, str, voedingsrelatie_str_fp, lsb, bevestigingsrelatie_str_lsb, kast,
                          bevestigingsrelatie_kast_lsb, hoortbijrelatie_beh_3_legacy, hoortbijrelatie_flitsgroep2_legacy,
                          hoortbijrelatie_str_legacy, hoortbijrelatie_lsb_legacy, hoortbijrelatie_kast_legacy,
                          voedingsrelatie_str_meter, bevestigingsrelatie_aansluiting_kast, bevestigingsrelatie_meter_lsb]

    # encode to a json representation
    encoded_json = otl_facility.encoder.encode(lijst_otl_objecten)
    print(encoded_json)

    # write the json file
    filepath = f'Output/{datetime.now().strftime("%Y%m%d%H%M%S")}_export.json'
    otl_facility.encoder.write_json_to_file(encoded_json, filepath)

    lijst_otl_objecten.extend(assets)

    otl_facility.visualiser.show(lijst_otl_objecten)

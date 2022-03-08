from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.Daalpaal import Daalpaal
from OTLMOW.OTLModel.Classes.Flitsgroep import Flitsgroep
from OTLMOW.OTLModel.Classes.Flitspaalbehuizing import Flitspaalbehuizing
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Laagspanningsbord import Laagspanningsbord
from OTLMOW.OTLModel.Classes.PunctueleVerlichtingsmast import PunctueleVerlichtingsmast
from OTLMOW.OTLModel.Classes.Stroomkring import Stroomkring
from OTLMOW.OTLModel.Classes.Voedt import Voedt

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    # add EM-Infra assets through API
    input_uuids = []

    cert_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.crt'
    key_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.key'
    importer = EMInfraImporter(cert_path=cert_path, key_path=key_path)

    # fetch assets, based on a list of uuids
    assets = importer.import_assets_from_webservice_by_uuids(input_uuids)

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
    #flitsgroep.externeReferentie.externReferentienummer = 'https://bmidata.drive-it.be/sites/sites/321'
    #flitsgroep.externeReferentie.externePartij = 'Belgisch Meet Instituut'

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

    flitsgroep2 = Flitsgroep()
    flitsgroep2.naam = '421C6'
    flitsgroep2.assetId.identificator = '421C6'
    flitsgroep2.toestand = 'in-gebruik'
    flitsgroep2.isRoodLicht = False

    hoortbijrelatie_beh_3 = HoortBij()
    hoortbijrelatie_beh_3.assetId.identificator = '421C6-421C6.1'
    hoortbijrelatie_beh_3.bronAssetId.identificator = '421C6.1'
    hoortbijrelatie_beh_3.doelAssetId.identificator = '421C6'

    str = Stroomkring()
    str.assetId.identificator = '421C6-str'

    voedingsrelatie_str_fp = Voedt()
    voedingsrelatie_str_fp.assetId.identificator = "421C6.1-421C6-str"
    voedingsrelatie_str_fp.bronAssetId.identificator = '421C6-str'
    voedingsrelatie_str_fp.doelAssetId.identificator = '421C6.1'

    lsb = Laagspanningsbord() # mee deel van LSDEEL
    lsb.assetId.identificator = '421C6-lsb'



    # lsb > bev > stroomkring
    # wegkantkast > bev > lsb



    lijst_otl_objecten = [flitspaalbehuizing1, flitsgroep, hoortbijrelatie_beh_1, flitspaalbehuizing3, flitsgroep2, hoortbijrelatie_beh_3, str, voedingsrelatie_str_fp, lsb]
    lijst_otl_objecten.extend(assets)

    otl_facility.visualiser.show(lijst_otl_objecten)



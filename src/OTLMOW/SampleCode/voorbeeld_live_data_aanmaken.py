from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.PunctueleVerlichtingsmast import PunctueleVerlichtingsmast
from OTLMOW.OTLModel.Classes.Voedt import Voedt

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    # add EM-Infra assets through API
    input_uuids = ['eb45c3a5-2bf9-4c56-b665-2a7dafb6b709']

    cert_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.crt'
    key_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.key'
    importer = EMInfraImporter(cert_path=cert_path, key_path=key_path)

    # fetch assets, based on a list of uuids
    assets = importer.import_assets_from_webservice_by_uuids(input_uuids)

    # use the generated datamodel to create instances of OTL classes
    mast = PunctueleVerlichtingsmast()
    mast.naam = 'A0024'
    mast.toestand = 'in-gebruik'
    # dnb.toestand = 'foute toestand'  # raises ValueError
    mast.assetId.identificator = 'eigen_Id_voor_A0024'

    voedingsrelatie = Voedt()
    voedingsrelatie.assetId.identificator = "A0024-50004784"
    voedingsrelatie.bronAssetId.identificator = 'eigen_Id_voor_A0024'
    voedingsrelatie.doelAssetId.identificator = 'eigen_Id_voor_50004784'

    lijst_otl_objecten = [mast, voedingsrelatie]
    lijst_otl_objecten.extend(assets)

    otl_facility.visualiser.show(lijst_otl_objecten)



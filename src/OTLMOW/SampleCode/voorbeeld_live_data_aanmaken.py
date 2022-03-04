from datetime import datetime

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

    otl_facility.visualiser.show(lijst_otl_objecten)



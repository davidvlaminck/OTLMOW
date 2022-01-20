from datetime import datetime

from Facility.OTLFacility import OTLFacility
from Loggers.ConsoleLogger import ConsoleLogger
from Loggers.LoggerCollection import LoggerCollection
from Loggers.TxtLogger import TxtLogger
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLModel.Classes.DNBLaagspanning import DNBLaagspanning
from OTLModel.Classes.EnergiemeterDNB import EnergiemeterDNB
from OTLModel.Classes.Voedt import Voedt

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    # use the generated datamodel to create instances of OTL classes
    dnb = DNBLaagspanning()
    dnb.naam = 'A0024'
    # dnb.naam = 24  # this raises a TypeError because it has an incorrect value
    dnb.toestand = 'in-gebruik'
    dnb.assetId.identificator = 'eigen_Id_voor_A0024'
    dnb.eanNummer = '541448860003995215'
    dnb.adresVolgensDNB.gemeente = 'brasschaat'
    # dnb.adresVolgensDNB.gemeente = 'Brasschaat'  # this raises a ValueError because it has an incorrect value
    dnb.adresVolgensDNB.postcode = '2930'
    dnb.adresVolgensDNB.straatnaam = 'Bredabaan 90'

    meter = EnergiemeterDNB()
    meter.naam = '50004784'
    meter.assetId.identificator = 'eigen_Id_voor_50004784'
    meter.aantalTelwerken = 1
    meter.geometry = 'POINT Z(157696.6 219065.5 0)'

    voedingsrelatie = Voedt()
    voedingsrelatie.assetId.identificator = "A0024-50004784"
    voedingsrelatie.bronAssetId.identificator = 'eigen_Id_voor_A0024'
    voedingsrelatie.doelAssetId.identificator = 'eigen_Id_voor_50004784'

    lijst_otl_objecten = [dnb, meter, voedingsrelatie]

    otl_facility.visualiser.show(lijst_otl_objecten)

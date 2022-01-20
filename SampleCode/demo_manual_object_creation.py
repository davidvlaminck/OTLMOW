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
    dnb.naam.waarde = 'A0024'
    # dnb.naam.waarde = 24  # this raises a ValueError because it has an incorrect value
    dnb.toestand.set_value_by_label('in gebruik')
    dnb.assetId.identificator.waarde = 'eigen_Id_voor_A0024'
    dnb.eanNummer.waarde = '541448860003995215'
    dnb.adresVolgensDNB.gemeente.set_value_by_label('brasschaat')
    # dnb.adresVolgensDNB.gemeente.set_value_by_label('Brasschaat')  # this raises a ValueError because it has an incorrect value
    dnb.adresVolgensDNB.postcode.waarde = '2930'
    dnb.adresVolgensDNB.straatnaam.waarde = 'Bredabaan 90'

    meter = EnergiemeterDNB()
    meter.naam = '50004784'
    meter.assetId.identificator.waarde = 'eigen_Id_voor_50004784'
    meter.aantalTelwerken.waarde = 1
    meter.geometry = 'POINT Z(157696.6 219065.5 0)'

    voedingsrelatie = Voedt()
    voedingsrelatie.assetId.identificator.waarde = "A0024-50004784"
    voedingsrelatie.bronAssetId.identificator.waarde = 'eigen_Id_voor_A0024'
    voedingsrelatie.doelAssetId.identificator.waarde = 'eigen_Id_voor_50004784'

    lijst_otl_objecten = [dnb, meter, voedingsrelatie]

    # encode to a json representation
    encoded_json = otl_facility.encoder.encode(lijst_otl_objecten)
    print(encoded_json)

    # write the json file
    path = f'{datetime.now().strftime("%Y%m%d%H%M%S")}_export.json'
    otl_facility.encoder.write_json_to_file(encoded_json, path)

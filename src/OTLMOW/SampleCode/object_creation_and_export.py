from datetime import datetime

from OTLMOW.ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from src.OTLMOW.Facility.OTLFacility import OTLFacility
from src.OTLMOW.OTLModel.Classes.Onderdeel.DNBLaagspanning import DNBLaagspanning
from src.OTLMOW.OTLModel.Classes.Onderdeel.EnergiemeterDNB import EnergiemeterDNB
from src.OTLMOW.OTLModel.Classes.Onderdeel.Voedt import Voedt


if __name__ == '__main__':
    # create the main facade class: OTLFacility
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\python_log.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    # use the generated datamodel to create instances of OTL classes
    dnb = DNBLaagspanning()
    dnb.naam = 'A0024'
    dnb.toestand = 'in-gebruik'
    dnb.assetId.identificator = 'eigen_Id_voor_A0024'
    dnb.eanNummer = '541448860003995215'
    dnb.adresVolgensDNB.gemeente = 'brasschaat'
    dnb.adresVolgensDNB.postcode = '2930'
    dnb.adresVolgensDNB.straatnaam = 'Bredabaan 90'
    # dnb.toestand = 'foute toestand'  # wouls raise ValueError because the value is not valid

    meter = EnergiemeterDNB()
    meter.naam = '50004784'
    meter.assetId.identificator = 'eigen_Id_voor_50004784'
    meter.aantalTelwerken = 1
    meter.geometry = 'POINT Z (157696.6 219065.5 0)'

    voedingsrelatie = Voedt()
    voedingsrelatie.assetId.identificator = "A0024-50004784"
    voedingsrelatie.bronAssetId.identificator = 'eigen_Id_voor_A0024'
    voedingsrelatie.doelAssetId.identificator = 'eigen_Id_voor_50004784'

    lijst_otl_objecten = [dnb, meter, voedingsrelatie]

    # (OPTIONAL) encode to a json representation
    encoder = OtlAssetJSONEncoder(indent=4, settings=otl_facility.settings)
    encoded_json = encoder.encode(lijst_otl_objecten)
    print(encoded_json)

    # write the json file
    path = f'{datetime.now().strftime("%Y%m%d%H%M%S")}_export.json'
    otl_facility.create_file_from_assets(list_of_objects=lijst_otl_objecten, filepath=path)

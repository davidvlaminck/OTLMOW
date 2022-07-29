from datetime import datetime

from OTLMOW.Facility.FileFormats.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.Facility.Visualiser import Visualiser
from OTLMOW.OTLModel.Classes.Onderdeel.DNBLaagspanning import DNBLaagspanning
from OTLMOW.OTLModel.Classes.Onderdeel.EnergiemeterDNB import EnergiemeterDNB
from OTLMOW.OTLModel.Classes.Onderdeel.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Onderdeel.Voedt import Voedt

if __name__ == '__main__':
    # otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\python_log.txt',
    #                            settings_path="C:\\resources\\settings_OTLMOW.json")
    otl_facility = OTLFacility(logfile='/home/davidlinux/Documents/AWV/python_log.txt',
                               settings_path="/home/davidlinux/Documents/AWV/resources/settings_OTLMOW.json")

    # use the generated datamodel to create instances of OTL classes
    dnb = DNBLaagspanning()
    dnb.naam = 'A0024'
    dnb.toestand = 'in-gebruik'
    # dnb.toestand = 'foute toestand'  # raises ValueError
    dnb.assetId.identificator = 'eigen_Id_voor_A0024'
    dnb.eanNummer = '541448860003995215'
    dnb.adresVolgensDNB.gemeente = 'brasschaat'
    dnb.adresVolgensDNB.postcode = '2930'
    dnb.adresVolgensDNB.straatnaam = 'Bredabaan 90'

    meter = EnergiemeterDNB()
    meter.naam = '50004784'
    meter.assetId.identificator = 'eigen_Id_voor_50004784'
    meter.aantalTelwerken = 1
    meter.geometry = 'POINT Z (157696.6 219065.5 0)'

    voedingsrelatie = Voedt()
    voedingsrelatie.assetId.identificator = "A0024-50004784"
    voedingsrelatie.bronAssetId.identificator = 'eigen_Id_voor_A0024'
    voedingsrelatie.doelAssetId.identificator = 'eigen_Id_voor_50004784'

    requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')
    importer = EMInfraImporter(requester=requester)
    asset_id = importer.get_asset_id_from_uuid_and_typeURI(uuid='43e9c946-ca49-44b3-8ce3-46de0ec12489', typeURI='https://lgc.data.wegenenverkeer.be/ns/installatie#LS')
    ls = importer.import_asset_from_webservice_by_asset_id(asset_id)

    hoortBijrelatie1 = HoortBij()
    hoortBijrelatie1.assetId.identificator = "A0024-LS"
    hoortBijrelatie1.bronAssetId.identificator = dnb.assetId.identificator
    hoortBijrelatie1.doelAssetId.identificator = ls.assetId.identificator

    hoortBijrelatie2 = HoortBij()
    hoortBijrelatie2.assetId.identificator = "50004784-LS"
    hoortBijrelatie2.bronAssetId.identificator = meter.assetId.identificator
    hoortBijrelatie2.doelAssetId.identificator = ls.assetId.identificator

    lijst_otl_objecten = [dnb, meter, voedingsrelatie, ls, hoortBijrelatie1, hoortBijrelatie2]

    # export as json file
    filepath = f'Output/{datetime.now().strftime("%Y%m%d%H%M%S")}_export.json'
    otl_facility.create_file_from_assets(list_of_objects=lijst_otl_objecten, filepath=filepath)

    Visualiser().show(lijst_otl_objecten)

from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLMOW.OTLModel.Classes.Onderdeel.DNBLaagspanning import DNBLaagspanning
from OTLMOW.OTLModel.Classes.Onderdeel.EnergiemeterDNB import EnergiemeterDNB
from OTLMOW.OTLModel.Classes.Onderdeel.Voedt import Voedt

if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\python_log.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    # use the generated datamodel to create instances of OTL classes
    dnb = DNBLaagspanning()
    dnb.naam = 'A0024'
    # dnb.naam.waarde = 24  # this raises a ValueError because it has an incorrect value
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
    meter.geometry = 'POINT Z (157696.6 219065.5 0)'

    voedingsrelatie = Voedt()
    voedingsrelatie.assetId.identificator = "A0024-50004784"
    voedingsrelatie.bronAssetId.identificator = 'eigen_Id_voor_A0024'
    voedingsrelatie.doelAssetId.identificator = 'eigen_Id_voor_50004784'

    lijst_otl_objecten = [dnb, meter, voedingsrelatie]

    # using facility's designated validator
    print(otl_facility.relatie_validator.validateRelatieByURI(dnb, meter, Voedt))
    # outputs True

    # using methods on the object itself
    dnb._loadGeldigeRelaties()
    print(dnb._validateRelatiePossible(meter, Voedt, relatieRichting=RelatieRichting.BRON_DOEL))
    # also outputs True

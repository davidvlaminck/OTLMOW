from datetime import datetime
import normalisatieExoten
from Facility.EMInfraDecoder import EMInfraDecoder
from Facility.EMInfraImporter import EMInfraImporter

from Facility.OTLFacility import OTLFacility
from Loggers.ConsoleLogger import ConsoleLogger
from Loggers.LoggerCollection import LoggerCollection
from Loggers.TxtLogger import TxtLogger
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLModel.Classes.DNBLaagspanning import DNBLaagspanning
from OTLModel.Classes.EnergiemeterDNB import EnergiemeterDNB
from OTLModel.Classes.Voedt import Voedt

class Bar(object):
    def __init__(self):
        self.value = ''

    def __get__(self, instance, owner):
        print("returned from descriptor object")
        return self.value

    def __set__(self, instance, value):
        print("set in descriptor object")
        self.value = value

    def __delete__(self, instance):
        print("deleted in descriptor object")
        del self.value

class Foo(object):
    bar = Bar()

if __name__ == '__main__':
    f = Foo()
    f.bar = 10
    print(f.bar)
    del f.bar



    # create the main facade class: OTLFacility
    logger = TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt')
    otl_facility = OTLFacility(LoggerCollection([logger, ConsoleLogger()]))

    # create a datamodel based on the OTL SQLite database and ttl files stored on the github
    otl_file_location = 'InputFiles/OTL.db'
    otl_facility.init_otl_model_creator(otl_file_location)
    otl_facility.create_otl_datamodel()

    # ===========================================================================================================================
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

    # ===========================================================================================================================
    # validation for relations is possible, either on the object itself or through the validator

    # validation from a concrete object
    print(dnb._validateRelatiePossible(meter, Voedt, relatieRichting=RelatieRichting.BRON_DOEL))
    # outputs True

    # using facility's designated validator
    print(otl_facility.relatieValidator.validateRelatieByURI(dnb, meter, Voedt))
    # also outputs True
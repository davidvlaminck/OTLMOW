from datetime import datetime

from Facility.OTLFacility import OTLFacility
from Loggers.TxtLogger import TxtLogger
from OTLModel.Classes.DNBLaagspanning import DNBLaagspanning
from OTLModel.Classes.EnergiemeterDNB import EnergiemeterDNB
from OTLModel.Classes.Voedt import Voedt

if __name__ == '__main__':
    # create the main facade class: OTLFacility
    logger = TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt')
    otl_facility = OTLFacility(logger)

    # create a datamodel based on the OTL SQLite database and ttl files stored on the github
    otl_file_location = 'InputFiles/OTL.db'
    otl_facility.init_otl_model_creator(otl_file_location)
    #otl_facility.create_otl_datamodel()

    # use the generated datamodel to create instances of OTL classes
    dnb = DNBLaagspanning()
    dnb.naam.waarde = 'A0024'
    #dnb.naam.waarde = 24  # this raises a ValueError because it has an incorrect value
    dnb.toestand.set_value_by_label('in gebruik')
    dnb.assetId.identificator.waarde = 'eigen_Id_voor_A0024'
    dnb.eanNummer.waarde = '541448860003995215'
    dnb.adresVolgensDNB.gemeente.set_value_by_label('brasschaat')
    # dnb.adresVolgensDNB.gemeente.set_value_by_label('Brasschaat')  # this raises a ValueError because it has an incorrect value
    dnb.adresVolgensDNB.postcode.waarde = '2930'
    dnb.adresVolgensDNB.straatnaam.waarde = 'Bredabaan 90'

    meter = EnergiemeterDNB()
    meter.naam = '1234567'
    meter.assetId.identificator.waarde = 'eigen_Id_voor_1234567'
    meter.metertype.set_value_by_invulwaarde('mechanisch')

    v = Voedt()
    v.assetId.identificator.waarde = "A0024-1234567"
    v.bronAssetId.identificator.waarde = 'eigen_Id_voor_A0024'
    v.doelAssetId.identificator.waarde = 'eigen_Id_voor_1234567'

    # encode to a json representation
    encoded_json = otl_facility.encoder.encode([dnb, meter, v])
    print(encoded_json)

    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%Y%m%d%H%M%S")
    f = open(f"{timestampStr}_export.json", "w")
    f.write(encoded_json)
    f.close()

    #r = RelatieValidator(GeldigeRelatieLijst())
    #dnb._validateRelatiePossible(meter, Voedt, relatieRichting=RelatieRichting.BRON_DOEL)
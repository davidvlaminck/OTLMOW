from csv import reader

from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.Camera import Camera
from OTLMOW.OTLModel.Classes.Netwerkelement import Netwerkelement
from OTLMOW.OTLModel.Classes.Netwerkpoort import Netwerkpoort
from OTLMOW.OTLModel.Classes.Sturing import Sturing

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    uuid_file_path = 'C:\\resources\\202204291039_netwerkelementen_locatie_van_IP.csv'

    lijst_objecten = []
    with open(uuid_file_path, 'r') as uuidfile:
        csv_reader = reader(uuidfile, delimiter='\t')
        for row in csv_reader:
            if row[0] == 'uuid':
                continue

            netwerkElement = Netwerkelement()
            netwerkElement.assetId.identificator = EMInfraImporter.get_asset_id_from_uuid_and_typeURI(row[0], Netwerkelement.typeURI)
            netwerkElement.assetId.toegekendDoor = 'AWV'
            netwerkElement.geometry = row[1].replace('POINT (', 'POINT Z (').replace(')', ' 0)')
            lijst_objecten.append(netwerkElement)

    otl_facility.davieExporter.export_objects_to_json_file(lijst_objecten, 'C:\\resources\\netwerkelementen_locaties_van_IP.json')


from Facility.OTLFacility import OTLFacility
from Loggers.ConsoleLogger import ConsoleLogger
from Loggers.LoggerCollection import LoggerCollection
from Loggers.TxtLogger import TxtLogger

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    jsonPath = "DA-2022-00006_export_slagbomen.json"
    slagbomen_assets = otl_facility.davieImporter.import_file(jsonPath)

    otl_facility.visualiser.show(slagbomen_assets)

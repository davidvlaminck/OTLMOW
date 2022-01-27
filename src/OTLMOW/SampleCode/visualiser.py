from src.OTLMOW.Facility.OTLFacility import OTLFacility
from src.OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from src.OTLMOW.Loggers.TxtLogger import TxtLogger
from src.OTLMOW.Loggers.LoggerCollection import LoggerCollection


if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    jsonPath = "DA-2022-00006_export_slagbomen.json"

    slagbomen_assets = otl_facility.davieImporter.import_file(jsonPath)

    otl_facility.visualiser.show(slagbomen_assets)

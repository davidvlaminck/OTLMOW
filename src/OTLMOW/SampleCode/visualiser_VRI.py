from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection


if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    jsonPath = "DA-2022-00191_export.json"

    vri_assets = otl_facility.davieImporter.import_file(jsonPath)

    otl_facility.visualiser.show(vri_assets)


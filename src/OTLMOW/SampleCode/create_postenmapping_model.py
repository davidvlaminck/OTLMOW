from src.OTLMOW.Facility.OTLFacility import OTLFacility
from src.OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from src.OTLMOW.Loggers.LoggerCollection import LoggerCollection
from src.OTLMOW.Loggers.TxtLogger import TxtLogger

if __name__ == '__main__':
    # create the main facade class: OTLFacility
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    # create a datamodel based on the postenmapping SQLite
    otl_file_location = '../InputFiles/Postenmapping_v1.0.0_RC1.db'
    otl_facility.init_postenmapping_creator(otl_file_location)
    otl_facility.create_posten_model()


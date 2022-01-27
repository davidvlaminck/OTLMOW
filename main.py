from src.OTLMOW.Facility.OTLFacility import OTLFacility
from src.OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from src.OTLMOW.Loggers.LoggerCollection import LoggerCollection
from src.OTLMOW.Loggers.TxtLogger import TxtLogger

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    otl_file_location = 'src/OTLMOW/InputFiles/OTL.db'
    otl_facility.init_otl_model_creator(otl_file_location)
    modelcreator = otl_facility.modelCreator
    modelcreator.query_correct_base_classes()

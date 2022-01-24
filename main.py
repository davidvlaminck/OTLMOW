from Facility.OTLFacility import OTLFacility
from Loggers.ConsoleLogger import ConsoleLogger
from Loggers.LoggerCollection import LoggerCollection
from Loggers.TxtLogger import TxtLogger

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    otl_file_location = 'InputFiles/OTL.db'
    otl_facility.init_otl_model_creator(otl_file_location)
    modelcreator = otl_facility.modelCreator
    modelcreator.query_correct_base_classes()

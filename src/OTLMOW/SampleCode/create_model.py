from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger

if __name__ == '__main__':
    # create the main facade class: OTLFacility
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    # create a datamodel based on the OTL SQLite database and ttl files stored on the github
    otl_file_location = '../InputFiles/OTL 2.3.db'
    GA_file_location = '../InputFiles/Geometrie_Artefact_2.3.RC2.db'
    otl_facility.init_otl_model_creator(otl_file_location, GA_file_location)
    otl_facility.create_otl_datamodel()

    # create an oef model as well
    oef_file_location = '../InputFiles/oef.legacy.json'
    ins_ond_file_location = '../InputFiles/oef.ins.ond.json'
    #otl_facility.init_oef_model_creator(oef_file_location, ins_ond_file_location)
    #otl_facility.create_oef_datamodel()


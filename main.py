from OTLMOW.Facility.AgentCollection import AgentCollection
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.Facility.SettingsManager import SettingsManager
from src.OTLMOW.Facility.OTLFacility import OTLFacility
from src.OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from src.OTLMOW.Loggers.LoggerCollection import LoggerCollection
from src.OTLMOW.Loggers.TxtLogger import TxtLogger

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger, settings_path='C:\\resources\\settings_OTLMOW.json', enable_relation_features=True)
    settings_manager = SettingsManager(settings_path='C:\\resources\\settings_OTLMOW.json')
    requester = RequesterFactory.create_requester(settings=settings_manager.settings, auth_type='cert', env='prd')
    agent = AgentCollection(requester=requester).get_agent_by_fulltextsearch_name("11")
    pass

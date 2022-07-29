from OTLMOW.Facility.AgentCollection import AgentCollection
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.Facility.SettingsManager import SettingsManager
from src.OTLMOW.Facility.OTLFacility import OTLFacility

if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\python_log.txt',
                               settings_path='C:\\resources\\settings_OTLMOW.json', enable_relation_features=True)
    settings_manager = SettingsManager(settings_path='C:\\resources\\settings_OTLMOW.json')
    requester = RequesterFactory.create_requester(settings=settings_manager.settings, auth_type='JWT', env='prd')
    agent = AgentCollection(requester=requester).get_agent_by_fulltextsearch_name("112")

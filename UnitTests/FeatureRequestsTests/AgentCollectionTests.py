import unittest

from OTLMOW.Facility.AgentCollection import AgentCollection
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.OTLModel.Classes.Agent import Agent
from SettingManagerForUnitTests import get_settings_path_for_unittests


class AgentCollectionTests(unittest.TestCase):
    def test_search_agent_by_name(self):
        settings_path = get_settings_path_for_unittests()
        otl_facility = OTLFacility(logfile='', settings_path=settings_path)
        requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')
        collection = AgentCollection(requester)
        agents_found = collection.get_agent_by_full_name('dave geudens')
        self.assertTrue(isinstance(agents_found, Agent))
        self.assertEqual('8a7c6f90-23b8-4170-b6b7-1517b8c8465b', agents_found.agentId.identificator[:36])
        self.assertEqual('Dave Geudens', agents_found.naam)

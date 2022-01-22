import unittest

from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder
from OTLModel.Classes.Agent import Agent


class AgentCollectionTests(unittest.TestCase):
    def test_search_agent_by_name(self):
        collection = AgentCollection()
        agents_found = collection.search_by_name('geudens')
        self.assertTrue(isinstance(agents_found, list))
        self.assertTrue(isinstance(agents_found[0], Agent))
        self.assertEqual('8a7c6f90-23b8-4170-b6b7-1517b8c8465b', agents_found[0].agentId[:36])
        self.assertEqual('Dave Geudens', agents_found[0].naam)
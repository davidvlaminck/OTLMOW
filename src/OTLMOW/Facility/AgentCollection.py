# agent collection queries EM-Infra otl/agents to check if an agent exists and returns is
# had built-in cache to reduce calls to the API
import json

from requests import Session

from OTLMOW.OTLModel.Classes.Agent import Agent


class AgentCollection:
    def __init__(self, requester: Session):
        self.requester = requester
        self.cache = {}

    def get_agent_by_full_name(self, full_name: str = ''):
        if full_name in self.cache:
            return self.cache[full_name]

        url = "eminfra/core/api/otl/agents/search"
        body = '{"filters": { "naam": ' + f'"{full_name}"' + ' }}'
        json_data = json.loads(body)
        response = self.requester.post(url, json=json_data)
        data = response.content.decode("utf-8")
        jsonobj = json.loads(data)
        obj_list = jsonobj["@graph"]

        if obj_list is None:
            self.cache[full_name] = None
            return None

        agent = Agent()
        agent.agentId.identificator = obj_list[0]['@id'].replace('https://data.awvvlaanderen.be/id/asset/', '')
        agent.agentId.toegekendDoor = 'AWV'
        agent.naam = obj_list[0]['purl:Agent.naam']

        self.cache[full_name] = agent
        return agent



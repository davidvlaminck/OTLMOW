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

        if obj_list is None or obj_list == []:
            self.cache[full_name] = None
            return None

        agent = Agent()
        agent.agentId.identificator = obj_list[0]['@id'].replace('https://data.awvvlaanderen.be/id/asset/', '')
        agent.agentId.toegekendDoor = 'AWV'
        agent.naam = obj_list[0]['purl:Agent.naam']

        self.cache[full_name] = agent
        return agent

    def get_agent_by_fulltextsearch_name(self, full_name: str = ''):
        if full_name in self.cache:
            return self.cache[full_name]

        url = "eminfra/core/api/agents/search"
        body = '{ "size": 10, "from": 0, "selection": { "expressions": [{ "terms": [{ "property": "naam", "value": "' + full_name + '", "operator": 1, "logicalOp": null, "negate": false } ], "logicalOp": null }, { "terms": [{ "property": "actief", "value": true, "operator": 0, "logicalOp": null, "negate": false } ], "logicalOp": "AND" } ] }, "pagingMode": "OFFSET" }'
        json_data = json.loads(body)
        response = self.requester.post(url, json=json_data)
        response_data = response.content.decode("utf-8")
        response_data_json = json.loads(response_data)
        if len (response_data_json['data']) == 0:
            self.cache[full_name] = None
            return None
        if len (response_data_json['data']) > 1:
            self.cache[full_name] = None
            raise ValueError('More than 1 Agent found, please narrow your search parameter')
        agent_uuids = list(map(lambda a: a['uuid'], response_data_json['data']))
        agent_uuids_str = '", "'.join(agent_uuids)

        url = "eminfra/core/api/otl/agents/search"
        body = '{"filters": { "uuid": [' + f'"{agent_uuids_str}"' + '] }}'
        json_data = json.loads(body)
        response = self.requester.post(url, json=json_data)
        data = response.content.decode("utf-8")
        jsonobj = json.loads(data)
        obj_list = jsonobj["@graph"]

        if obj_list is None or obj_list == []:
            self.cache[full_name] = None
            return None

        agent = Agent()
        agent.agentId.identificator = obj_list[0]['@id'].replace('https://data.awvvlaanderen.be/id/asset/', '')
        agent.agentId.toegekendDoor = 'AWV'
        agent.naam = obj_list[0]['purl:Agent.naam']

        self.cache[full_name] = agent
        return agent



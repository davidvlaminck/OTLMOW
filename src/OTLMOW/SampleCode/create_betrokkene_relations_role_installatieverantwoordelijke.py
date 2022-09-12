import json
from datetime import datetime
from pathlib import Path

from OTLMOW.Facility.AgentCollection import AgentCollection
from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.OTLModel.Classes.Onderdeel.HeeftBetrokkene import HeeftBetrokkene
from src.OTLMOW.Facility.OTLFacility import OTLFacility


def create_installatie_verantwoordelijke_relation(bron_identificator, doel_identificator):
    relatie = AssetFactory().dynamic_create_instance_from_uri(class_uri=HeeftBetrokkene.typeURI)

    relatie.bronAssetId.identificator = bron_identificator
    relatie.bronAssetId.toegekendDoor = 'AWV'

    relatie.doelAssetId.identificator = doel_identificator
    relatie.doelAssetId.toegekendDoor = 'AWV'

    relatie.assetId.identificator = bron_identificator + '_-_' + doel_identificator
    relatie.assetId.toegekendDoor = 'OTLMOW'

    relatie.rol = 'installatieverantwoordelijke'

    return relatie


if __name__ == '__main__':
    # create the main facade class: OTLFacility
    # otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\python_log.txt',
    #                            settings_path="C:\\resources\\settings_OTLMOW.json")
    otl_facility = OTLFacility(logfile=Path('/home/davidlinux/Documents/AWV/python_log.txt'),
                               settings_path=Path("/home/davidlinux/Documents/AWV/resources/settings_OTLMOW.json"))

    with open('/home/davidlinux/Documents/AWV/installatie_verantwoordelijke_antwerpen.json', encoding='utf-8-sig') \
            as input_data_file:
        input_data = json.load(input_data_file)

    requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')
    agent_collection = AgentCollection(requester=requester)

    relations = []

    for input_record in input_data:
        agent_name = input_record['installatieverantwoordelijke']
        aansluiting_identificator = input_record['aansl_identificator']

        if agent_name == 'onbekend':
            continue

        agent = agent_collection.get_agent_by_full_name(agent_name)

        relations.append(create_installatie_verantwoordelijke_relation(bron_identificator=aansluiting_identificator,
                                                                       doel_identificator=agent.agentId.identificator))

    # write the json file to upload in DAVIE
    path = Path(f'Output/{datetime.now().strftime("%Y%m%d%H%M%S")}_export.json')
    otl_facility.create_file_from_assets(list_of_objects=relations, filepath=path)

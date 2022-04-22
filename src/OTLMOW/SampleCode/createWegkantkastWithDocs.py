from OTLMOW.Facility.AgentCollection import AgentCollection
from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Wegkantkast import Wegkantkast

if __name__ == '__main__':
    # create the main facade class: OTLFacility
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger, settings_path='C:\\resources\\settings_OTLMOW.json', enable_relation_features=True)

    input_uuids = ['0199a655-8b63-4250-973b-a4d997a41325', '04040026-ded1-47b0-b0b1-a337393dd99b',
                   '054ec109-3ce6-4c04-817e-828ee4b30099', '055d54e7-0d60-471b-a256-9395b7916a35',
                   '05ee4ea3-02cf-467b-84b2-a531b5c2f3a0', '05f7d8b4-4bcd-48cd-a63a-70ce1fec29d0',
                   '06b6576d-1db2-4820-af83-e720d07cdc83', '084e7e1a-475c-4240-b255-cc2b597d81bc',
                   '086b6b79-79d7-497b-9616-daf86dddfed4', '0a673e4c-0551-4c06-8e42-799fd80b5c82',
                   '0b43b089-426f-4379-9d7e-cbfbb6416575', '0eba95f7-9f1a-49b3-8bea-7a634ba41155',
                   '0f99a24f-e263-4c93-a6b8-30c60f30b164', '102ef1b9-b8d5-4663-b40e-1bf2e9da13bf',
                   '11d83eeb-a2d3-455c-a349-b445444dc664', '127ed5a9-e01d-4b37-aedc-68b5a093f8ca',
                   '135b4158-7c2a-4c33-9928-c1c1546d0082', '13b75268-72c4-4145-b718-0727ac5e4754',
                   '16d6040e-ca06-4b57-9fe6-66378570ed75', '18e017f0-1b89-4b29-b47f-3629162b9ff2',
                   '192c0ee3-dd9e-492a-b487-34f7b2065f20', '19a63eb0-43d2-463f-822b-c233328a1b13',
                   '1a18c12c-f158-4a8b-8b83-05a61eac0a94', '1dd25a5e-c8bc-40da-8569-71bc20129c85',
                   '20d43a61-aa8b-434e-a052-14375f384891', '24449036-600a-4a39-bd73-75bc31786fc8',
                   '2482bd0a-f0c7-415c-ab5b-1aa6ca5b0042', '262caba7-32f2-4b16-9012-b9ec8e4da07b',
                   '274cff2f-5d81-4a84-b4d3-e8d5527152e9', '29bd4ee2-2668-4f8c-b0df-a6f18b665b4c',
                   '2b220d99-f178-48ad-9ffb-2c86fe078145', '2bb88991-b3db-4ec5-9072-154e8c429700',
                   '2c40f030-ed23-488e-bb20-d095677d0c0c', '2c65e205-7ab4-461d-86cc-3ab29854c36f',
                   '2d6e3a82-5335-40f1-a94b-cb6365bfb262', '2ddf1ea0-bade-42fa-96bf-b26bdea0ba61',
                   '2fa83b83-1592-4930-b23c-25b5a52aea1f', '2fad1235-7e1f-4eb4-a13f-5544ad12cdea',
                   '30d33462-5e5a-4f0f-a8b9-ac3d42ddba79', '3125c77d-f7dc-406a-8cdb-09c059b7c063',
                   '332a56d8-d544-41ae-9305-ad0f9c842b6f', '339c87a7-66ed-4969-bc37-8a1346dea1c8',
                   '339cceda-6306-4fd5-be31-2f88ace24f52', '34784869-2579-4262-8d5f-edd91fe854a3',
                   '34a2d38b-aa54-46a4-9974-96aa7c7865b2', '34e05fb2-f3f1-46b8-b968-27eacd3ba741',
                   '366fc820-9fbe-4a43-be30-5a36b717f20c', '367b63bc-aac9-40ab-b080-25a5e933e602',
                   '38b38cef-1dca-4639-987d-2a0c941a2f25', '3b193f9a-8f14-4205-b772-4b3dba8d8be2',
                   '3bd360e9-d7f1-4bb8-a385-ebb65636eeca', '3f6d85d3-5a0b-4162-962d-011aeb928013',
                   '407b5850-b0e9-4f03-8d2b-6269c4ca7499', '45077cbf-753a-4f02-bec8-6f195826349d',
                   '4756e7d0-8f19-4163-a911-18d7e0fd5366', '4982ad6b-b294-441a-846b-634b422a5e29',
                   '4a470b61-087d-4a16-823f-4461c3df62c8', '4a5fd2c5-c4d6-4fec-a0c6-8e79db0a1c93',
                   '4a793b1e-4ea1-4efb-8ea4-f427132f562e', '4b2c6edd-da8f-4e1e-95d8-7cd808f1cba6',
                   '4cc7ae64-594e-42c8-8fb6-e8419b078235', '4e0be4d6-354e-475b-8dd8-73d1c9fffdf9',
                   '4e750eca-e658-4eda-b8bb-aad42b2c86d4', '521d67ea-575a-46dc-886a-c39fae1585f2',
                   '5384dbc4-309d-4444-a4d0-7e540d802138', '53a95977-1c05-4ff0-bfe3-05be2ca8b7c7',
                   '54f06011-883c-4887-b628-067f3926973f', '551a0e52-8787-4ef9-af06-70180307f650',
                   '5a627b81-1eee-44ed-b86c-019d92791a78', '5c9ea193-afe0-41f6-88d6-ae2f491634df',
                   '5e1da6fd-189f-4834-b289-116e252b0227', '5e3f51b2-d618-48c4-b2a6-2033d9937788',
                   '5eaef68c-9a61-4233-b6aa-a79024bd920c', '605000aa-1f01-423b-83ba-20cc1dc1861f',
                   '65af0bf0-cd22-47b7-8bad-083851fd88b3', '65ffd41e-9732-4a71-883b-59591135b324',
                   '68b7f254-12ec-47be-8f9e-c6c4ebb19984', '6d456fa6-0301-4374-b84b-6f10e038c7c1',
                   '6e24cbbd-e0c4-43bd-bd60-bf5066faa664', '6e84f4c6-8b97-40dc-9ac4-eb823407d594',
                   '6fa050cb-6bca-4c65-beab-3c80ca6acb49', '704e6291-78ae-4fb2-b2e2-403d909c2508',
                   '70db1a4d-763b-41b4-99b9-1c50f346f4b5', '744f4bf8-8b1e-4fff-b010-115c4ebddef9',
                   '753600e9-1d3f-4bb6-8fdd-3783b09ec375', '75962469-3c43-49b0-a33f-6d9f5cfbcfdb',
                   '75abbc64-d337-4871-843c-8917ae87bb01', '75e82b07-0837-4b6a-b4a5-a46ce003360d',
                   '76dd1935-014b-4624-beea-4285de4a2605', '775bdedc-dd9d-4d9c-bbbb-dae55bc305ea',
                   '77c2fcf3-398d-420a-89a8-0f7a47279141', '79c46f91-0ce8-4f4a-ac9e-1483484789c8',
                   '7da0d11a-fbe6-4f26-9b54-9bd12e0141b0', '7ebbd910-bb27-414b-9165-d5d4169e0383',
                   '7f355ae3-202a-40d0-8d67-0c0826e7da6c', '7ff55fd1-3d46-45f8-9435-2654285983d0',
                   '80510500-d052-41ef-916c-127ec913ca2d', '8351f806-9fe8-4ff9-8a7e-edb11a651e19',
                   '84aeb334-f3aa-43be-86c1-539eae40435a', '84b08e24-048c-4e23-a52f-4957c7c3b887',
                   '86a9f41c-31ef-40bc-afd1-db758678d951', '883ad403-14f7-4b5e-82bb-1b1966a23c97',
                   '88f465ba-a09c-47df-8b34-9672c54f9c07', '8952748d-73a3-4463-a30c-4b68b7f7fd8a',
                   '89fdf664-91e7-4fe2-994c-d29f067ccaaa', '8a6d6f17-1048-4b31-b1f7-b717457533a5',
                   '8afbad4f-8a6b-4326-9c8e-d60e293e6843', '8b3f6ced-4667-49a5-8bfb-595965ab7cf3',
                   '8ed5a9f6-422f-4022-aa3a-5a7c4de974a4', '9095f8ff-203e-4993-9638-96e06665c089',
                   '948e4ddf-5e97-4426-a3f9-bbdb4a5621e7', '961af87e-6f00-4901-b56e-fda3873347dd',
                   '972a3120-7f7a-46c4-b534-4bcae7cd5958', '978fad6d-8352-40d7-869e-92094815ac5a',
                   '97e7fe65-dda8-44dc-9667-28bcbbf1c862', '9a30aaa1-b9e6-4539-9950-32f93f1ae02b',
                   '9c43dcc5-5175-4c7f-a5ea-7b2c20537899', '9d9ed37a-a095-4e20-a36c-d4b8b88e4eda',
                   '9e4369dc-a152-4630-b01a-bc4354b85744', '9e805d31-b314-44f3-8fdd-d0d30d7748d6',
                   '9eea5719-2834-4988-a204-41fdc740d8c7', '9f33114c-234e-4df3-adc4-2162a3a234ed',
                   'a1999503-4b1a-424d-8411-5467f8abd44b', 'a1e78188-d479-43ae-8354-b096e889c25b',
                   'a1ef5043-c428-4928-ab15-917d87197765', 'a500c7fc-1165-4e1c-b683-59a361db40e9',
                   'a6a4eabf-35f3-4f70-9b3f-309b9596fdd0', 'a7a9aeee-4383-4ea8-b25e-c27bf2462194',
                   'a8690254-a9d8-4169-9d25-a27f8013ba88', 'a9637316-220f-4ea3-81f8-7a2fc03118f6',
                   'a9f897a9-0778-4ef1-b281-d4e78f149d14', 'acdca43f-7194-40a7-9fec-fd85c8d95c2d',
                   'ad1da1e7-d411-4166-b1ff-1b7423b5d9b7', 'add5bfa1-c645-4963-b755-751d81abebe6',
                   'aecd72e8-53a3-4d65-a9c4-2263a598b2e3', 'b0b3bc8a-78d3-4698-b145-b9d0355da682',
                   'b301d676-307a-40ba-95c8-9c9fb53e05ad', 'b34a502d-31f8-48a9-9ea6-c22195391f37',
                   'b7104fea-6797-4cb1-b735-dc362db88f86', 'b8d831e8-0ff0-4651-b9d1-5b563873b292',
                   'b9f161d3-d051-44e5-8ff8-01dfcca86a37', 'bb22b2ac-040c-431a-8726-cfd3d0bd7498',
                   'bd361573-070e-4a6c-954b-531118b76a86', 'bda5d0cb-d174-4a27-b39c-0f85f24405e9',
                   'bdd92801-f809-4431-825e-bfc725c7873d', 'be8b64b5-9824-4e24-a0a9-b6d88b9e63f0',
                   'c1786f0a-9214-4e06-8005-d890a12c8fb5', 'c21c4bbc-efda-43aa-89b1-944ac294ae1c',
                   'c307cfa2-1a39-46c5-acdf-3e03fe007fd8', 'c4113d62-295c-4218-86ec-309354e55b4f',
                   'c4fb8a93-7b8f-4769-ab09-6fba4d6344c7', 'c576c71d-a8af-4873-8063-c66826a66b5d',
                   'c6c6445b-4496-4364-a41d-5093843367b5', 'c749dd58-dc22-42f6-975e-037cb39e6eec',
                   'ca07b864-6916-4589-88a5-e71cbbe75f31', 'cbfe9e6e-a87d-40a0-96c0-97d4fcdf50ee',
                   'cf43f9ac-fcf0-413f-994e-98960b2a3944', 'cfda0c80-a5a8-4537-bd75-a705c40f1079',
                   'd44726c3-9fc9-452c-b108-52929f744e8b', 'd89ec736-e279-4979-b358-5d33d637796d',
                   'd8c4a3d5-d675-408e-8cfb-9613583e81fa', 'd8d60d5d-a3c4-4f0d-90e9-c0263142fa89',
                   'd98457f8-428f-4f88-9186-27fd2122345f', 'd9e0b78a-be6c-4679-bab8-25b7502db180',
                   'da329ccd-e60c-4257-8058-9d110a0d89f1', 'dba01c68-d7d9-4b02-9ec4-3eb9ae47c275',
                   'dc039abe-5313-473f-8ff1-a2ffb9159a55', 'dc5caacb-be6e-4c4b-9239-4ce2bb643314',
                   'dc8cafa3-5b54-4c9a-9f63-ce8a5a0cc9f3', 'dcdce3a2-f916-4563-b406-d0a313ffd652',
                   'dd5659f5-348f-4bcb-bf14-bdfa786195ee', 'dda9c7da-348f-4a56-a584-09e090341d28',
                   'df686bdd-98f3-41b0-94e6-d6fa5a39d5f4', 'dfc6da8f-9213-412e-8e16-e91584b6718a',
                   'e0c09811-addc-402e-85d7-b8f32f2d20ac', 'e0f59790-6283-460f-81e3-cba0b2e17913',
                   'e1d444cf-85d6-44d1-b8a0-0a553a8482b8', 'e250db11-aceb-45a3-8dec-2272e123c16a',
                   'e45b294c-3d59-48d0-9ebe-67a511400f9e', 'e4796bd6-8f41-48fd-b716-c417fa4622ca',
                   'e60b48aa-1525-4f34-9fd1-bffa81b359b8', 'e6149f48-55ba-4f1d-bea5-d8013660e078',
                   'e64cd6dc-26e9-4e66-8867-e542c72c9ca9', 'e7dc3a76-f26f-4e89-bb4e-ac50267f6526',
                   'e865256b-d254-446c-81ea-8e892a7a4f31', 'e9eb6032-51b2-4fd5-b41b-7e0b5652569a',
                   'ea25ef7d-39a3-4888-b409-310ac08d953c', 'eb5d4c13-c8a5-4175-9b7f-9a4256d369cb',
                   'ebc65331-8a89-4414-999e-9d473dc0ee8a', 'ec056155-72d6-4efa-b156-2db0bdb99d7f',
                   'ecfcd01e-e099-4f24-afce-8ef9396c72f7', 'ede1f137-8a8c-4290-9202-1d31921aa580',
                   'eed09ebe-5d31-4113-988b-60e10b09e789', 'ef451eb2-420c-42e4-96bd-176107bfe5d7',
                   'f1f1e8f6-568a-43a9-b567-805602c6d292', 'f362d41e-ddcd-4878-b673-e6f36e3d3e16',
                   'f384f3f8-df3a-4470-aeab-1a53d016a130', 'f5df5613-fc6b-4304-b658-0edb03c1ff60',
                   'f6bd9254-cf52-4ea5-9c9b-1d029cb1a387', 'f7a1b988-325a-4a67-999b-1eb58c77b41b',
                   'fa758917-4b78-400b-ba5f-b7dd3a398754', 'fae380ca-f3e2-43cd-b169-917dfce6dca1',
                   'fae4dfb5-7b65-47cf-9cb0-f72207c7e917', 'fbc05df2-563f-40a3-958a-c1767f18a31e',
                   'fcd8a4a5-7072-4ea6-bb37-a3e0172c3cb3', 'fd4ebf0e-ca82-4f54-95f4-ac9880b2bc05',
                   'fd9d13e5-32b9-440e-a380-06cf46abd852', 'fea3e6fa-8273-4ad6-94ae-eb5d6d34f6c8',
                   'fef1efee-c219-4ad6-a379-34c865a3cbb8', 'ff829789-e84b-4f70-a82c-2da0aabd4410',
                   'ffcef8a9-b45a-48e9-bea7-117a0878691f', 'fff6c74a-58e5-4565-b261-7faad8ea741b']

    requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')

    importer = EMInfraImporter(requester=requester)
    assets = importer.import_assets_from_webservice_by_uuids(input_uuids)
    lijst_objecten = []

    agent_collection = AgentCollection(requester=requester)

    for kast in assets:
        wegkantkast = Wegkantkast()
        wegkantkast.naam = kast.naam
        wegkantkast.toestand = kast.toestand
        wegkantkast.geometry = kast.geometry
        wegkantkast.assetId.identificator = kast.naam
        wegkantkast.assetId.toegekendDoor = 'OTLMOW'

        toezichternaam = kast.toezichter.voornaam
        if toezichternaam is None:
            toezichternaam = ''
        if kast.toezichter.naam is not None:
            toezichternaam = toezichternaam + ' ' + kast.toezichter.naam
        toezichter = agent_collection.get_agent_by_full_name(toezichternaam)
        if toezichter is not None:
            toezichterrelatie = otl_facility.relatie_creator.create_betrokkenerelation(bron=wegkantkast, doel=toezichter)
            toezichterrelatie.rol = 'toezichter'
            lijst_objecten.append(toezichterrelatie)

        toezichtgroepnaam = kast.toezichtgroep.naam
        toezichtgroep = agent_collection.get_agent_by_full_name(toezichtgroepnaam)
        if toezichtgroep is not None:
            toezichtgroeprelatie = otl_facility.relatie_creator.create_betrokkenerelation(bron=wegkantkast, doel=toezichtgroep)
            toezichtgroeprelatie.rol = 'toezichtsgroep'
            lijst_objecten.append(toezichtgroeprelatie)

        schadebeheerdernaam = kast.schadebeheerder.naam
        schadebeheerder = agent_collection.get_agent_by_full_name(schadebeheerdernaam)
        if schadebeheerder is not None:
            schadebeheerderrelatie = otl_facility.relatie_creator.create_betrokkenerelation(bron=wegkantkast,
                                                                                            doel=schadebeheerder)
            schadebeheerderrelatie.rol = 'schadebeheerder'
            lijst_objecten.append(schadebeheerderrelatie)

        lijst_objecten.append(wegkantkast)

        hoortbijrelatie = otl_facility.relatie_creator.create_relation(bron=wegkantkast, doel=kast, relatie=HoortBij)
        lijst_objecten.append(hoortbijrelatie)

    # write to a json file that can be uploaded in Davie
    otl_facility.davieExporter.export_objects_to_json_file(lijst_objecten,
                                                           'C:\\resources\\DA-2022-00557_wegkantkasten_prd_voor_import.json')

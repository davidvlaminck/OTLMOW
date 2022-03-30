import collections

from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection


if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger, settings_path='C:\\resources\\settings_OTLMOW.json')

    input_uuids = ['eb45c3a5-2bf9-4c56-b665-2a7dafb6b709', 'c22298c5-1978-49c9-83ec-a2ffd7a71665',
                   '2caf2a3c-bc45-454c-8602-26dbfc2ea3bd', '3d22fd7e-d45d-4553-973f-87a18c29f428',
                   '25fc76ba-3e20-46cb-868f-3946647df08a', 'c22298c5-1978-49c9-83ec-a2ffd7a71665',
                   'abf9749f-649c-4eaf-9870-419f8c978ab4', 'dd8aa900-49ef-413c-917e-01cd76ba274a',
                   '73947f51-767a-4155-893c-02d5c6f359a0', '7f8a1021-cc52-4922-b8bc-e9c28c34180d',
                   '446d9ea9-d82b-4e0c-a12a-067c80baa809', '2d1c2ce3-9bff-4e4c-8e24-b2bbcfe66cd5',
                   '007105f0-521c-4ead-9e4e-1c7f8546f01b', '771f43fe-50d6-43ad-94ac-8bfa14ec7eb4',
                   '63ab7434-918b-463e-ab9e-e004e4335482', '13d10054-737f-4b22-a18b-a7c8dd3683d6',
                   '93f5cdc3-fe0c-412d-ba31-0787d14258c5', 'eb45c3a5-2bf9-4c56-b665-2a7dafb6b709',
                   '25bbea3b-ac64-4ded-99b4-42133f4b76d8', '119bd2c7-23b5-40ea-94c1-7729a055c441',
                   '782720cf-585e-4863-a3db-d6b2a743eeaa', '850f9be7-302b-44b5-8752-c3323c55ce75',
                   '9ca7baae-8d4b-4752-a016-b58f1b2a9cdc', '9d085b55-5bf2-4f9e-a16a-c571ab2158f1',
                   '865cddb3-4737-4048-8a94-b2072c68ea8e', '04d7544e-06b9-4f3f-afde-0dd69de0a7e3',
                   '2f92ba74-9011-4dda-9935-51b5e00a097d', '79c4b922-3984-4895-83f0-11da8002f1a6',
                   '450d5fe8-3d1f-441e-9fd6-3df9129d9265', 'edac00d5-8c8e-4ba1-b781-48ef029809f7',
                   '83d761ca-62e6-4951-9a0d-83c416d4a44c', '2f92ba74-9011-4dda-9935-51b5e00a097d',
                   '0e507a88-cf7c-461b-bdb5-cf092b171105', '400919e2-cca4-424b-8f96-4003732bdf2b']

    requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')

    importer = EMInfraImporter(requester=requester)

    # fetch assets, based on a list of uuids
    assets = importer.import_assets_from_webservice_by_uuids(input_uuids)
    relatie_list = []

    # for each asset, find all relations
    for asset in assets:
        relaties = importer.import_assetrelaties_from_webservice_by_assetuuid(asset.assetId.identificator[0:36])
        relatie_list.extend(relaties)
    assets.extend(relatie_list)

    # there will be duplicates, this removes duplicate assets, based on assetId.identificator
    seen = collections.OrderedDict()
    for obj in assets:
        if obj.assetId.identificator not in seen:
            seen[obj.assetId.identificator] = obj
    assets = list(seen.values())

    #visualize the list of assets
    otl_facility.visualiser.show(seen.values())

    # for item in otl_facility.make_overview_of_assets(slagbomen_assets).items():
    #     print(item)

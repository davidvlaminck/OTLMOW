from csv import reader

from OTLMOW.Facility.FileFormats.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Netwerkelement import Netwerkelement


# goal:
# take list of uuid's and find the related legacy element to inherit geometry from
if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger, settings_path="C:\\resources\\settings_OTLMOW.json")
    requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')
    importer = EMInfraImporter(requester=requester)

    # input file
    uuid_file_path = 'C:\\resources\\export.csv'

    # create objects based on uuid (from input file) and typeURI
    lijst_objecten = []
    with open(uuid_file_path, 'r') as uuidfile:
        csv_reader = reader(uuidfile, delimiter=',')
        for row in csv_reader:
            netwerkElement = Netwerkelement()
            netwerkElement.assetId.identificator = EMInfraImporter.get_asset_id_from_uuid_and_typeURI(row[0], Netwerkelement.typeURI)
            netwerkElement.assetId.toegekendDoor = 'AWV'
            lijst_objecten.append(netwerkElement)

    # use the uuids of the objects to get the HoortBij relations
    netwerkelement_uuids = list(map(lambda x: x.assetId.identificator[0:36], lijst_objecten))
    all_relations = importer.import_assetrelaties_from_webservice_by_assetuuids(netwerkelement_uuids)
    hoortbij_relations = list(filter(lambda r: r.typeURI == HoortBij.typeURI, all_relations))

    # use the HoortBij relations to get the target objects
    hoortbij_doel_uuids = list(map(lambda x: x.doelAssetId.identificator[0:36], hoortbij_relations))
    hoortbij_doelen = importer.import_assets_from_webservice_by_uuids(hoortbij_doel_uuids)

    aan_te_leveren = []
    for netwerkElement in lijst_objecten:
        # filter out elements that do not have a HoortBij relation
        hoortbij_relaties = list(filter(lambda r: r.bronAssetId.identificator[0:36] == netwerkElement.assetId.identificator[0:36], hoortbij_relations))
        if len(hoortbij_relaties) == 0:
            continue

        # filter out elements where the target object of the HoortBij relation does not have a geometry
        hoortbij_doel_uuids = list(map(lambda x: x.doelAssetId.identificator[0:36], hoortbij_relaties))
        bijhorende_objecten = list(filter(lambda d: d.assetId.identificator[0:36] in hoortbij_doel_uuids and
                                       d.typeURI != 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#L2AccessStructuur', hoortbij_doelen))
        if len(bijhorende_objecten) == 0:
            continue
        if len(bijhorende_objecten) > 1:
            raise NotImplementedError

        bijhorend_object = bijhorende_objecten[0]
        if bijhorend_object is None or not hasattr(bijhorend_object, 'geometry') or bijhorend_object.geometry is None:
            continue

        netwerkElement.geometry = bijhorend_object.geometry
        aan_te_leveren.append(netwerkElement)

    # write a file for Davie
    otl_facility.davieExporter.export_objects_to_json_file(aan_te_leveren, 'C:\\resources\\netwerkelementen_locaties_van_IP_20220518.json')


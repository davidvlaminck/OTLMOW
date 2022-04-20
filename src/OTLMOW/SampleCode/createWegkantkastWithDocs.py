from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Wegkantkast import Wegkantkast


def normaliseer_exoten():
    # create the main facade class: OTLFacility
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger, settings_path='C:\\resources\\settings_OTLMOW.json')

    input_uuids = ['4a470b61-087d-4a16-823f-4461c3df62c8', '0199a655-8b63-4250-973b-a4d997a41325', '04040026-ded1-47b0-b0b1-a337393dd99b',
                   '054ec109-3ce6-4c04-817e-828ee4b30099', '055d54e7-0d60-471b-a256-9395b7916a35',
                   '05ee4ea3-02cf-467b-84b2-a531b5c2f3a0', '05f7d8b4-4bcd-48cd-a63a-70ce1fec29d0']

    requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')

    importer = EMInfraImporter(requester=requester)
    assets = importer.import_assets_from_webservice_by_uuids(input_uuids)
    lijst_objecten = []

    for kast in assets:
        wegkantkast = Wegkantkast()
        wegkantkast.naam = kast.naam
        wegkantkast.geometry = kast.geometry
        # toezichter
        # toezichtgroep
        # schadebeheerder
        # assetId
        lijst_objecten.append(wegkantkast)

        hoortbijrelatie = otl_facility.relatie_creator.create_relation(bron=wegkantkast, doel=kast, relatie=HoortBij)
        lijst_objecten.append(hoortbijrelatie)

    # write to a json file that can be uploaded in Davie
    otl_facility.davieExporter.export_objects_to_json_file(lijst_objecten, 'C:\\resources\\DA-2022-00000_wegkantkasten_prd_voor_import.json')


if __name__ == '__main__':
    normaliseer_exoten()

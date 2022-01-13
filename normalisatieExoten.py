from Facility.OTLFacility import OTLFacility
from Loggers.TxtLogger import TxtLogger
from OTLModel.Classes.InvasieveExoten import InvasieveExoten


def normaliseer_exoten():
    # create the main facade class: OTLFacility
    logger = TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt')
    otl_facility = OTLFacility(logger)

    # import from a Davie json file
    jsonPath = "C:\\resources\\DA-2022-00004_export_exoten_normalisatie_prd.json"
    lijst_exoten = otl_facility.davieImporter.import_file(jsonPath)

    lijst_objecten = []
    # loop through all objects and create an instance of InvasieveExoten based on an existing Exoten
    list_of_fields_to_copy = otl_facility.asset_factory.get_public_fieldlist_from_object(lijst_exoten[0])
    for exoten in lijst_exoten:
        nieuwe_invasieve_exoten = otl_facility.asset_factory.create_aimObject_using_other_aimObject_as_template(
            orig_aimObject=exoten, typeURI=InvasieveExoten.typeURI, fieldsToCopy=list_of_fields_to_copy)

        nieuwe_invasieve_exoten.assetId.identificator.waarde = f'nieuwe_versie_van_{exoten.assetId.identificator.waarde}'
        lijst_objecten.append(nieuwe_invasieve_exoten)

        # also set isActief to False to soft-delete Exoten
        exoten.isActief.waarde = False
        lijst_objecten.append(exoten)

    # write to a json file that can be uploaded in Davie
    otl_facility.davieExporter.export_objects_to_json_file(lijst_objecten, 'C:\\resources\\DA-2022-00004_exoten_normalisatie_prd_voor_import.json')

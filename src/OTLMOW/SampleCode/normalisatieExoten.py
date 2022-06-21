from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.Onderdeel.InvasieveExoten import InvasieveExoten


def normaliseer_exoten():
    # create the main facade class: OTLFacility
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\pythonlog.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    # import from a Davie json file
    jsonPath = "C:\\resources\\DA-2022-00004_export_exoten_normalisatie_prd.json"
    lijst_exoten = otl_facility.json_importer.import_file(jsonPath)

    lijst_objecten = []

    # loop through all objects and create an instance of InvasieveExoten based on an existing Exoten object
    list_of_fields_to_copy = otl_facility.asset_factory.get_public_fieldlist_from_object(lijst_exoten[0])
    for exoten in lijst_exoten:
        # create InvasieveExoten, using the data of Exoten
        nieuwe_invasieve_exoten = otl_facility.asset_factory.create_aimObject_using_other_aimObject_as_template(
            orig_aimObject=exoten, typeURI=InvasieveExoten.typeURI, fieldsToCopy=list_of_fields_to_copy)

        # change the assetId and add for the import
        nieuwe_invasieve_exoten.assetId.identificator = f'nieuwe_versie_van_{exoten.assetId.identificator}'
        lijst_objecten.append(nieuwe_invasieve_exoten)

        # set isActief to False to soft-delete Exoten and add for the import
        exoten.isActief = False
        lijst_objecten.append(exoten)

    # write to a json file that can be uploaded in Davie
    otl_facility.jsonExporter.export_objects_to_json_file(lijst_objecten,
                                                          'C:\\resources\\DA-2022-00004_exoten_normalisatie_prd_voor_import.json')


if __name__ == '__main__':
    normaliseer_exoten()

from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.AanvullendeGeometrie import AanvullendeGeometrie

def normaliseer_exoten():
    # create the main facade class: OTLFacility
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\pythonlog.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    # import from a Davie json file
    jsonPath = "C:\\resources\\DA-2022-00553_export.json"
    lijst_FoV = otl_facility.davieImporter.import_file(jsonPath)
    lijst_FoV = list(filter(lambda a: "FieldOfView" in a.typeURI, lijst_FoV))

    lijst_objecten = []

    # loop through all objects and create an instance of InvasieveExoten based on an existing Exoten object
    list_of_fields_to_copy = otl_facility.asset_factory.get_public_field_list_from_object(lijst_FoV[0])
    for FoV in lijst_FoV:
        # create InvasieveExoten, using the data of Exoten
        aanvullende_geometrie = otl_facility.asset_factory.create_aimObject_using_other_aimObject_as_template(
            orig_aimObject=FoV, typeURI=AanvullendeGeometrie.typeURI, fields_to_copy=list_of_fields_to_copy)

        # change the assetId and add for the import
        aanvullende_geometrie.assetId.identificator = f'nieuwe_versie_van_{FoV.assetId.identificator}'
        lijst_objecten.append(aanvullende_geometrie)

        # set isActief to False to soft-delete Exoten and add for the import
        FoV.isActief = False
        lijst_objecten.append(FoV)

    # write to a json file that can be uploaded in Davie
    otl_facility.jsonExporter.export_objects_to_json_file(lijst_objecten, 'C:\\resources\\DA-2022-00553_normalisatie_FoV_prd_voor_import.json')

if __name__ == '__main__':
    normaliseer_exoten()
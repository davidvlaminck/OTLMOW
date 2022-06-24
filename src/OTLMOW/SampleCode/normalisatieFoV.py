from OTLMOW.Facility.FileFormats.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.OTLModel.Classes.Onderdeel.AanvullendeGeometrie import AanvullendeGeometrie


def normaliseer_field_of_views():
    # create the main facade class: OTLFacility
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\pythonlog.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')
    importer = EMInfraImporter(requester=requester)
    lijst_FoV = importer.import_assets_from_webservice_by_type_uuid("397d531c-9b76-44e7-a0e3-05e7f4150018")

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
    normaliseer_field_of_views()
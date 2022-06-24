from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.Abstracten.Behuizing import Behuizing

if __name__ == '__main__':
    otl_facility = OTLFacility(settings_path="C:\\resources\\settings_OTLMOW.json")

    # create a datamodel based on the OTL SQLite database and ttl files stored on the github
    otl_file_location = '../InputFiles/OTL 2.4.db'
    GA_file_location = '../InputFiles/Geometrie_Artefact_2.4.db'

    abstract_class_type = Behuizing

    model_creator = otl_facility._init_otl_model_creator(otl_file_location, GA_file_location)
    model_creator.oslo_collector.collect()

    for uri in model_creator.oslo_collector.find_indirect_superclasses_uri_by_class_uri(abstract_class_type.typeURI):
        print(uri)



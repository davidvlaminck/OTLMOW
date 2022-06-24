from OTLMOW.Facility.OTLFacility import OTLFacility

if __name__ == '__main__':
    # create the main facade class: OTLFacility
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\python_log.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    # create a datamodel based on the postenmapping SQLite
    otl_file_location = '../InputFiles/Postenmapping_v1.0.0_RC1.db'
    otl_facility.init_postenmapping_creator(otl_file_location)
    otl_facility.create_posten_model()


from OTLMOW.Facility.OTLFacility import OTLFacility

if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\pythonlog.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    file_path = 'C:\\resources\\DA-2022-00191_export.json'
    objects = otl_facility.davieImporter.import_file(filePath=file_path)
    pass
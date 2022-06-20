from OTLMOW.Facility.OTLFacility import OTLFacility


if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\pythonlog.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    jsonPath = "DA-2022-00006_export_slagbomen.json"

    slagbomen_assets = otl_facility.davie_importer.import_file(jsonPath)

    otl_facility.visualiser.show(slagbomen_assets)

    # for item in otl_facility.make_overview_of_assets(slagbomen_assets).items():
    #     print(item)

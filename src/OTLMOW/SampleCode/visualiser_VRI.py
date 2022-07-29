from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.Visualiser import Visualiser

if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\python_log.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    jsonPath = "DA-2022-00191_export.json"

    vri_assets = otl_facility.create_assets_from_file(jsonPath)

    Visualiser().show(vri_assets)


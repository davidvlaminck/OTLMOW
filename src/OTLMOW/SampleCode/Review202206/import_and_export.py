from datetime import datetime

from OTLMOW.Facility.OTLFacility import OTLFacility

if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=fr'C:\temp\pythonLogging\{datetime.now().strftime("%Y%m%d%H%M%S")}_python_log.txt',
                               settings_path=r'C:\resources\settings_OTLMOW.json')

    # import a JSON file from Davie
    file_path = r'C:\resources\DA-2022-00191_export.json'  # VRI Stenenbrug op tei
    objects = otl_facility.create_assets_from_file(filepath=file_path, ignore_failed_objects=True)

    # export to a JSON file
    export_json_path = f'..\\Output\\{datetime.now().strftime("%Y%m%d%H%M%S")}_export.json'
    otl_facility.create_file_from_assets(filepath=export_json_path, list_of_objects=objects)

    # export to a csv file
    export_csv_path = f'..\\Output\\{datetime.now().strftime("%Y%m%d%H%M%S")}_export.csv'
    otl_facility.create_file_from_assets(filepath=export_csv_path, list_of_objects=objects, split_per_type=True)

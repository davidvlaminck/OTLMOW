from datetime import datetime

from OTLMOW.Facility.FileFormats.CsvExporter import CsvExporter
from OTLMOW.Facility.OTLFacility import OTLFacility

if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=fr'C:\temp\pythonLogging\{datetime.now().strftime("%Y%m%d%H%M%S")}_pythonlog.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    # import a JSON file from Davie
    file_path = 'C:\\resources\\DA-2022-00191_export.json' # VRI Stenenbrug op tei
    objects = otl_facility.davie_importer.import_file(filePath=file_path, ignore_failed_objects=True)

    # export to a JSON file
    export_json_path = f'{datetime.now().strftime("%Y%m%d%H%M%S")}_export.json'
    encoded_json = otl_facility.encoder.encode(objects)
    otl_facility.encoder.write_json_to_file(encoded_json, export_json_path)

    # export to a csv file
    export_csv_path = f'{datetime.now().strftime("%Y%m%d%H%M%S")}_export.csv'
    exporter_csv = CsvExporter(otl_facility.settings)
    exporter_csv.export_csv_file(objects, file_location=export_csv_path, split_per_type=True)

    pass
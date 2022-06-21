import os

from OTLMOW.Facility.Exceptions.InvalidExtensionError import InvalidExtensionError
from OTLMOW.Facility.FileFormats.CsvImporter import CsvImporter
from OTLMOW.Facility.FileFormats.JsonImporter import JsonImporter


class FileImporter:
    def __init__(self, settings: dict):
        self.settings = settings

    def create_assets_from_file(self, filepath, **kwargs):
        extension = self.get_file_extension(filepath)
        importer = self.get_importer_from_extension(extension=extension, settings=self.settings)
        return importer.import_file(filepath=filepath, **kwargs)

    @staticmethod
    def get_file_extension(filepath):
        if filepath == '' or filepath is None:
            raise ValueError('filepath is empty, specify a file path')

        if '.' not in filepath:
            raise ValueError('This file does not have an extension. An extension is required to determine the type of importer '
                             'that is needed to import this file')

        if not os.path.isfile(filepath):
            raise FileNotFoundError(filepath + " is not a valid path. File does not exist.")

        index = filepath.rfind('.')
        return filepath[index+1:]

    @staticmethod
    def get_importer_from_extension(extension, settings):
        if extension == 'csv':
            return CsvImporter(settings=settings)
        if extension == 'json':
            return JsonImporter(settings=settings)
        else:
            raise InvalidExtensionError('This file has an invalid extension. Supported file formats are: csv, json')


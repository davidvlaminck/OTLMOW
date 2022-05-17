import os

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.DotnotatieHelper import DotnotatieHelper
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject


class CsvExporter:
    def __init__(self, settings=None):
        if settings is None:
            settings = {}
        self.settings = settings

        if 'file_formats' not in self.settings:
            raise ValueError("The settings are not loaded or don't contain settings for file formats")
        csv_settings = next((s for s in settings['file_formats'] if 'name' in s and s['name'] == 'csv'), None)
        if csv_settings is None:
            raise ValueError("Unable to find csv in file formats settings")

        self.settings = csv_settings
        self.headers = []
        self.data = [[]]
        self.objects = []
        self.csv_headers = []

    def export_csv_file(self, list_of_objects: list = [], file_location: str = '', separator=';'):
        if file_location == '' or not os.path.isfile(file_location):
            raise FileNotFoundError(f'Could not load the file at: {file_location}')

        try:
            with open(file_location, 'r') as file:
                self.headers = file.readline()[:-1].split(separator)
                data = []
                for line in file:
                    data.append(line[:-1].split(separator))
                self.data = data[1:]

        except Exception as ex:
            raise ex

        return self.create_data_from_objects()

    def create_data_from_objects(self, list_of_objects: list = []) -> [[str]]:
        csv_data = []
        if list_of_objects is None or list_of_objects == []:
            raise ValueError('There is no data to export to a csv file')

        self.csv_headers = ['typeURI', 'assetId.identificator', 'assetId.toegekendDoor']

        for object in list_of_objects:
            if isinstance(object, AIMObject):
                if object.assetId.identificator is None or object.assetId.identificator == '':
                    raise ValueError(f'Not possible to export AIM Objects without a valid assetId.identificator. This is missing for object : {object}')

                csv_data.append(self.create_csv_row_for_AIMObject(object))

        csv_data.insert(0, self.csv_headers)

        csv_data = self.append_with_nones(csv_data)

        return csv_data

        for record in self.data:
            object = AssetFactory().dynamic_create_instance_from_uri(record[type_index])
            list_of_objects.append(object)
            for index, row in enumerate(record):
                if index == type_index:
                    continue
                if row == '':
                    continue

                if self.headers[index] in ['bron.typeURI', 'doel.typeURI']:
                    continue

                cardinality_indicator = self.settings['dotnotatie']['cardinality indicator']

                if cardinality_indicator in self.headers[index]:
                    value = row.split(self.settings['dotnotatie']['cardinality separator'])
                else:
                    value = row

                if self.headers[index] == 'geometry':
                    value = value
                    if value == '':
                        value = None
                    self.headers[index] = 'geometry'

                DotnotatieHelper.set_attribute_by_dotnotatie(instanceOrAttribute=object,
                                                             dotnotatie=self.headers[index],
                                                             value=value,
                                                             convert=True,
                                                             separator=self.settings['dotnotatie']['separator'],
                                                             cardinality_indicator=cardinality_indicator,
                                                             waarde_shortcut_applicable=self.settings['dotnotatie'][
                                                                 'waarde_shortcut_applicable'])

    def create_csv_row_for_AIMObject(self, object):
        values_list = [object.typeURI, object.assetId.identificator, object.assetId.toegekendDoor]
        while len(values_list) < len(self.csv_headers):
            values_list.append(None)

        for attribute, value in object.attributes_by_dotnotatie():
            if attribute in self.csv_headers[1:3]:
                continue

            if attribute not in self.csv_headers:
                self.csv_headers.append(attribute)
                while len(values_list) < len(self.csv_headers):
                    values_list.append(None)

            index = self.csv_headers.index(attribute)
            values_list[index] = value

        return values_list

    def append_with_nones(self, csv_data):
        header_len = len(csv_data[0])

        for row in csv_data[1:]:
            while len(row) < header_len:
                row.append(None)

        return csv_data

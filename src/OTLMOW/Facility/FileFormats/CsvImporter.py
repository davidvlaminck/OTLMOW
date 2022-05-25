import os

from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.DotnotatieHelper import DotnotatieHelper


class CsvImporter:
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

    def import_csv_file(self, file_location: str = '', delimiter=';'):
        if file_location == '' or not os.path.isfile(file_location):
            raise FileNotFoundError(f'Could not load the file at: {file_location}')

        try:
            with open(file_location, 'r') as file:
                self.headers = file.readline()[:-1].split(delimiter)
                data = []
                for line in file:
                    data.append(line[:-1].split(delimiter))
                self.data = data[1:]

        except Exception as ex:
            raise ex

        return self.create_objects_from_data()

    def create_objects_from_data(self):
        list_of_objects = []

        try:
            type_index = self.headers.index('typeURI')
        except ValueError:
            raise ValueError('The data is missing essential typeURI data')

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

        return list_of_objects
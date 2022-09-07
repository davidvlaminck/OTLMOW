import copy
from pathlib import Path

from OTLMOW.Facility.DotnotationHelper import DotnotationHelper
from OTLMOW.Facility.GenericHelper import GenericHelper
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject


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
        self.csv_data = []

    def export_to_file(self, filepath: Path = None, list_of_objects: list = None, **kwargs):
        delimiter = ';'
        split_per_type = False

        if kwargs is not None:
            if 'delimiter' in kwargs:
                delimiter = kwargs['delimiter']
            if 'split_per_type' in kwargs:
                split_per_type = kwargs['split_per_type']

        if filepath == None:
            raise ValueError(f'Can not write a file to: {filepath}')

        if delimiter == '':
            delimiter = self.settings['delimiter']
            if delimiter == '':
                delimiter = ';'

        if split_per_type:
            self.export_multiple_csv_files(list_of_objects, filepath, delimiter)
        else:
            csv_data = self.create_data_from_objects(list_of_objects)
            csv_data_lines = self.create_data_lines_from_data(csv_data, delimiter)
            self.write_file(file_location=filepath, data=csv_data_lines)

    def export_multiple_csv_files(self, list_of_objects: list, file_location: Path = None, delimiter: str = ''):
        if list_of_objects is None:
            list_of_objects = []

        types = set(map(lambda x: x.typeURI, list_of_objects))
        for object_type in types:
            filtered_objects = list(filter(lambda x: x.typeURI == object_type, list_of_objects))
            ns, name = GenericHelper.get_ns_and_name_from_uri(object_type)
            shortened_uri = ns + '_' + name
            specific_file_location = str(file_location)
            index = specific_file_location.rfind('\\')
            dir_location = specific_file_location[0:index]
            filename = specific_file_location[index+1:]
            specific_filename = filename.split('.')[0] + '_' + shortened_uri + '.' + filename.split('.')[1]
            csv_data = self.create_data_from_objects(filtered_objects)
            csv_data_lines = self.create_data_lines_from_data(csv_data, delimiter)
            self.write_file(file_location=dir_location + '\\' + specific_filename, data=csv_data_lines)

    def create_data_from_objects(self, list_of_objects: list) -> [[str]]:
        self.csv_data = []
        if list_of_objects is None or list_of_objects == []:
            raise ValueError('There is no data to export to a csv file')

        self.csv_headers = ['typeURI', 'assetId.identificator', 'assetId.toegekendDoor']

        for asset_object in list_of_objects:
            if isinstance(asset_object, AIMObject):
                if asset_object.assetId.identificator is None or asset_object.assetId.identificator == '':
                    raise ValueError(
                        f'Not possible to export AIM Objects without a valid assetId.identificator. '
                        f'This is missing for asset_object : {asset_object}')

                self.csv_data.append(self.create_csv_row_for_AIMObject(asset_object))

        self.csv_headers = self.adjust_dotnotation_by_settings(headers=self.csv_headers, settings=self.settings)
        self.csv_headers = self.sort_headers(self.csv_headers)
        self.csv_data.insert(0, self.csv_headers)

        csv_data = self.append_with_nones(self.csv_data)

        return csv_data

    def create_csv_row_for_AIMObject(self, aim_object):
        values_list = [aim_object.typeURI, aim_object.assetId.identificator, aim_object.assetId.toegekendDoor]
        while len(values_list) < len(self.csv_headers):
            values_list.append(None)

        for attribute, value in aim_object.list_attributes_and_values_by_dotnotation(
                waarde_shortcut=self.settings['dotnotation']['waarde_shortcut_applicable']):
            if attribute in self.csv_headers[1:3]:
                continue

            if attribute not in self.csv_headers:
                index = self.find_sorted_header_index(attribute)
                self.csv_headers.insert(index, attribute)
                while len(values_list) < len(self.csv_headers):
                    values_list.insert(index, None)
                    for data_row in self.csv_data:
                        if len(data_row) > 0:
                            data_row.insert(index, None)

            index = self.csv_headers.index(attribute)

            if isinstance(value, list):
                value = self.fix_cardinality_value(aim_object, attribute)
                values_list[index] = value
            else:
                values_list[index] = value

        return values_list

    @staticmethod
    def append_with_nones(csv_data):
        header_len = len(csv_data[0])

        for row in csv_data[1:]:
            while len(row) < header_len:
                row.append(None)

        return csv_data

    @staticmethod
    def adjust_dotnotation_by_settings(headers, settings):
        for index, header in enumerate(headers):
            headers[index] = header.replace('.', settings['dotnotation']['separator']) \
                .replace('[]', settings['dotnotation']['cardinality indicator'])
        return headers

    def create_data_lines_from_data(self, csv_data, delimiter):
        csv_data_lines = []
        for index, row in enumerate(csv_data):
            row = self.stringify_list(row, self.settings['dotnotation']['cardinality separator'])
            csv_data_lines.append(delimiter.join(row))
        return csv_data_lines

    @staticmethod
    def stringify_list(row: list, cardinality_seperator: str = '|'):
        for index, item in enumerate(row):
            if item is None:
                row[index] = ''
            else:
                if isinstance(item, list):
                    if len(item) == 0:
                        row[index] = ''
                    else:
                        item_string = ''
                        for item_element in item:
                            if item_element is None:
                                item_string += cardinality_seperator
                            elif isinstance(item_element, str):
                                item_string += item_element + cardinality_seperator
                            else:
                                item_string += str(item_element) + cardinality_seperator
                        item_string = item_string[:-1]
                        row[index] = item_string
                else:
                    try:
                        row[index] = str(item)
                    except TypeError:
                        row[index] = ''
        return row

    @staticmethod
    def write_file(file_location, data):
        try:
            with open(file_location, "w") as file:
                for line in data:
                    file.writelines(line + '\n')
        except Exception as ex:
            raise ex

    @staticmethod
    def sort_headers(headers):
        if headers is None or headers == []:
            return headers
        first_three = headers[0:3]
        rest = headers[3:]
        sorted_rest = sorted(rest)
        first_three.extend(sorted_rest)

        return first_three

    def find_sorted_header_index(self, attribute):
        headers = copy.copy(self.csv_headers)
        headers.append(attribute)
        headers = self.sort_headers(headers)
        return headers.index(attribute)

    def fix_cardinality_value(self, aim_object, attribute):
        actual_attributes = DotnotationHelper.get_attributes_by_dotnotation(instance_or_attribute=aim_object,
                                                                            dotnotation=attribute,
                                                                            separator='.',
                                                                            cardinality_indicator='[]',
                                                                            waarde_shortcut_applicable=False)

        if actual_attributes is None:
            return []
        if not isinstance(actual_attributes, list):
            return actual_attributes.waarde

        if self.settings['dotnotation']['waarde_shortcut_applicable']:
            first_attr = actual_attributes[0]
            if first_attr.field.waarde_shortcut_applicable:
                values_list = []
                for actual_attribute in actual_attributes:
                    if actual_attribute.waarde is not None:
                        values_list.append(actual_attribute.waarde.waarde)
                    else:
                        values_list.append(None)
            else:
                values_list = list(map(lambda x: x.waarde, actual_attributes))
        else:
            values_list = list(map(lambda x: x.waarde, actual_attributes))
        return values_list

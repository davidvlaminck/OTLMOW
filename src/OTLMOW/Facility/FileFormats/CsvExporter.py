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

    def export_csv_file(self, list_of_objects: list = [], file_location: str = '', delimiter=';'):
        if file_location == '':
            raise ValueError(f'Can not write a file to: {file_location}')

        csv_data = self.create_data_from_objects(list_of_objects)
        csv_data_lines = self.create_data_lines_from_data(csv_data)
        self.write_file(file_location=file_location, data=csv_data_lines)

    def create_data_from_objects(self, list_of_objects: list = []) -> [[str]]:
        csv_data = []
        if list_of_objects is None or list_of_objects == []:
            raise ValueError('There is no data to export to a csv file')

        self.csv_headers = ['typeURI', 'assetId.identificator', 'assetId.toegekendDoor']

        for object in list_of_objects:
            if isinstance(object, AIMObject):
                if object.assetId.identificator is None or object.assetId.identificator == '':
                    raise ValueError(
                        f'Not possible to export AIM Objects without a valid assetId.identificator. This is missing for object : {object}')

                csv_data.append(self.create_csv_row_for_AIMObject(object))

        self.csv_headers = self.adjust_dotnotatie_by_settings(headers=self.csv_headers, settings=self.settings)
        self.csv_headers = self.sort_headers(self.csv_headers)
        csv_data.insert(0, self.csv_headers)


        csv_data = self.append_with_nones(csv_data)

        return csv_data

    def create_csv_row_for_AIMObject(self, aimobject):
        values_list = [aimobject.typeURI, aimobject.assetId.identificator, aimobject.assetId.toegekendDoor]
        while len(values_list) < len(self.csv_headers):
            values_list.append(None)

        for attribute, value in aimobject.list_attributes_and_values_by_dotnotatie(
                waarde_shortcut=self.settings['dotnotatie']['waarde_shortcut_applicable']):
            if attribute in self.csv_headers[1:3]:
                continue

            if attribute not in self.csv_headers:
                self.csv_headers.append(attribute)
                while len(values_list) < len(self.csv_headers):
                    values_list.append(None)

            index = self.csv_headers.index(attribute)
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
    def adjust_dotnotatie_by_settings(headers, settings):
        for index, header in enumerate(headers):
            headers[index] = header.replace('.', settings['dotnotatie']['separator']) \
                .replace('[]', settings['dotnotatie']['cardinality indicator'])
        return headers

    def create_data_lines_from_data(self, csv_data):
        for index, row in enumerate(csv_data):
            row = self.stringify_list(row, self.settings['dotnotatie']['cardinality separator'])
            csv_data[index] = self.settings['delimiter'].join(row)
        return csv_data

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
                        row[index] = cardinality_seperator.join(item)
                else:
                    try:
                        row[index] = str(item)
                    except:
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
        first_three.extend(sorted(rest))

        return first_three


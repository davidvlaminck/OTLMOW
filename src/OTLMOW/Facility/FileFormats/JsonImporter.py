from OTLMOW.Facility.FileFormats.JsonDecoder import JsonDecoder


class JsonImporter:
    def __init__(self, settings):
        self.decoder = JsonDecoder(settings=settings)

    def import_file(self, filepath: str = '', **kwargs) -> list:
        """Imports a json file created with Davie and decodes it to OTL objects

        :param filepath: location of the file, defaults to ''
        :type: str
        :rtype: list
        :return: returns a list of OTL objects
        """

        ignore_failed_objects = False

        if kwargs is not None:
            if 'ignore_failed_objects' in kwargs:
                ignore_failed_objects = kwargs['ignore_failed_objects']

        with open(filepath, 'r') as file:
            data = file.read()
        return self.decoder.decode_json_string(data, ignore_failed_objects=ignore_failed_objects)

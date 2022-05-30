from OTLMOW.Facility.FileFormats.JsonDecoder import JsonDecoder


class DavieImporter:
    def __init__(self, settings):
        self.decoder = JsonDecoder(settings=settings)

    def import_file(self, filePath='', ignore_failed_objects=False) -> list:
        """Imports a json file creates with Davie and decodes it to OTL objects

        :param filePath: location of the file, defaults to ''
        :type: str
        :rtype: list
        :return: returns a list of OTL objects
        """
        with open(filePath, 'r') as file:
            data = file.read()
        return self.decoder.decode_json_string(data, ignore_failed_objects=ignore_failed_objects)

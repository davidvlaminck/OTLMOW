from Facility.DavieDecoder import DavieDecoder


class DavieImporter:
    def __init__(self):
        self.decoder = DavieDecoder()

    def import_file(self, filePath='') -> list:
        """Imports a json file creates with Davie and decodes it to OTL objects

        :param filePath: location of the file, defaults to ''
        :type: str
        :rtype: list
        :return: returns a list of OTL objects
        """
        with open(filePath, 'r') as file:
            data = file.read()
        return self.decoder.decode(data)

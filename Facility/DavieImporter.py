from Facility.DavieDecoder import DavieDecoder


class DavieImporter:
    def __init__(self):
        self.decoder = DavieDecoder()

    def import_file(self, filePath):
        with open(filePath, 'r') as file:
            data = file.read()
        return self.decoder.decode(data)
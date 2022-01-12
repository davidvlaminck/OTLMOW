from ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder


class DavieExporter:
    def __init__(self):
        self.encoder = OtlAssetJSONEncoder(indent=4)

    def export_objects_to_json_file(self, list_of_objects, file_path):
        encoded_json = self.encoder.encode(list_of_objects)
        self.encoder.write_json_to_file(encoded_json, file_path)

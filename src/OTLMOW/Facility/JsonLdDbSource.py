import os

from OTLMOW.Facility.EMInfraDecoder import EMInfraDecoder
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader


class JsonLdDbSource:
    def __init__(self, path_db: str):
        if not os.path.isfile(path_db):
            raise FileNotFoundError('database file not found')
        self.path_db = path_db
        self.reader = SQLDbReader(path_db)

    def get_asset_by_uuid(self, uuid: str):
        data = self.reader.performReadQuery('select jsonld from assets where uuid = :uuid',  {"uuid": uuid})
        jsonlddata = data[0][0]
        decoder = EMInfraDecoder()
        asset = decoder.decode_object(jsonlddata)
        return asset

    def get_asset_by_naampad(self, naampad: str):
        data = self.reader.performReadQuery('select jsonld from assets where naampad = :naampad',  {"naampad": naampad})
        jsonlddata = data[0][0]
        decoder = EMInfraDecoder()
        asset = decoder.decode_object(jsonlddata)
        return asset

    def get_relaties_by_bronuuid(self, bron_uuid: str):
        data = self.reader.performReadQuery('select jsonld from relaties where bronUuid = :bron_uuid', {"bron_uuid": bron_uuid})

        assetlijst = []
        for line in data:
            jsonlddata = line[0]
            decoder = EMInfraDecoder()
            asset = decoder.decode_object(jsonlddata)
            assetlijst.append(asset)

        return assetlijst

    def get_relaties_by_doeluuid(self, doel_uuid: str):
        data = self.reader.performReadQuery('select jsonld from relaties where doelUuid = :doel_uuid', {"doel_uuid": doel_uuid})

        assetlijst = []
        for line in data:
            jsonlddata = line[0]
            decoder = EMInfraDecoder()
            asset = decoder.decode_object(jsonlddata)
            assetlijst.append(asset)

        return assetlijst

    def get_relaties_by_typeURI_and_bron_or_doeluuid(self, typeURI: str, bron_or_doel_uuid: str):
        data = self.reader.performReadQuery(
            'select jsonld from relaties where typeURI = :typeURI and (bronUuid = :bron_or_doel_uuid or doelUuid = :bron_or_doel_uuid)',
            {"typeURI": typeURI, "bron_or_doel_uuid": bron_or_doel_uuid})

        assetlijst = []
        for line in data:
            jsonlddata = line[0]
            decoder = EMInfraDecoder()
            asset = decoder.decode_object(jsonlddata)
            assetlijst.append(asset)

        return assetlijst

    def get_relaties_by_bronuuid_or_doeluuid(self, bron_or_doel_uuid: str):
        data = self.reader.performReadQuery('select jsonld from relaties where bronUuid = :bron_or_doel_uuid or doelUuid = :bron_or_doel_uuid', {"bron_or_doel_uuid": bron_or_doel_uuid})

        assetlijst = []
        for line in data:
            jsonlddata = line[0]
            decoder = EMInfraDecoder()
            asset = decoder.decode_object(jsonlddata)
            assetlijst.append(asset)

        return assetlijst

    def get_relaties_by_typeURI_and_doeluuid(self, typeURI: str, doel_uuid: str):
        data = self.reader.performReadQuery('select jsonld from relaties where typeURI = :typeURI and doelUuid = :doel_uuid',
                                            {"typeURI": typeURI, "doel_uuid": doel_uuid})
        assetlijst = []
        for line in data:
            jsonlddata = line[0]
            decoder = EMInfraDecoder()
            asset = decoder.decode_object(jsonlddata)
            assetlijst.append(asset)

        return assetlijst

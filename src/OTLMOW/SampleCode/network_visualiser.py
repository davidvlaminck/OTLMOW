from timeit import default_timer as timer

from OTLMOW.Facility.JsonLdDbSource import JsonLdDbSource
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.Visualiser import Visualiser
from OTLMOW.OEFModel.Classes.GebouwLegacy import GebouwLegacy
from OTLMOW.OEFModel.Classes.HS import HS
from OTLMOW.OEFModel.Classes.HSCabineLegacy import HSCabineLegacy
from OTLMOW.OEFModel.Classes.HSDeel import HSDeel
from OTLMOW.OEFModel.Classes.Kast import Kast
from OTLMOW.OEFModel.Classes.LS import LS
from OTLMOW.OEFModel.Classes.LSDeel import LSDeel
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Classes.Onderdeel.Bevestiging import Bevestiging
from OTLMOW.OTLModel.Classes.Onderdeel.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Onderdeel.Voedt import Voedt


class AlgoritmeVoedingsbronZoeken:
    def __init__(self, jsonldsource: JsonLdDbSource):
        self.jsonldsource = jsonldsource
        self.collected_assets = []

    def use_algorithm_to_collect_assets(self, asset: AIMObject):
        self.collected_assets.append(asset)
        self.find_more_assets(asset)

    def find_more_assets(self, asset):
        doelUuid = asset.assetId.identificator[0:36]
        relaties = jsonldsource.get_relaties_by_typeURI_and_doeluuid(typeURI=Voedt.typeURI, doel_uuid=doelUuid)
        if len(relaties) == 0:
            return

        for relatie in relaties:
            self.collected_assets.append(relatie)
            andere_asset = jsonldsource.get_asset_by_uuid(relatie.bronAssetId.identificator[0:36])
            self.collected_assets.append(andere_asset)
            self.collect_if_aansluiting(andere_asset)
            self.collect_behuizing(andere_asset)
            self.find_more_assets(andere_asset)

    def collect_behuizing(self, asset):
        if asset.typeURI not in (LS.typeURI, LSDeel.typeURI, HSDeel.typeURI, HS.typeURI):
            return

        bron_or_doelUuid = asset.assetId.identificator[0:36]
        relaties = jsonldsource.get_relaties_by_typeURI_and_bron_or_doeluuid(typeURI=Bevestiging.typeURI, bron_or_doel_uuid=bron_or_doelUuid)
        if len(relaties) == 0:
            return

        for relatie in relaties:

            andere_asset_bron_uuid = relatie.bronAssetId.identificator[0:36]
            if andere_asset_bron_uuid == bron_or_doelUuid:
                andere_asset_bron_uuid = relatie.doelAssetId.identificator[0:36]
            andere_asset = jsonldsource.get_asset_by_uuid(andere_asset_bron_uuid)

            if andere_asset.typeURI in (GebouwLegacy.typeURI, Kast.typeURI, HSCabineLegacy.typeURI):
                self.collected_assets.append(relatie)
                self.collected_assets.append(andere_asset)

    def collect_if_aansluiting(self, asset):
        if asset.typeURI not in (LS.typeURI, HS.typeURI):
            return

        doelUuid = asset.assetId.identificator[0:36]
        relaties = jsonldsource.get_relaties_by_typeURI_and_doeluuid(typeURI=HoortBij.typeURI, doel_uuid=doelUuid)
        if len(relaties) == 0:
            return

        for relatie in relaties:
            self.collected_assets.append(relatie)
            andere_asset = jsonldsource.get_asset_by_uuid(relatie.bronAssetId.identificator[0:36])
            self.collected_assets.append(andere_asset)


if __name__ == '__main__':
    start = timer()

    jsonldsource = JsonLdDbSource(r'C:\resources\syncedGraphsAWVInfra.db')

    asset = jsonldsource.get_asset_by_naampad('A2X85.8/A2P85.8.K/MIV153')

    algoritme = AlgoritmeVoedingsbronZoeken(jsonldsource)
    algoritme.use_algorithm_to_collect_assets(asset)

    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\python_log.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")
    Visualiser().show(algoritme.collected_assets)

    end = timer()
    print(end-start)


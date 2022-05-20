from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.DotnotatieHelper import DotnotatieHelper


class StandaardPost:
    def __init__(self, nummer: str = '', beschrijving: str = '', meetstaateenheid: str = '', mappings=None):
        if mappings is None:
            mappings = []
        self.nummer = nummer
        self.beschrijving = beschrijving
        self.meetstaateenheid = meetstaateenheid
        self.mappings = mappings

    def get_assets_from_post(self):
        asset_factory = AssetFactory()
        lijst = []
        for mapping in self.mappings:
            asset = next((c for c in lijst if c.typeURI == mapping.typeURI), None)
            if asset is None:
                asset = asset_factory.dynamic_create_instance_from_uri(mapping.typeURI)
                lijst.append(asset)
            if mapping.defaultWaarde != '':
                DotnotatieHelper().set_attribute_by_dotnotatie(asset, mapping.dotnotatie, mapping.defaultWaarde)
        return lijst

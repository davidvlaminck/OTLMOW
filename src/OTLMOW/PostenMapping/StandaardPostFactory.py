from OTLMOW.Facility.AssetFactory import AssetFactory
from OTLMOW.Facility.DotnotatieHelper import DotnotatieHelper
from OTLMOW.OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLMOW.PostenMapping.PostenLijst import PostenLijst
from OTLMOW.PostenMapping.StandaardPost import StandaardPost


class StandaardPostFactory:
    @staticmethod
    def find_post_by_nummer(nummer: str):
        posten_lijst = PostenLijst().lijst.values()
        return next(p for p in posten_lijst if p.nummer == nummer)

    @staticmethod
    def create_assets_from_post(post: StandaardPost):
        class_loader = AssetFactory()
        lijst = []
        for mapping in post.mappings:
            asset = next((c for c in lijst if c.typeURI == mapping.typeURI), None)
            if asset is None:
                asset = class_loader.dynamic_create_instance_from_uri(mapping.typeURI)
                lijst.append(asset)
            if mapping.defaultWaarde != '':
                DotnotatieHelper.set_attribute_by_dotnotatie(asset, mapping.dotnotatie, mapping.defaultWaarde)
        return lijst

    @staticmethod
    def find_posten_from_asset_by_typeURI(otlObject: OTLAsset):
        posten_lijst = PostenLijst().lijst.values()

        mappings = [mappings for posten in posten_lijst for mappings in posten.mappings]
        results_by_uri = list(filter(lambda m: m.typeURI == otlObject.typeURI, mappings))
        postennummers = list(set(map(lambda x: x.standaardpostnummer, results_by_uri)))
        posten_lijst = list(filter(lambda m: m.nummer in postennummers, posten_lijst))
        return posten_lijst

    @staticmethod
    def find_posten_from_asset(otlObject: OTLAsset):
        posten_lijst = StandaardPostFactory.find_posten_from_asset_by_typeURI(otlObject)
        mappings = [mappings for posten in posten_lijst for mappings in posten.mappings]
        mappings_met_invulbare_attributen = list(filter(lambda m: m.isAltijdInTeVullen == 0, mappings))

        selectie = []
        selectie.extend(mappings_met_invulbare_attributen)

        for mapping in mappings_met_invulbare_attributen:
            attribuut = DotnotatieHelper.get_attributes_by_dotnotatie(otlObject, mapping.dotnotatie)
            if attribuut.field.waardeObject is not None and not attribuut.field.waarde_shortcut_applicable:
                waarde = attribuut.waarde.waarde
            else:
                waarde = attribuut.waarde
            if waarde is None:
                continue
            selectie = list(filter(lambda m: DotnotatieHelper.convert_waarde_to_correct_type(m.dotnotatie == mapping.dotnotatie and m.defaultWaarde, attribuut) == waarde, selectie))

        postennummers = list(set(map(lambda x: x.standaardpostnummer, selectie)))
        posten_lijst = list(filter(lambda m: m.nummer in postennummers, posten_lijst))
        return posten_lijst


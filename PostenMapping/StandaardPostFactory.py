from Facility.ToOTLDecoder import ToOTLDecoder
from OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLModel.ClassLoader import ClassLoader
from PostenMapping.PostenLijst import PostenLijst
from PostenMapping.StandaardPost import StandaardPost


class StandaardPostFactory:
    @staticmethod
    def find_post_by_nummer(nummer: str):
        posten_lijst = PostenLijst().lijst.values()
        return next(p for p in posten_lijst if p.nummer == nummer)

    @staticmethod
    def create_assets_from_post(post: StandaardPost):
        class_loader = ClassLoader()
        lijst = []
        for mapping in post.mappings:
            asset = next((c for c in lijst if c.typeURI == mapping.typeURI), None)
            if asset is None:
                asset = class_loader.dynamic_create_instance_from_uri(mapping.typeURI)
                lijst.append(asset)
            if mapping.defaultWaarde != '':
                ToOTLDecoder().set_value_by_dotnotatie(asset, mapping.dotnotatie, mapping.defaultWaarde)
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

        # create assets from mappings and compare with get_attribute to find matches

        for mapping in mappings_met_invulbare_attributen:
            attribuut = StandaardPostFactory.get_attribute_by_dotnotatie(otlObject, mapping.dotnotatie)
            if attribuut.field.waardeObject is not None and not attribuut.field._uses_waarde_object:
                waarde = attribuut.waarde.waarde
            else:
                waarde = attribuut.waarde
            if waarde is None:
                continue
            selectie = list(filter(lambda m: m.defaultWaarde == waarde, selectie)) # fails because defaultWaarde is a string

        postennummers = list(set(map(lambda x: x.standaardpostnummer, selectie)))
        posten_lijst = list(filter(lambda m: m.nummer in postennummers, posten_lijst))
        return posten_lijst

    @staticmethod
    def get_attribute_by_dotnotatie(instanceOrAttribute, dotnotatie):
        if '.' in dotnotatie:
            first = dotnotatie.split('.')[0]
            rest = dotnotatie.split('.', 1)[1]
            attribute = getattr(instanceOrAttribute, first)
            return StandaardPostFactory.get_attribute_by_dotnotatie(attribute, rest)
        else:
            return getattr(instanceOrAttribute, '_' + dotnotatie)



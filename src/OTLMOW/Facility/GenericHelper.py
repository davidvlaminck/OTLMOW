from collections import defaultdict

from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject


class GenericHelper:
    @staticmethod
    def count_assets_by_type(objects: [OTLObject]) -> defaultdict:
        d = defaultdict(int)
        for i in objects:
            d[i.typeURI] += 1
        return d

    @classmethod
    def remove_duplicates_in_iterable_based_on_property(cls, iterable: iter, prop: str) -> []:
        done = []
        new_iterable = []
        for item in iterable:
            item_prop = getattr(item, prop)
            if item_prop not in done:
                done.append(item_prop)
                new_iterable.append(item)
        return new_iterable

    @staticmethod
    def get_ns_and_name_from_uri(objectUri):
        if 'https://wegenenverkeer.data.vlaanderen.be/ns/' not in objectUri:
            raise ValueError(f'{objectUri} is not a valid uri to extract a namespace from')

        verkorte_uri = objectUri.split('/ns/')[1]
        verkorte_uri_array = verkorte_uri.split('#')
        return verkorte_uri_array[0], verkorte_uri_array[1]

    @staticmethod
    def get_class_directory_from_ns(ns):
        return 'Classes/' + GenericHelper.get_titlecase_ns(ns)

    @staticmethod
    def get_titlecase_ns(ns: str) -> str:
        if ns == 'abstracten':
            return 'Abstracten'
        elif ns == 'implementatieelement':
            return 'ImplementatieElement'
        elif ns == 'installatie':
            return 'Installatie'
        elif ns == 'levenscyclus':
            return 'Levenscyclus'
        elif ns == 'onderdeel':
            return 'Onderdeel'
        elif ns == 'proefenmeting':
            return 'ProefEnMeting'

    

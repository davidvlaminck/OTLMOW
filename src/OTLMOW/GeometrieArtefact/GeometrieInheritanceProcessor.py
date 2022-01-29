import copy

from OTLMOW.GeometrieArtefact.GeometrieType import GeometrieType
from OTLMOW.ModelGenerator.Inheritance import Inheritance
from OTLMOW.ModelGenerator.OSLOClass import OSLOClass


class GeometrieInheritanceProcessor:
    def __init__(self, geometrie_types: [GeometrieType], inheritances: [Inheritance], classes: [OSLOClass]):
        self.geometrie_types = geometrie_types
        self.inheritances = copy.copy(inheritances)
        self.classes = copy.copy(classes)

    def ProcessInheritances(self) -> [GeometrieType]:
        print(f'start with {len(self.geometrie_types)} geometry types and {len(self.inheritances)} inheritances')

        while len(self.inheritances) > 0:
            # zoek een inheritance en gebruik die voor een goede base class af te leiden

            inheritance = next(c for c in self.inheritances)
            base = self.search_for_valid_base_using_inheritance(inheritance.base_uri)
            self.process_inheritance_for_base(base)

        print(f'end with {len(self.geometrie_types)} geometry types and {len(self.inheritances)} inheritances')
        return self.geometrie_types

    def search_for_valid_base_using_inheritance(self, base):
        inheritances = list(filter(lambda i: i.base_uri == base, self.inheritances))
        if len(inheritances) == 0:
            return base
        for inheritance in inheritances:
            sub_inheritances = list(filter(lambda i: i.base_uri == inheritance.class_uri, self.inheritances))
            if len(sub_inheritances) > 0:
                return self.search_for_valid_base_using_inheritance(inheritance.class_uri)
        return base

    def process_inheritance_for_base(self, base):
        inheritances = list(filter(lambda i: i.base_uri == base, self.inheritances))
        if len(inheritances) == 0:
            return

        i = 0
        first_geo = None
        while first_geo is None and i <= len(inheritances):
            try:
                first_geo = next(g for g in self.geometrie_types if g.objectUri == inheritances[i].class_uri)
            except Exception:
                i += 1
        if first_geo is not None:
            same_geo_type = True
            for inheritance in inheritances:
                try:
                    concrete = next(g for g in self.geometrie_types if g.objectUri == inheritance.class_uri)
                    if concrete.geen_geometrie != first_geo.geen_geometrie or concrete.punt3D != first_geo.punt3D or concrete.lijn3D != first_geo.lijn3D or concrete.polygoon3D != first_geo.polygoon3D:
                        same_geo_type = False
                        break
                except StopIteration:
                    pass

            if same_geo_type:
                new_geo_type = copy.copy(first_geo)
                new_geo_type.objectUri = base
                new_geo_type.label_nl = next(g for g in self.classes if g.objectUri == base).label
                self.geometrie_types.append(new_geo_type)
                print(f'able to inherit geometry type for classes with base {inheritances[0].base_name}')
                for inheritance in inheritances:
                    try:
                        current_geo_type = next(g for g in self.geometrie_types if g.objectUri == inheritance.class_uri)
                        self.geometrie_types.remove(current_geo_type)
                    except StopIteration:
                        pass

        for inheritance in inheritances:
            self.inheritances.remove(inheritance)


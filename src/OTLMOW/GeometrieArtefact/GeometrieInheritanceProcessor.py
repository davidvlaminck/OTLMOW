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

        # per type geo nakijken of alle inheritance classes dezelfde waarde hebben
        # één None waarde betekent geen overerving van geo type

        no_None_types = True
        geen = 1
        point = 1
        line = 1
        polygon = 1

        for inheritance in inheritances:
            geo_type = next((g for g in self.geometrie_types if g.objectUri == inheritance.class_uri), None)
            if geo_type is None:
                no_None_types = False
                break
            if geen == 1 and geo_type.geen_geometrie == 0:
                geen = 0
            if point == 1 and geo_type.punt3D == 0:
                point = 0
            if line == 1 and geo_type.lijn3D == 0:
                line = 0
            if polygon == 1 and geo_type.polygoon3D == 0:
                polygon = 0

        if no_None_types and (geen + point + line + polygon > 0):
            new_geo_type = GeometrieType()
            new_geo_type.objectUri = base
            new_geo_type.label_nl = next(g for g in self.classes if g.objectUri == base).label
            new_geo_type.geen_geometrie = geen
            new_geo_type.punt3D = point
            new_geo_type.lijn3D = line
            new_geo_type.polygoon3D = polygon

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


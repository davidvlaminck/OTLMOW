import copy

from OTLMOW.GeometrieArtefact.GeometrieType import GeometrieType
from OTLMOW.ModelGenerator.Inheritance import Inheritance
from OTLMOW.ModelGenerator.OSLOClass import OSLOClass


class GeometrieInheritanceProcessor:
    def __init__(self, geometrie_types: [GeometrieType], inheritances: [Inheritance], classes: [OSLOClass]):
        self.geometrie_types = geometrie_types
        self.inheritances = inheritances
        self.classes = classes

    def ProcessInheritances(self) -> [GeometrieType]:
        processed = []

        while len(self.inheritances) > 0:
            # zoek een concrete class en neem daar een inheritance van (> 1 mogelijk)
            concrete_class = next(c for c in self.classes if c.abstract == 0)
            if concrete_class is None:
                break
            for inheritance in list(filter(lambda i: i.class_uri == concrete_class.objectUri, self.inheritances)):
                base = inheritance.base_uri
                self.process_inheritance_for_base_with_only_concrete_inheritors(base)


            # elke keer vertrekken van concrete classes dan naar benden en terug naar boven in volgorde zodat geen enkele inheritance gemist wordt
            # kan alleen als alle classes concrete zijn ofwel de inheritance reeds is doorgebubbeld

        return self.geometrie_types

    def process_inheritance_for_base_with_only_concrete_inheritors(self, base):
        inheritances = list(filter(lambda i: i.base_uri == base, self.inheritances))
        if len(inheritances) == 0:
            return
        first_concrete = inheritances[0].class_uri
        first_geo = next(g for g in self.geometrie_types if g.objectUri == first_concrete)
        same_geo_type = True
        for inheritance in inheritances:
            concrete = next(g for g in self.geometrie_types if g.objectUri == inheritance.class_uri)
            if concrete.geen_geometrie != first_geo.geen_geometrie or concrete.punt3D != first_geo.punt3D or concrete.lijn3D != first_geo.lijn3D or concrete.polygoon3D != first_geo.polygoon3D:
                same_geo_type = False
                break
        if same_geo_type:
            new_geo_type = copy.copy(first_geo)
            new_geo_type.objectUri = base
            new_geo_type.label_nl = next(g for g in self.classes if g.objectUri == base).label
            for inheritance in inheritances:
                current_geo_type = next(g for g in self.geometrie_types if g.objectUri == inheritance.class_uri)
                self.geometrie_types.remove(current_geo_type)
            self.geometrie_types.append(new_geo_type)

        for inheritance in inheritances:
            self.inheritances.remove(inheritance)

        base_inheritances = list(filter(lambda i: i.class_uri == base, self.inheritances))
        for base_inheritance in base_inheritances:
            # check of de base inheritance non-concrete classes heeft, zo ja, ga eerst verder omhoog

            self.process_inheritance_for_base(base_inheritance.base_uri)

# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Inloopbehuizing import Inloopbehuizing
from OTLMOW.OTLModel.Datatypes.KlCabineAardingsstelsel import KlCabineAardingsstelsel
from OTLMOW.OTLModel.Datatypes.KlCabineStandaardtype import KlCabineStandaardtype
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cabine(Inloopbehuizing, VlakGeometrie):
    """Een behuizing voornamelijk bestemd voor het beschermen van elektromechanische technieken waarin het omwille van de grootte en toegankelijkheid mogelijk is om rond te lopen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Inloopbehuizing.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator')

        self._aardingsstelsel = OTLAttribuut(field=KlCabineAardingsstelsel,
                                             naam='aardingsstelsel',
                                             label='aardingsstelsel',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.aardingsstelsel',
                                             definition='Keuze tussen verschillende types voor het gebruikte aardingsstelsel.',
                                             owner=self)

        self._kelderdiepte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='kelderdiepte',
                                          label='kelderdiepte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.kelderdiepte',
                                          definition='Binnenhoogte in meter van de kabelkelder onder de cabine.',
                                          owner=self)

        self._standaardtype = OTLAttribuut(field=KlCabineStandaardtype,
                                           naam='standaardtype',
                                           label='standaardtype',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine.standaardtype',
                                           definition='Het type van de cabine volgens de gangbare standaarden.',
                                           owner=self)

    @property
    def aardingsstelsel(self):
        """Keuze tussen verschillende types voor het gebruikte aardingsstelsel."""
        return self._aardingsstelsel.get_waarde()

    @aardingsstelsel.setter
    def aardingsstelsel(self, value):
        self._aardingsstelsel.set_waarde(value, owner=self)

    @property
    def kelderdiepte(self):
        """Binnenhoogte in meter van de kabelkelder onder de cabine."""
        return self._kelderdiepte.get_waarde()

    @kelderdiepte.setter
    def kelderdiepte(self, value):
        self._kelderdiepte.set_waarde(value, owner=self)

    @property
    def standaardtype(self):
        """Het type van de cabine volgens de gangbare standaarden."""
        return self._standaardtype.get_waarde()

    @standaardtype.setter
    def standaardtype(self, value):
        self._standaardtype.set_waarde(value, owner=self)

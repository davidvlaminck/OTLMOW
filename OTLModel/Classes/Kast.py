# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.Behuizing import Behuizing
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kast(Behuizing):
    """Abstracte voor allerlei types kasten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._afmeting = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.afmeting',
                                      definition='Buitenafmeting van de kast als maximale breedte, lengte en hoogte in millimeter.')

        self._heeftVerlichting = OTLAttribuut(field=BooleanField,
                                              naam='heeftVerlichting',
                                              label='heeft verlichting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.heeftVerlichting',
                                              definition='Geeft aan of er verlichting aanwezig is binnen de kast.')

        self._indelingsplan = OTLAttribuut(field=DtcDocument,
                                           naam='indelingsplan',
                                           label='indelingsplan',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.indelingsplan',
                                           definition='Schematisch overzicht van de indeling van de kast volgens de aanwezige technieken in vooraanzicht.')

        self._kastmateriaal = OTLAttribuut(field=KlAlgMateriaal,
                                           naam='kastmateriaal',
                                           label='kastmateriaal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.kastmateriaal',
                                           definition='Materiaal waaruit de kast is opgebouwd.')

    @property
    def afmeting(self):
        """Buitenafmeting van de kast als maximale breedte, lengte en hoogte in millimeter."""
        return self._afmeting.waarde

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def heeftVerlichting(self):
        """Geeft aan of er verlichting aanwezig is binnen de kast."""
        return self._heeftVerlichting.waarde

    @heeftVerlichting.setter
    def heeftVerlichting(self, value):
        self._heeftVerlichting.set_waarde(value, owner=self)

    @property
    def indelingsplan(self):
        """Schematisch overzicht van de indeling van de kast volgens de aanwezige technieken in vooraanzicht."""
        return self._indelingsplan.waarde

    @indelingsplan.setter
    def indelingsplan(self, value):
        self._indelingsplan.set_waarde(value, owner=self)

    @property
    def kastmateriaal(self):
        """Materiaal waaruit de kast is opgebouwd."""
        return self._kastmateriaal.waarde

    @kastmateriaal.setter
    def kastmateriaal(self, value):
        self._kastmateriaal.set_waarde(value, owner=self)

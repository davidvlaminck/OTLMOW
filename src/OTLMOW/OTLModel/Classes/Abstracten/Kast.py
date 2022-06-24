# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.Behuizing import Behuizing
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kast(Behuizing, PuntGeometrie, VlakGeometrie):
    """Abstracte voor allerlei types kasten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Behuizing.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._afmeting = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.afmeting',
                                      definition='Buitenafmeting van de kast als maximale breedte, lengte en hoogte in millimeter.',
                                      owner=self)

        self._heeftVerlichting = OTLAttribuut(field=BooleanField,
                                              naam='heeftVerlichting',
                                              label='heeft verlichting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.heeftVerlichting',
                                              definition='Geeft aan of er verlichting aanwezig is binnen de kast.',
                                              owner=self)

        self._indelingsplan = OTLAttribuut(field=DtcDocument,
                                           naam='indelingsplan',
                                           label='indelingsplan',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.indelingsplan',
                                           definition='Schematisch overzicht van de indeling van de kast volgens de aanwezige technieken in vooraanzicht.',
                                           owner=self)

        self._kastmateriaal = OTLAttribuut(field=KlAlgMateriaal,
                                           naam='kastmateriaal',
                                           label='kastmateriaal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast.kastmateriaal',
                                           definition='Materiaal waaruit de kast is opgebouwd.',
                                           owner=self)

    @property
    def afmeting(self):
        """Buitenafmeting van de kast als maximale breedte, lengte en hoogte in millimeter."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def heeftVerlichting(self):
        """Geeft aan of er verlichting aanwezig is binnen de kast."""
        return self._heeftVerlichting.get_waarde()

    @heeftVerlichting.setter
    def heeftVerlichting(self, value):
        self._heeftVerlichting.set_waarde(value, owner=self)

    @property
    def indelingsplan(self):
        """Schematisch overzicht van de indeling van de kast volgens de aanwezige technieken in vooraanzicht."""
        return self._indelingsplan.get_waarde()

    @indelingsplan.setter
    def indelingsplan(self, value):
        self._indelingsplan.set_waarde(value, owner=self)

    @property
    def kastmateriaal(self):
        """Materiaal waaruit de kast is opgebouwd."""
        return self._kastmateriaal.get_waarde()

    @kastmateriaal.setter
    def kastmateriaal(self, value):
        self._kastmateriaal.set_waarde(value, owner=self)

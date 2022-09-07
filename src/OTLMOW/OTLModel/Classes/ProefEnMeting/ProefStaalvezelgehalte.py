# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefStaalvezelgehalte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de hoeveelheid staalvezels in de cementbetonverharding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStaalvezelgehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

        self._staalvezelgehalte = OTLAttribuut(field=DtcDocument,
                                               naam='staalvezelgehalte',
                                               label='staalvezelgehalte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStaalvezelgehalte.staalvezelgehalte',
                                               definition='Het resultaat van de test van het gemeten staalvezelgehalte in de BV laag.',
                                               owner=self)

    @property
    def staalvezelgehalte(self):
        """Het resultaat van de test van het gemeten staalvezelgehalte in de BV laag."""
        return self._staalvezelgehalte.get_waarde()

    @staalvezelgehalte.setter
    def staalvezelgehalte(self, value):
        self._staalvezelgehalte.set_waarde(value, owner=self)

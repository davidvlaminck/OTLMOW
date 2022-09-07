# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefTextuurdiepte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de uitwasdiepte van de verharding na een oppervlaktebehandeling volgens NBN EN ISO 13473-1."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

        self._textuurdiepte = OTLAttribuut(field=DtcDocument,
                                           naam='textuurdiepte',
                                           label='textuurdiepte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte.textuurdiepte',
                                           definition='Proefresultaten van de textuurdiepte van de toplaag.',
                                           owner=self)

    @property
    def textuurdiepte(self):
        """Proefresultaten van de textuurdiepte van de toplaag."""
        return self._textuurdiepte.get_waarde()

    @textuurdiepte.setter
    def textuurdiepte(self, value):
        self._textuurdiepte.set_waarde(value, owner=self)

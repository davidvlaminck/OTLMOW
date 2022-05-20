# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPctHolleruimte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef om het percentage holle ruimte in een bitumineuze laag te bepalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._pctHolleruimte = OTLAttribuut(field=DtcDocument,
                                            naam='pctHolleruimte',
                                            label='pct holleruimte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte.pctHolleruimte',
                                            definition='Het resultaat van het aantal percentage holleruimte meting aanwezig in de laag.',
                                            owner=self)

    @property
    def pctHolleruimte(self):
        """Het resultaat van het aantal percentage holleruimte meting aanwezig in de laag."""
        return self._pctHolleruimte.get_waarde()

    @pctHolleruimte.setter
    def pctHolleruimte(self, value):
        self._pctHolleruimte.set_waarde(value, owner=self)

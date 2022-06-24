# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefEffectiefBindmiddelgehalte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de hoeveelheid bitumen, uitgedrukt t.o.v. het totale mengsel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._effectiefBindmiddelgehalte = OTLAttribuut(field=DtcDocument,
                                                        naam='effectiefBindmiddelgehalte',
                                                        label='effectief bindmiddelgehalte',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte.effectiefBindmiddelgehalte',
                                                        definition='Het resultaat van de test van het gemeten effectief bindmiddelgehalte in de BV laag.',
                                                        owner=self)

    @property
    def effectiefBindmiddelgehalte(self):
        """Het resultaat van de test van het gemeten effectief bindmiddelgehalte in de BV laag."""
        return self._effectiefBindmiddelgehalte.get_waarde()

    @effectiefBindmiddelgehalte.setter
    def effectiefBindmiddelgehalte(self, value):
        self._effectiefBindmiddelgehalte.set_waarde(value, owner=self)

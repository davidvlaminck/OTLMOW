# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefEffectiefBindmiddelgehalte(Proef):
    """Bepaling van de hoeveelheid bitumen, uitgedrukt t.o.v. het totale mengsel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._effectiefBindmiddelgehalte = OTLAttribuut(field=DtcDocument,
                                                        naam='effectiefBindmiddelgehalte',
                                                        label='effectief bindmiddelgehalte',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte.effectiefBindmiddelgehalte',
                                                        definition='Het resultaat van de test van het gemeten effectief bindmiddelgehalte in de BV laag.')

    @property
    def effectiefBindmiddelgehalte(self):
        """Het resultaat van de test van het gemeten effectief bindmiddelgehalte in de BV laag."""
        return self._effectiefBindmiddelgehalte.waarde

    @effectiefBindmiddelgehalte.setter
    def effectiefBindmiddelgehalte(self, value):
        self._effectiefBindmiddelgehalte.set_waarde(value, owner=self)

# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefBindmiddeldosering(Proef):
    """Proef om de hoeveelheid bindmiddel te bepalen die nodig is om de grond als funderingslaag te garanderen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBindmiddeldosering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._technischVerslagBindmiddeldosering = OTLAttribuut(field=DtcDocument,
                                                                naam='technischVerslagBindmiddeldosering',
                                                                label='technisch verslag bindmiddeldosering',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBindmiddeldosering.technischVerslagBindmiddeldosering',
                                                                definition='Het technisch verslag van een aangewezen bindmiddeldosering.')

    @property
    def technischVerslagBindmiddeldosering(self):
        """Het technisch verslag van een aangewezen bindmiddeldosering."""
        return self._technischVerslagBindmiddeldosering.waarde

    @technischVerslagBindmiddeldosering.setter
    def technischVerslagBindmiddeldosering(self, value):
        self._technischVerslagBindmiddeldosering.set_waarde(value, owner=self)

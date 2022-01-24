# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPctHolleruimte(Proef):
    """Proef om het percentage holle ruimte in een bitumineuze laag te bepalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._pctHolleruimte = OTLAttribuut(field=DtcDocument,
                                            naam='pctHolleruimte',
                                            label='pct holleruimte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte.pctHolleruimte',
                                            definition='Het resultaat van het aantal percentage holleruimte meting aanwezig in de laag.')

    @property
    def pctHolleruimte(self):
        """Het resultaat van het aantal percentage holleruimte meting aanwezig in de laag."""
        return self._pctHolleruimte.waarde

    @pctHolleruimte.setter
    def pctHolleruimte(self, value):
        self._pctHolleruimte.set_waarde(value, owner=self)

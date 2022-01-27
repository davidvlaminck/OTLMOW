# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Kast import Kast
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class IndoorKast(Kast):
    """Behuizing in de vorm van een kast voor gebruik in binnenruimtes."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IndoorKast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._mplan = OTLAttribuut(field=DtcDocument,
                                   naam='mplan',
                                   label='m-plan',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IndoorKast.mplan',
                                   usagenote='Bestanden van het type dwg of pdf.',
                                   kardinaliteit_max='*',
                                   definition='Mechanisch plan van de volledige installatie. Er wordt 1 plan toegevoegd per installatie/techniek die op de kast is aangesloten.')

    @property
    def mplan(self):
        """Mechanisch plan van de volledige installatie. Er wordt 1 plan toegevoegd per installatie/techniek die op de kast is aangesloten."""
        return self._mplan.waarde

    @mplan.setter
    def mplan(self, value):
        self._mplan.set_waarde(value, owner=self)

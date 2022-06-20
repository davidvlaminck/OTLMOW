# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Beginstuk import Beginstuk
from OTLMOW.OTLModel.Datatypes.KlLEACUitbuigingstype import KlLEACUitbuigingstype


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietGetestBeginstuk(Beginstuk):
    """Een niet-gecertificeerd begin aan een geleideconstructie, aan de stroomopwaartse zijde ten opzichte van de meest nabij gelegen rijstrook."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietGetestBeginstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._uitbuigingstype = OTLAttribuut(field=KlLEACUitbuigingstype,
                                             naam='uitbuigingstype',
                                             label='uitbuigingstype',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietGetestBeginstuk.uitbuigingstype',
                                             definition='Niet getest beginstuk dat uitbuigt weg van de weg in grondplan.',
                                             owner=self)

    @property
    def uitbuigingstype(self):
        """Niet getest beginstuk dat uitbuigt weg van de weg in grondplan."""
        return self._uitbuigingstype.get_waarde()

    @uitbuigingstype.setter
    def uitbuigingstype(self, value):
        self._uitbuigingstype.set_waarde(value, owner=self)

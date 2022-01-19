# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from OTLModel.Datatypes.KlCalamiteitsbordType import KlCalamiteitsbordType
from OTLModel.Datatypes.KlCalamiteitsbordVorm import KlCalamiteitsbordVorm


# Generated with OTLClassCreator. To modify: extend, do not edit
class CalamiteitsBord(RetroreflecterendVerkeersbord, AttributeInfo):
    """De aanwijzingsborden ter plaatse van een startpunt, een aantakpunt, een wissel- of koppelpunt van een omleggingsroute bij calamiteiten zijn geïntegreerd in een één-bordsysteem met een scharnierende plaat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CalamiteitsBord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        RetroreflecterendVerkeersbord.__init__(self)

        self._calamiteitsbordType = OTLAttribuut(field=KlCalamiteitsbordType,
                                                 naam='calamiteitsbordType',
                                                 label='calamiteitsbord type',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CalamiteitsBord.calamiteitsbordType',
                                                 definition='Het type van calamiteitsbord (bv. draaiend of dragend).')

        self._vorm = OTLAttribuut(field=KlCalamiteitsbordVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CalamiteitsBord.vorm',
                                  definition='De vorm van het calamiteitsbord.')

    @property
    def calamiteitsbordType(self):
        """Het type van calamiteitsbord (bv. draaiend of dragend)."""
        return self._calamiteitsbordType.waarde

    @calamiteitsbordType.setter
    def calamiteitsbordType(self, value):
        self._calamiteitsbordType.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """De vorm van het calamiteitsbord."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)

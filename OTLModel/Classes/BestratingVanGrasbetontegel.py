# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.KlBestratingOpvulsoort import KlBestratingOpvulsoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanGrasbetontegel(Bestrating, AttributeInfo):
    """Bestrating van grasbetontegels."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGrasbetontegel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Bestrating.__init__(self)

        self._vulling = OTLAttribuut(field=KlBestratingOpvulsoort,
                                     naam='vulling',
                                     label='vulling',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGrasbetontegel.vulling',
                                     definition='Het gebruikte materiaal als toevoeging in de vrije openingen van de tegels.')

    @property
    def vulling(self):
        """Het gebruikte materiaal als toevoeging in de vrije openingen van de tegels."""
        return self._vulling.waarde

    @vulling.setter
    def vulling(self, value):
        self._vulling.set_waarde(value, owner=self)

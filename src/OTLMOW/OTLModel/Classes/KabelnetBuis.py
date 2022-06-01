# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.URIField import URIField


# Generated with OTLClassCreator. To modify: extend, do not edit
class KabelnetBuis(AIMNaamObject):
    """Koppeling met het corresponderend object in Kabelnet die toegang geeft tot de informatie die in Kabelnet bewaard wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetBuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._kabelnetBuisId = OTLAttribuut(field=IntegerField,
                                            naam='kabelnetBuisId',
                                            label='kabelnetbuis ID',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetBuis.kabelnetBuisId',
                                            definition='Uniek nummer uit de Kabelnet toepassing dat de betrokken beschermbuis identificeert.',
                                            owner=self)

        self._kabelnetURL = OTLAttribuut(field=URIField,
                                         naam='kabelnetURL',
                                         label='kabelnet URL',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetBuis.kabelnetURL',
                                         definition='De URL waarmee het corresponderend object in Kabelnet rechtstreeks gevonden kan worden in de Kabelnet-toepassing.',
                                         owner=self)

    @property
    def kabelnetBuisId(self):
        """Uniek nummer uit de Kabelnet toepassing dat de betrokken beschermbuis identificeert."""
        return self._kabelnetBuisId.get_waarde()

    @kabelnetBuisId.setter
    def kabelnetBuisId(self, value):
        self._kabelnetBuisId.set_waarde(value, owner=self)

    @property
    def kabelnetURL(self):
        """De URL waarmee het corresponderend object in Kabelnet rechtstreeks gevonden kan worden in de Kabelnet-toepassing."""
        return self._kabelnetURL.get_waarde()

    @kabelnetURL.setter
    def kabelnetURL(self, value):
        self._kabelnetURL.set_waarde(value, owner=self)

# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Bestrating import Bestrating
from OTLMOW.OTLModel.Datatypes.KlBestratingOpvulsoort import KlBestratingOpvulsoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerhardingGrasKunststofplaat(Bestrating):
    """Gras/grind-kunststofplaten zijn kunststofplaten met raatvormige structuur die aangewend worden voor het wapenen van grasmatten. Ze voldoen aan de voorschriften van PTV 828. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerhardingGrasKunststofplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._vulling = OTLAttribuut(field=KlBestratingOpvulsoort,
                                     naam='vulling',
                                     label='vulling',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerhardingGrasKunststofplaat.vulling',
                                     definition='Het gebruikte materiaal als toevoeging in de vrije openingen van de gras-kunststofplaten.',
                                     owner=self)

    @property
    def vulling(self):
        """Het gebruikte materiaal als toevoeging in de vrije openingen van de gras-kunststofplaten."""
        return self._vulling.get_waarde()

    @vulling.setter
    def vulling(self, value):
        self._vulling.set_waarde(value, owner=self)

# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.VRIDraagconstructie import VRIDraagconstructie
from OTLMOW.OTLModel.Datatypes.KlRechteSteunType import KlRechteSteunType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RechteSteun(VRIDraagconstructie, PuntGeometrie):
    """Rechte paal voor het steun geven aan allerlei installaties. Dit omvat het volledige draagsysteem, zijnde de logische samenstelling van met elkaar verbonden onderdelen, bestemd voor het geven van mechanische sterkte en stabiliteit aan de installatie voor wegsignalering.
Afhankelijk van het gekozen model kan de rechte steun bestemd zijn voor: verkeerslichten (A-paal, D-paal en zwanenhals), variabele zone 30, bi-flash of andere installaties."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RechteSteun'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        VRIDraagconstructie.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30')

        self._type = OTLAttribuut(field=KlRechteSteunType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RechteSteun.type',
                                  definition='Het type verwijst naar de aanpassingen die gebeuren wanneer een andere techniek gebruik maakt van de rechte steun. Meestal gaat dit over een aanpassing in de lengte van het verjongde deel van de rechte steun.',
                                  owner=self)

    @property
    def type(self):
        """Het type verwijst naar de aanpassingen die gebeuren wanneer een andere techniek gebruik maakt van de rechte steun. Meestal gaat dit over een aanpassing in de lengte van het verjongde deel van de rechte steun."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

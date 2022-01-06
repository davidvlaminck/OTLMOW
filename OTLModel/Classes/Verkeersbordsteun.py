from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Classes.Draagconstructie import Draagconstructie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from OTLModel.Datatypes.KlVerkeersbordsteunType import KlVerkeersbordsteunType
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbordsteun(AIMNaamObject, Draagconstructie):
    """Een draagconstructie voor verkeersborden of pictogrammen. Dit kan een ronde paal of een vakwerksteun zijn."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Draagconstructie.__init__(self)

        self.fabricagevoorschrift = StringField(naam="fabricagevoorschrift",
                                                label="fabricagevoorschrift",
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.fabricagevoorschrift",
                                                definition="Genormaliseerde referentie waaraan het infrastructuur element aan voldoet.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Genormaliseerde referentie waaraan het infrastructuur element aan voldoet."""

        self.lengte = KwantWrdInMeter()
        """De lengte van de verkeersbordpaal in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengte"
        self.lengte.definition = "De lengte van de verkeersbordpaal in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.lengteBovengronds = KwantWrdInMeter()
        """De bovengrondse lengte van de verkeersbordpaal in meter."""
        self.lengteBovengronds.naam = "lengteBovengronds"
        self.lengteBovengronds.label = "lengte bovengronds"
        self.lengteBovengronds.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengteBovengronds"
        self.lengteBovengronds.definition = "De bovengrondse lengte van de verkeersbordpaal in meter."
        self.lengteBovengronds.constraints = ""
        self.lengteBovengronds.usagenote = ""
        self.lengteBovengronds.deprecated_version = ""

        self.lengteOndergronds = KwantWrdInMeter()
        """De ondergrondse lengte van de verkeersbordpaal in meter."""
        self.lengteOndergronds.naam = "lengteOndergronds"
        self.lengteOndergronds.label = "lengte ondergronds"
        self.lengteOndergronds.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengteOndergronds"
        self.lengteOndergronds.definition = "De ondergrondse lengte van de verkeersbordpaal in meter."
        self.lengteOndergronds.constraints = ""
        self.lengteOndergronds.usagenote = ""
        self.lengteOndergronds.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlVerkeersbordsteunType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.type",
                                    definition="Het type verkeersbordpaal.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type verkeersbordpaal."""

        self.wanddikte = KwantWrdInMillimeter()
        """De dikte van de wand in millimeter."""
        self.wanddikte.naam = "wanddikte"
        self.wanddikte.label = "wanddikte"
        self.wanddikte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.wanddikte"
        self.wanddikte.definition = "De dikte van de wand in millimeter."
        self.wanddikte.constraints = ""
        self.wanddikte.usagenote = ""
        self.wanddikte.deprecated_version = ""

        self.diameter = KwantWrdInMillimeter()
        """De diameter van de verkeersbordpaal in millimeter."""
        self.diameter.naam = "diameter"
        self.diameter.label = "diameter"
        self.diameter.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.diameter"
        self.diameter.definition = "De diameter van de verkeersbordpaal in millimeter."
        self.diameter.constraints = ""
        self.diameter.usagenote = ""
        self.diameter.deprecated_version = ""

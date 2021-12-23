from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBeheerExoten import KlBeheerExoten
from OTLModel.Datatypes.KlNazorgJaarfrequentie import KlNazorgJaarfrequentie
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator
class BeheerExoten(AIMObject):
    """Het beheerobject voor de exoten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.beheeroptie = KeuzelijstField(naam="beheeroptie",
                                           label="beheeroptie",
                                           lijst=KlBeheerExoten(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.beheeroptie",
                                           definition="Behandelingswijzen van exoten.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Behandelingswijzen van exoten."""

        self.bijzondereAfvoerVereist = BooleanField(naam="bijzondereAfvoerVereist",
                                                    label="bijzondere afvoer vereist",
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.bijzondereAfvoerVereist",
                                                    definition="Aanduiding of voor de verwijderde exoten een niet-reguliere afvoer is voorzien.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """Aanduiding of voor de verwijderde exoten een niet-reguliere afvoer is voorzien."""

        self.heeftDeponie = BooleanField(naam="heeftDeponie",
                                         label="heeft deponie",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.heeftDeponie",
                                         definition="Aanduiding of de Japanse duizendknoop terplaatse kan worden gedeponeerd in een gecontamineerde zone.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Aanduiding of de Japanse duizendknoop terplaatse kan worden gedeponeerd in een gecontamineerde zone."""

        self.nazorgJaarfrequentie = KeuzelijstField(naam="nazorgJaarfrequentie",
                                                    label="nazorg jaarfrequentie",
                                                    lijst=KlNazorgJaarfrequentie(),
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.nazorgJaarfrequentie",
                                                    definition="Aantal keer dat de behandelde zone jaarlijks dient te worden gecontroleerd.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """Aantal keer dat de behandelde zone jaarlijks dient te worden gecontroleerd."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte in vierkante meter van de te behandelen exoten."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerExoten.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte in vierkante meter van de te behandelen exoten."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

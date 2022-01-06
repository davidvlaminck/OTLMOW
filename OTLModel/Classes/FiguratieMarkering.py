from OTLModel.Classes.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlFiguratieCode import KlFiguratieCode
from OTLModel.Datatypes.KlFiguratieSoort import KlFiguratieSoort
from OTLModel.Datatypes.KlFiguratieType import KlFiguratieType
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class FiguratieMarkering(FiguratieMarkeringToegang):
    """Een markering als figuratie op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.code = KeuzelijstField(naam="code",
                                    label="code",
                                    lijst=KlFiguratieCode(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering.code",
                                    definition="De code van de figuratie markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De code van de figuratie markering."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van de markering zoals beschreven in de algemene omzendbrief."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van de markering zoals beschreven in de algemene omzendbrief."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.soortOmschrijving = KeuzelijstField(naam="soortOmschrijving",
                                                 label="soort omschrijving",
                                                 lijst=KlFiguratieSoort(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering.soortOmschrijving",
                                                 definition="De soort en tevens de omschrijving van de figuratie markering.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De soort en tevens de omschrijving van de figuratie markering."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlFiguratieType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkering.type",
                                    definition="Het type van figuratie markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van figuratie markering."""

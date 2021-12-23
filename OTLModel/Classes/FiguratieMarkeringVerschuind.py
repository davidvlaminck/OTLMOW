from OTLModel.Classes.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlFiguratieCodeVerschuind import KlFiguratieCodeVerschuind
from OTLModel.Datatypes.KlFiguratieSoortVerschuind import KlFiguratieSoortVerschuind
from OTLModel.Datatypes.KlFiguratieTypeVerschuind import KlFiguratieTypeVerschuind
from OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator
class FiguratieMarkeringVerschuind(FiguratieMarkeringToegang):
    """Een schuine markering als figuratie op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.basisOppervlakte = KwantWrdInVierkanteMeter()
        """De (basis) oppervlakte van de markering zoals beschreven in de algemene omzendbrief."""
        self.basisOppervlakte.naam = "basisOppervlakte"
        self.basisOppervlakte.label = "basisoppervlakte"
        self.basisOppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.basisOppervlakte"
        self.basisOppervlakte.definition = "De (basis) oppervlakte van de markering zoals beschreven in de algemene omzendbrief."
        self.basisOppervlakte.constraints = ""
        self.basisOppervlakte.usagenote = ""
        self.basisOppervlakte.deprecated_version = ""

        self.code = KeuzelijstField(naam="code",
                                    label="code",
                                    lijst=KlFiguratieCodeVerschuind(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.code",
                                    definition="De code van de verschuinde figuratie markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De code van de verschuinde figuratie markering."""

        self.hoek = KwantWrdInDecimaleGraden()
        """De hoek van de verschuinde figuratiemarkering in decimale graden."""
        self.hoek.naam = "hoek"
        self.hoek.label = "hoek"
        self.hoek.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.hoek"
        self.hoek.definition = "De hoek van de verschuinde figuratiemarkering in decimale graden."
        self.hoek.constraints = ""
        self.hoek.usagenote = ""
        self.hoek.deprecated_version = ""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van de figuratie markering na verschuining."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van de figuratie markering na verschuining."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.soortOmschrijving = KeuzelijstField(naam="soortOmschrijving",
                                                 label="soort omschrijving",
                                                 lijst=KlFiguratieSoortVerschuind(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.soortOmschrijving",
                                                 definition="De soort en tevens de omschrijving van de verschuinde figuratie markering.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De soort en tevens de omschrijving van de verschuinde figuratie markering."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlFiguratieTypeVerschuind(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FiguratieMarkeringVerschuind.type",
                                    definition="Het type van de verschuinde figuratie markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de verschuinde figuratie markering."""

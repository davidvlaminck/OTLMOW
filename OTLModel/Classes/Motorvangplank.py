from OTLModel.Classes.AfschermendeConstructie import AfschermendeConstructie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACSchokindexMVP import KlLEACSchokindexMVP
from OTLModel.Datatypes.KlLEACSnelheidsklasse import KlLEACSnelheidsklasse
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Motorvangplank(AfschermendeConstructie):
    """Een constructie geïnstalleerd aan een geleideconstructie of in de onmiddellijke omgeving ervan,met als doel de ernst van een botsing van een motorrijder met de geleideconstructie te reduceren."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.lengte = KwantWrdInMeter()
        """De lengte van de motorvangplank in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.lengte"
        self.lengte.definition = "De lengte van de motorvangplank in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.schokindexMvp = KeuzelijstField(naam="schokindexMvp",
                                             label="schokindex motorvangplank",
                                             lijst=KlLEACSchokindexMVP(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.schokindexMvp",
                                             definition="Head injury criterium (HIC) van een motorvangplank.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Head injury criterium (HIC) van een motorvangplank."""

        self.snelheidsklasse = KeuzelijstField(naam="snelheidsklasse",
                                               label="snelheidsklasse",
                                               lijst=KlLEACSnelheidsklasse(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.snelheidsklasse",
                                               definition="De snelheid waarmee de testen uitgevoerd worden en of deze plaatsvinden op een continu of discontinu (niet in gebruik bij AWV) systeem.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """De snelheid waarmee de testen uitgevoerd worden en of deze plaatsvinden op een continu of discontinu (niet in gebruik bij AWV) systeem."""

        self.werkingsbreedteMvpwd = KwantWrdInMeter()
        """De afstand tussen de voorkant van het onvervormd systeem tot de maximale dynamische laterale positie van elk onderdeel van het systeem."""
        self.werkingsbreedteMvpwd.naam = "werkingsbreedteMvpwd"
        self.werkingsbreedteMvpwd.label = "werkingsbreedte mvpwd"
        self.werkingsbreedteMvpwd.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank.werkingsbreedteMvpwd"
        self.werkingsbreedteMvpwd.definition = "De afstand tussen de voorkant van het onvervormd systeem tot de maximale dynamische laterale positie van elk onderdeel van het systeem."
        self.werkingsbreedteMvpwd.constraints = ""
        self.werkingsbreedteMvpwd.usagenote = ""
        self.werkingsbreedteMvpwd.deprecated_version = ""

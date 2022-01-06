from OTLModel.Classes.AndereLaag import AndereLaag
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDunneOverlagingType import KlDunneOverlagingType
from OTLModel.Datatypes.KlKleurSupp import KlKleurSupp
from OTLModel.Datatypes.KwantWrdInTon import KwantWrdInTon


# Generated with OTLClassCreator. To modify: extend, do not edit
class DunneOverlaging(AndereLaag):
    """Een dunne overlaging kan bestaan uit een SME overlaging of een antisliplaag."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.gewicht = KwantWrdInTon()
        """Het gewicht van de dunne overlaging in ton."""
        self.gewicht.naam = "gewicht"
        self.gewicht.label = "gewicht"
        self.gewicht.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging.gewicht"
        self.gewicht.definition = "Het gewicht van de dunne overlaging in ton."
        self.gewicht.constraints = ""
        self.gewicht.usagenote = ""
        self.gewicht.deprecated_version = ""

        self.kleur = KeuzelijstField(naam="kleur",
                                     label="kleur",
                                     lijst=KlKleurSupp(),
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging.kleur",
                                     definition="De kleur van de dunne overlaging.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """De kleur van de dunne overlaging."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlDunneOverlagingType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging.type",
                                    definition="Het type SME overlaging of antisliplaag.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type SME overlaging of antisliplaag."""

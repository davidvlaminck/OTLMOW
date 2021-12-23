from OTLModel.Classes.Communicatieapparatuur import Communicatieapparatuur
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAntenneFrequentierange import KlAntenneFrequentierange
from OTLModel.Datatypes.KlAntenneMerk import KlAntenneMerk
from OTLModel.Datatypes.KlAntenneModelnaam import KlAntenneModelnaam


# Generated with OTLClassCreator
class Antenne(Communicatieapparatuur):
    """Toestel verbonden met een zender of ontvanger ten behoeve van het opvangen of verspreiden van signalen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.frequentierange = KeuzelijstField(naam="frequentierange",
                                               label="frequentierange",
                                               lijst=KlAntenneFrequentierange(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.frequentierange",
                                               definition="Geeft de frequentierange aan waarbinnen de antenne gebruikt kan worden.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Geeft de frequentierange aan waarbinnen de antenne gebruikt kan worden."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlAntenneMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.merk",
                                    definition="Het merk van de antenne.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de antenne."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlAntenneModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.modelnaam",
                                         definition="De modelnaam/product range van een antenne.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van een antenne."""

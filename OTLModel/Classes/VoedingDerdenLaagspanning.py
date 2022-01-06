from OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEleAansluitvermogen import KlEleAansluitvermogen


# Generated with OTLClassCreator. To modify: extend, do not edit
class VoedingDerdenLaagspanning(Voedingspunt):
    """Aansluiting op het laagspanningsnet van een andere partij, niet rechtstreeks bij de distributienetbeheerder en niet afgetakt van de asset beheerder."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedingDerdenLaagspanning"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aansluitvermogen = KeuzelijstField(naam="aansluitvermogen",
                                                label="aansluitvermogen",
                                                lijst=KlEleAansluitvermogen(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedingDerdenLaagspanning.aansluitvermogen",
                                                definition="Vermogen van de aansluiting.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Vermogen van de aansluiting."""

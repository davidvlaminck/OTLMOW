from abc import abstractmethod
from OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcHoutigeAanleg import DtcHoutigeAanleg
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoutigeVegetatie(BegroeidVoorkomen):
    """Houtige planten of houtige gewassen (planta lignosa) zijn overblijvende planten die worden gekenmerkt door secundaire diktegroei, waardoor de takken, stammen en wortels veel hout bevatten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        aanlegField = DtcHoutigeAanleg()
        aanlegField.naam = "aanleg"
        aanlegField.label = "aanleg"
        aanlegField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.aanleg"
        aanlegField.definition = "De manier van aanplanten van de houtige vegetatie."
        aanlegField.constraints = ""
        aanlegField.usagenote = ""
        aanlegField.deprecated_version = ""
        self.aanleg = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=aanlegField)
        """De manier van aanplanten van de houtige vegetatie."""

        self.hoogte = KwantWrdInMeter()
        """De hoogte in meter gemeten van de stamvoet tot de top of bovenste snoeivlak van de houtige vegetatie. """
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.hoogte"
        self.hoogte.definition = "De hoogte in meter gemeten van de stamvoet tot de top of bovenste snoeivlak van de houtige vegetatie. "
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.isVrijUitgroeiend = BooleanField(naam="isVrijUitgroeiend",
                                              label="is vrij uitgroeiend",
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.isVrijUitgroeiend",
                                              definition="Geeft aan of de vegetatie of begroeiing al dan niet snoei vereist.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Geeft aan of de vegetatie of begroeiing al dan niet snoei vereist."""

        self.knipoppervlak = KwantWrdInVierkanteMeter()
        """De afmeting van de begroeiing in vierkante meter dat geschoren moet worden."""
        self.knipoppervlak.naam = "knipoppervlak"
        self.knipoppervlak.label = "knipoppervlak"
        self.knipoppervlak.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HoutigeVegetatie.knipoppervlak"
        self.knipoppervlak.definition = "De afmeting van de begroeiing in vierkante meter dat geschoren moet worden."
        self.knipoppervlak.constraints = ""
        self.knipoppervlak.usagenote = ""
        self.knipoppervlak.deprecated_version = ""

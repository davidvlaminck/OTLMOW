from OTLModel.Classes.AndereLaag import AndereLaag
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHechtspecie import KlHechtspecie
from OTLModel.Datatypes.KlStortsteenKaliber import KlStortsteenKaliber
from OTLModel.Datatypes.KlStortsteenPlaatsingswijze import KlStortsteenPlaatsingswijze
from OTLModel.Datatypes.KlStortsteenType import KlStortsteenType
from OTLModel.Datatypes.KwantWrdInTon import KwantWrdInTon


# Generated with OTLClassCreator
class Stortsteen(AndereLaag):
    """Natuursteen van onregelmatige vorm,meestal gebruikt voor verstevigings- en beschermingsdoeleinden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.gewicht = KwantWrdInTon()
        """De hoeveelheid stortsteen in ton."""
        self.gewicht.naam = "gewicht"
        self.gewicht.label = "gewicht"
        self.gewicht.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.gewicht"
        self.gewicht.definition = "De hoeveelheid stortsteen in ton."
        self.gewicht.constraints = ""
        self.gewicht.usagenote = ""
        self.gewicht.deprecated_version = ""

        hechtspecieField = KeuzelijstField(naam="hechtspecie",
                                           label="hechtspecie",
                                           lijst=KlHechtspecie(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.hechtspecie",
                                           definition="Het gebruikte hechtingsmateriaal tussen gestapelde stenen.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.hechtspecie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=hechtspecieField)
        """Het gebruikte hechtingsmateriaal tussen gestapelde stenen."""

        self.isVerankerd = BooleanField(naam="isVerankerd",
                                        label="is verankerd",
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.isVerankerd",
                                        definition="Aanduiding of de gestapelde ruwe steen verankerd is.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Aanduiding of de gestapelde ruwe steen verankerd is."""

        self.kaliber = KeuzelijstField(naam="kaliber",
                                       label="kaliber",
                                       lijst=KlStortsteenKaliber(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.kaliber",
                                       definition="De gemiddelde diameter van de stortsteen.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """De gemiddelde diameter van de stortsteen."""

        self.plaatsingswijze = KeuzelijstField(naam="plaatsingswijze",
                                               label="bestortingswijze",
                                               lijst=KlStortsteenPlaatsingswijze(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.plaatsingswijze",
                                               definition="De manier waarop de stenen worden geplaatst.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """De manier waarop de stenen worden geplaatst."""

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.technischeFiche"
        technischeFicheField.definition = "De technische fiche van stortsteen als bijlage."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = ""
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """De technische fiche van stortsteen als bijlage."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlStortsteenType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.type",
                                    definition="Het type stortsteen.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type stortsteen."""

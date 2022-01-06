from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVerderOnderzoekTrekproef(Proef):
    """Een trekproef is een manier om nader te onderzoeken hoe het met de veiligheid van een (aangetaste of beschadigde) boom gesteld is. Door met een lier effectief aan een boom te trekken wordt de belasting bij storm in een model gegoten en getest."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerderOnderzoekTrekproef"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        verderOnderzoekTrekproefField = DtcDocument()
        verderOnderzoekTrekproefField.naam = "verderOnderzoekTrekproef"
        verderOnderzoekTrekproefField.label = "verder onderzoek trekproef"
        verderOnderzoekTrekproefField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerderOnderzoekTrekproef.verderOnderzoekTrekproef"
        verderOnderzoekTrekproefField.definition = "Een trekproef is een niet-destructieve methode om de stabiliteit (gevoeligheid voor windworp) vanbomen te testen door een kunstmatige belasting op de stam te relateren met het kantelen van destamvoet."
        verderOnderzoekTrekproefField.constraints = ""
        verderOnderzoekTrekproefField.usagenote = ""
        verderOnderzoekTrekproefField.deprecated_version = ""
        self.verderOnderzoekTrekproef = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=verderOnderzoekTrekproefField)
        """Een trekproef is een niet-destructieve methode om de stabiliteit (gevoeligheid voor windworp) vanbomen te testen door een kunstmatige belasting op de stam te relateren met het kantelen van destamvoet."""

# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVerderOnderzoekTrekproef(Proef):
    """Een trekproef is een manier om nader te onderzoeken hoe het met de veiligheid van een (aangetaste of beschadigde) boom gesteld is. Door met een lier effectief aan een boom te trekken wordt de belasting bij storm in een model gegoten en getest."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerderOnderzoekTrekproef'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._verderOnderzoekTrekproef = OTLAttribuut(field=DtcDocument,
                                                      naam='verderOnderzoekTrekproef',
                                                      label='verder onderzoek trekproef',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerderOnderzoekTrekproef.verderOnderzoekTrekproef',
                                                      kardinaliteit_max='*',
                                                      definition='Een trekproef is een niet-destructieve methode om de stabiliteit (gevoeligheid voor windworp) van bomen te testen door een kunstmatige belasting op de stam te relateren met het kantelen van de stamvoet.')

    @property
    def verderOnderzoekTrekproef(self):
        """Een trekproef is een niet-destructieve methode om de stabiliteit (gevoeligheid voor windworp) van bomen te testen door een kunstmatige belasting op de stam te relateren met het kantelen van de stamvoet."""
        return self._verderOnderzoekTrekproef.waarde

    @verderOnderzoekTrekproef.setter
    def verderOnderzoekTrekproef(self, value):
        self._verderOnderzoekTrekproef.set_waarde(value, owner=self)

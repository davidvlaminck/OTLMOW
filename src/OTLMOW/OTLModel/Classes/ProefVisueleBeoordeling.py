# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefVisueleBeoordeling(Proef):
    """Opsporen van de gebreken bij de definitieve oplevering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVisueleBeoordeling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._visueleBeoordeling = OTLAttribuut(field=DtcDocument,
                                                naam='visueleBeoordeling',
                                                label='visuele beoordeling',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVisueleBeoordeling.visueleBeoordeling',
                                                definition='Een rapport van de visuele beoordeling van de laag.')

    @property
    def visueleBeoordeling(self):
        """Een rapport van de visuele beoordeling van de laag."""
        return self._visueleBeoordeling.waarde

    @visueleBeoordeling.setter
    def visueleBeoordeling(self, value):
        self._visueleBeoordeling.set_waarde(value, owner=self)

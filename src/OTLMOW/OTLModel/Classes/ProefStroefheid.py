# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefStroefheid(Proef):
    """Het vermogen van een wegdek om door voertuigbanden tangentieel uitgeoefende krachten (bij het nemen van bochten, afremmen of optrekken) te compenseren door even grote wrijvingskrachten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStroefheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._stroefheid = OTLAttribuut(field=DtcDocument,
                                        naam='stroefheid',
                                        label='stroefheid',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStroefheid.stroefheid',
                                        definition='Proefresultaten van de stroefheid.')

    @property
    def stroefheid(self):
        """Proefresultaten van de stroefheid."""
        return self._stroefheid.waarde

    @stroefheid.setter
    def stroefheid(self, value):
        self._stroefheid.set_waarde(value, owner=self)

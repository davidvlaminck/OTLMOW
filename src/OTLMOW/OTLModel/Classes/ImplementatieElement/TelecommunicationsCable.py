# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Kabel import Kabel
from OTLMOW.OTLModel.Datatypes.KlTelecomCableMateriaalType import KlTelecomCableMateriaalType
from OTLMOW.OTLModel.Datatypes.KlTelecommunicationsSubthema import KlTelecommunicationsSubthema


# Generated with OTLClassCreator. To modify: extend, do not edit
class TelecommunicationsCable(Kabel):
    """Een aansluiting of reeks aansluitingen van een nutsvoorzieningennet voor het overbrengen van data van de ene locatie naar een andere."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TelecommunicationsCable'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._materiaalType = OTLAttribuut(field=KlTelecomCableMateriaalType,
                                           naam='materiaalType',
                                           label='materiaal type',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TelecommunicationsCable.materiaalType',
                                           definition='De indeling van het type volgens soort en materiaal van de kabel conform de indeling in IMKL.',
                                           owner=self)

        self._subthema = OTLAttribuut(field=KlTelecommunicationsSubthema,
                                      naam='subthema',
                                      label='subthema',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#TelecommunicationsCable.subthema',
                                      definition='Classificatie van een kabel, leiding, of leidingelementen volgens het thematisch domein waar deze toe behoren.',
                                      owner=self)

    @property
    def materiaalType(self):
        """De indeling van het type volgens soort en materiaal van de kabel conform de indeling in IMKL."""
        return self._materiaalType.get_waarde()

    @materiaalType.setter
    def materiaalType(self, value):
        self._materiaalType.set_waarde(value, owner=self)

    @property
    def subthema(self):
        """Classificatie van een kabel, leiding, of leidingelementen volgens het thematisch domein waar deze toe behoren."""
        return self._subthema.get_waarde()

    @subthema.setter
    def subthema(self, value):
        self._subthema.set_waarde(value, owner=self)

# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlSoortConstructiezeeg import KlSoortConstructiezeeg
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brugligger(AIMObject):
    """Abstracte om brugliggers te bundelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brugligger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._detailplanlBrugligger = OTLAttribuut(field=DtcDocument,
                                                   naam='detailplanlBrugligger',
                                                   label='detailplan brugligger',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brugligger.detailplanlBrugligger',
                                                   definition='Het detailplan van de brugligger.',
                                                   owner=self)

        self._grootteConstructiezeeg = OTLAttribuut(field=KwantWrdInCentimeter,
                                                    naam='grootteConstructiezeeg',
                                                    label='grootte constructiezeeg',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brugligger.grootteConstructiezeeg',
                                                    definition='De grootte van de doorbuiging van de brugligger. Deze wordt bepaald in het midden.',
                                                    owner=self)

        self._soortConstructiezeeg = OTLAttribuut(field=KlSoortConstructiezeeg,
                                                  naam='soortConstructiezeeg',
                                                  label='soort cunstructiezeeg',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brugligger.soortConstructiezeeg',
                                                  definition='Geeft het type van doorbuiging van de brugligger aan.',
                                                  owner=self)

    @property
    def detailplanlBrugligger(self):
        """Het detailplan van de brugligger."""
        return self._detailplanlBrugligger.get_waarde()

    @detailplanlBrugligger.setter
    def detailplanlBrugligger(self, value):
        self._detailplanlBrugligger.set_waarde(value, owner=self)

    @property
    def grootteConstructiezeeg(self):
        """De grootte van de doorbuiging van de brugligger. Deze wordt bepaald in het midden."""
        return self._grootteConstructiezeeg.get_waarde()

    @grootteConstructiezeeg.setter
    def grootteConstructiezeeg(self, value):
        self._grootteConstructiezeeg.set_waarde(value, owner=self)

    @property
    def soortConstructiezeeg(self):
        """Geeft het type van doorbuiging van de brugligger aan."""
        return self._soortConstructiezeeg.get_waarde()

    @soortConstructiezeeg.setter
    def soortConstructiezeeg(self, value):
        self._soortConstructiezeeg.set_waarde(value, owner=self)

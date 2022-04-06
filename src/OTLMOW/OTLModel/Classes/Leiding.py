# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.KabelgeleidingEnLeidingBevestiging import KabelgeleidingEnLeidingBevestiging
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Leiding(KabelgeleidingEnLeidingBevestiging, AIMNaamObject):
    """Abstracte om de gemeenschappelijke eigenschappen en relaties van de verschillende soorten leidingen onder één noemer te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        KabelgeleidingEnLeidingBevestiging.__init__(self)

        self._buitendiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='buitendiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding.buitendiameter',
                                            definition='De buitendiameter van de leiding in millimeter. Indien de leiding geen cirkelvormige doorsnede heeft, dan gaat het hier om de diameter van de omgeschreven cirkel.',
                                            owner=self)

        self._isRisicovol = OTLAttribuut(field=BooleanField,
                                         naam='isRisicovol',
                                         label='is risicovol',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding.isRisicovol',
                                         definition='Geeft aan of werken aan of rond de leiding een verhoogd risico met zich meebrengen omwille van de aard van de betrokken leiding.',
                                         owner=self)

    @property
    def buitendiameter(self):
        """De buitendiameter van de leiding in millimeter. Indien de leiding geen cirkelvormige doorsnede heeft, dan gaat het hier om de diameter van de omgeschreven cirkel."""
        return self._buitendiameter.waarde

    @buitendiameter.setter
    def buitendiameter(self, value):
        self._buitendiameter.set_waarde(value, owner=self)

    @property
    def isRisicovol(self):
        """Geeft aan of werken aan of rond de leiding een verhoogd risico met zich meebrengen omwille van de aard van de betrokken leiding."""
        return self._isRisicovol.waarde

    @isRisicovol.setter
    def isRisicovol(self, value):
        self._isRisicovol.set_waarde(value, owner=self)

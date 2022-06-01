# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcConstructiestaalspecificaties import DtcConstructiestaalspecificaties
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMillimeter import KwantWrdInVierkanteMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grondanker(AIMObject):
    """Abstracte voor de verschillende grondankers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._heeftBeschermingskap = OTLAttribuut(field=BooleanField,
                                                  naam='heeftBeschermingskap',
                                                  label='heeft beschermingskap',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker.heeftBeschermingskap',
                                                  definition='Geeft aan of het grondanker een beschermingskap heeft.',
                                                  owner=self)

        self._staalsectie = OTLAttribuut(field=KwantWrdInVierkanteMillimeter,
                                         naam='staalsectie',
                                         label='staalsectie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker.staalsectie',
                                         definition='Totale oppervlakte van staalsectie, uitgedrukte in vierkant milimeter.',
                                         owner=self)

        self._staalspecificaties = OTLAttribuut(field=DtcConstructiestaalspecificaties,
                                                naam='staalspecificaties',
                                                label='staalspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker.staalspecificaties',
                                                definition='Type constructiestaal dat wordt gebruikt.',
                                                owner=self)

    @property
    def heeftBeschermingskap(self):
        """Geeft aan of het grondanker een beschermingskap heeft."""
        return self._heeftBeschermingskap.get_waarde()

    @heeftBeschermingskap.setter
    def heeftBeschermingskap(self, value):
        self._heeftBeschermingskap.set_waarde(value, owner=self)

    @property
    def staalsectie(self):
        """Totale oppervlakte van staalsectie, uitgedrukte in vierkant milimeter."""
        return self._staalsectie.get_waarde()

    @staalsectie.setter
    def staalsectie(self, value):
        self._staalsectie.set_waarde(value, owner=self)

    @property
    def staalspecificaties(self):
        """Type constructiestaal dat wordt gebruikt."""
        return self._staalspecificaties.get_waarde()

    @staalspecificaties.setter
    def staalspecificaties(self, value):
        self._staalspecificaties.set_waarde(value, owner=self)

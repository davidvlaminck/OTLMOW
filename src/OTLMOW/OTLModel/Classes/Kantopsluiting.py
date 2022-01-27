# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from src.OTLMOW.OTLModel.Classes.LijnvormigElement import LijnvormigElement
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.KlLEKantopsluitingKleur import KlLEKantopsluitingKleur
from src.OTLMOW.OTLModel.Datatypes.KlLEKantopsluitingSoort import KlLEKantopsluitingSoort
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kantopsluiting(LijnvormigElement):
    """Abstracte voor de gemeenschappelijke eigenschappen en relaties voor de kantopsluiting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._isGeprefabriceerd = OTLAttribuut(field=BooleanField,
                                               naam='isGeprefabriceerd',
                                               label='is geprefabriceerd',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.isGeprefabriceerd',
                                               definition='Aanduiding of de kantopsluiting al dan niet is geprefabriceerd.')

        self._kleur = OTLAttribuut(field=KlLEKantopsluitingKleur,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.kleur',
                                   definition='De kleur van kantopsluiting.')

        self._soort = OTLAttribuut(field=KlLEKantopsluitingSoort,
                                   naam='soort',
                                   label='soort',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.soort',
                                   definition='De soort van kantopsluiting.')

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.totaleLengte',
                                          definition='De totale lengte van de geplaatste constructie van kantopsluitingen in meter.')

    @property
    def isGeprefabriceerd(self):
        """Aanduiding of de kantopsluiting al dan niet is geprefabriceerd."""
        return self._isGeprefabriceerd.waarde

    @isGeprefabriceerd.setter
    def isGeprefabriceerd(self, value):
        self._isGeprefabriceerd.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """De kleur van kantopsluiting."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def soort(self):
        """De soort van kantopsluiting."""
        return self._soort.waarde

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)

    @property
    def totaleLengte(self):
        """De totale lengte van de geplaatste constructie van kantopsluitingen in meter."""
        return self._totaleLengte.waarde

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)

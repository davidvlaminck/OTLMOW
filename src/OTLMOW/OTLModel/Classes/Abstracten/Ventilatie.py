# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInKubiekeMeterPerSeconde import KwantWrdInKubiekeMeterPerSeconde
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ventilatie(AIMObject, PuntGeometrie):
    """Abstracte voor attributen die gemeenschappelijk zijn voor verschillende types van ventilatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._binnendiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='binnendiameter',
                                            label='binnendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie.binnendiameter',
                                            definition='De grootste afstand van de rechte lijn die kan worden getrokken tussen twee punten op de binnenzijde van de ventilatie. Deze rechte lijn gaat altijd door het middelpunt van de ventilatie.',
                                            owner=self)

        self._buitendiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='buitendiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie.buitendiameter',
                                            definition='De grootste afstand van de rechte lijn die kan worden getrokken tussen twee punten op de buitenzijde van de ventilatie. Deze rechte lijn gaat altijd door het middelpunt van de ventilatie.',
                                            owner=self)

        self._maximaalDebiet = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                            naam='maximaalDebiet',
                                            label='maximaal debiet',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie.maximaalDebiet',
                                            usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                            deprecated_version='2.0.0',
                                            definition='Maximaal debiet is de grootste hoeveelheid gas of vloeistof die per tijdseenheid door een bepaald oppervlak kan stromen.',
                                            owner=self)

        self._maximaalVolumedebiet = OTLAttribuut(field=KwantWrdInKubiekeMeterPerSeconde,
                                                  naam='maximaalVolumedebiet',
                                                  label='maximaal volumedebiet',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie.maximaalVolumedebiet',
                                                  definition='Maximaal volumedebiet is de grootste hoeveelheid volume aan gas of vloeistof die per tijdseenheid door een bepaald oppervlak kan stromen.',
                                                  owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie.vermogen',
                                      definition='Het vermogen van een ventilatie is de energie die dat het per seconde omzet.',
                                      owner=self)

    @property
    def binnendiameter(self):
        """De grootste afstand van de rechte lijn die kan worden getrokken tussen twee punten op de binnenzijde van de ventilatie. Deze rechte lijn gaat altijd door het middelpunt van de ventilatie."""
        return self._binnendiameter.get_waarde()

    @binnendiameter.setter
    def binnendiameter(self, value):
        self._binnendiameter.set_waarde(value, owner=self)

    @property
    def buitendiameter(self):
        """De grootste afstand van de rechte lijn die kan worden getrokken tussen twee punten op de buitenzijde van de ventilatie. Deze rechte lijn gaat altijd door het middelpunt van de ventilatie."""
        return self._buitendiameter.get_waarde()

    @buitendiameter.setter
    def buitendiameter(self, value):
        self._buitendiameter.set_waarde(value, owner=self)

    @property
    def maximaalDebiet(self):
        """Maximaal debiet is de grootste hoeveelheid gas of vloeistof die per tijdseenheid door een bepaald oppervlak kan stromen."""
        return self._maximaalDebiet.get_waarde()

    @maximaalDebiet.setter
    def maximaalDebiet(self, value):
        self._maximaalDebiet.set_waarde(value, owner=self)

    @property
    def maximaalVolumedebiet(self):
        """Maximaal volumedebiet is de grootste hoeveelheid volume aan gas of vloeistof die per tijdseenheid door een bepaald oppervlak kan stromen."""
        return self._maximaalVolumedebiet.get_waarde()

    @maximaalVolumedebiet.setter
    def maximaalVolumedebiet(self, value):
        self._maximaalVolumedebiet.set_waarde(value, owner=self)

    @property
    def vermogen(self):
        """Het vermogen van een ventilatie is de energie die dat het per seconde omzet."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)

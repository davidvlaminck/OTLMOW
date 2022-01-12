# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLModel.Datatypes.KwantWrdInKubiekeMeterPerSeconde import KwantWrdInKubiekeMeterPerSeconde
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ventilatie(AIMObject):
    """Abstracte voor attributen die gemeenschappelijk zijn voor verschillende types van ventilatie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.binnendiameter = KwantWrdInMillimeter()
        """De grootste afstand van de rechte lijn die kan worden getrokken tussen twee punten op de binnenzijde van de ventilatie. Deze rechte lijn gaat altijd door het middelpunt van de ventilatie."""
        self.binnendiameter.naam = "binnendiameter"
        self.binnendiameter.label = "binnendiameter"
        self.binnendiameter.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie.binnendiameter"
        self.binnendiameter.definition = "De grootste afstand van de rechte lijn die kan worden getrokken tussen twee punten op de binnenzijde van de ventilatie. Deze rechte lijn gaat altijd door het middelpunt van de ventilatie."
        self.binnendiameter.constraints = ""
        self.binnendiameter.usagenote = ""
        self.binnendiameter.deprecated_version = ""

        self.buitendiameter = KwantWrdInMillimeter()
        """De grootste afstand van de rechte lijn die kan worden getrokken tussen twee punten op de buitenzijde van de ventilatie. Deze rechte lijn gaat altijd door het middelpunt van de ventilatie."""
        self.buitendiameter.naam = "buitendiameter"
        self.buitendiameter.label = "buitendiameter"
        self.buitendiameter.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie.buitendiameter"
        self.buitendiameter.definition = "De grootste afstand van de rechte lijn die kan worden getrokken tussen twee punten op de buitenzijde van de ventilatie. Deze rechte lijn gaat altijd door het middelpunt van de ventilatie."
        self.buitendiameter.constraints = ""
        self.buitendiameter.usagenote = ""
        self.buitendiameter.deprecated_version = ""

        self.maximaalVolumedebiet = KwantWrdInKubiekeMeterPerSeconde()
        """Maximaal volumedebiet is de grootste hoeveelheid volume aan gas of vloeistof die per tijdseenheid door een bepaald oppervlak kan stromen."""
        self.maximaalVolumedebiet.naam = "maximaalVolumedebiet"
        self.maximaalVolumedebiet.label = "maximaal volumedebiet"
        self.maximaalVolumedebiet.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie.maximaalVolumedebiet"
        self.maximaalVolumedebiet.definition = "Maximaal volumedebiet is de grootste hoeveelheid volume aan gas of vloeistof die per tijdseenheid door een bepaald oppervlak kan stromen."
        self.maximaalVolumedebiet.constraints = ""
        self.maximaalVolumedebiet.usagenote = ""
        self.maximaalVolumedebiet.deprecated_version = ""

        self.vermogen = KwantWrdInWatt()
        """Het vermogen van een ventilatie is de energie die dat het per seconde omzet."""
        self.vermogen.naam = "vermogen"
        self.vermogen.label = "vermogen"
        self.vermogen.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie.vermogen"
        self.vermogen.definition = "Het vermogen van een ventilatie is de energie die dat het per seconde omzet."
        self.vermogen.constraints = ""
        self.vermogen.usagenote = ""
        self.vermogen.deprecated_version = ""

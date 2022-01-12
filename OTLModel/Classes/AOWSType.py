# coding=utf-8
from abc import abstractmethod, ABC
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AOWSType(ABC):
    """Abstracte om alle eigenschappen en relaties van AOWS type onder 1 noemer te houden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.isGoedgekeurd = BooleanField(naam="isGoedgekeurd",
                                          label="is goedgekeurd",
                                          objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType.isGoedgekeurd",
                                          definition="Bepaling van de goedkeuring van AOWS.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Bepaling van de goedkeuring van AOWS."""

        self.versieGoedgekeurd = StringField(naam="versieGoedgekeurd",
                                             label="versie goedgekeurd",
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType.versieGoedgekeurd",
                                             definition="De versie van het standaardbestek 250 waar de goedkeuring is bepaald.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """De versie van het standaardbestek 250 waar de goedkeuring is bepaald."""

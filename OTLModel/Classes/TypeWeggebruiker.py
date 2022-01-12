# coding=utf-8
from abc import abstractmethod, ABC
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVriTypeweggebruiker import KlVriTypeweggebruiker


# Generated with OTLClassCreator. To modify: extend, do not edit
class TypeWeggebruiker(ABC):
    """Abstracte klasse die het type weggebruiker met een attribuut (volgens keuzelijst) aangeeft."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TypeWeggebruiker"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.typeWeggebruiker = KeuzelijstField(naam="typeWeggebruiker",
                                                label="type weggebruiker",
                                                lijst=KlVriTypeweggebruiker(),
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TypeWeggebruiker.typeWeggebruiker",
                                                definition="het type weggebruiker.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """het type weggebruiker."""

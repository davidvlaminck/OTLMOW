# coding=utf-8
from abc import abstractmethod, ABC
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACSchokindex import KlLEACSchokindex


# Generated with OTLClassCreator. To modify: extend, do not edit
class SchokindexVoertuigkering(ABC):
    """Abstracte waarin de resultaten van de proef voor de bepaling van de schokindex parameter worden bijgehouden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SchokindexVoertuigkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.schokindex = KeuzelijstField(naam="schokindex",
                                          label="schokindex",
                                          lijst=KlLEACSchokindex(),
                                          objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SchokindexVoertuigkering.schokindex",
                                          definition="De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding."""

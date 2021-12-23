from abc import abstractmethod, ABC
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator
class BijlageVoertuigkering(ABC):
    """Abstracte om bestanden te bundelen omtrent voertuigkering."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BijlageVoertuigkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        testrapportVoertuigkeringField = DtcDocument()
        testrapportVoertuigkeringField.naam = "testrapportVoertuigkering"
        testrapportVoertuigkeringField.label = "testrapport voertuigkering"
        testrapportVoertuigkeringField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BijlageVoertuigkering.testrapportVoertuigkering"
        testrapportVoertuigkeringField.definition = "De testresultaten van de crashtesten die op de voertuigkerende constructie uitgevoerd zijn."
        testrapportVoertuigkeringField.constraints = ""
        testrapportVoertuigkeringField.usagenote = ""
        testrapportVoertuigkeringField.deprecated_version = ""
        self.testrapportVoertuigkering = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=testrapportVoertuigkeringField)
        """De testresultaten van de crashtesten die op de voertuigkerende constructie uitgevoerd zijn."""

        videoVoertuigkeringField = DtcDocument()
        videoVoertuigkeringField.naam = "videoVoertuigkering"
        videoVoertuigkeringField.label = "video voertuigkering"
        videoVoertuigkeringField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BijlageVoertuigkering.videoVoertuigkering"
        videoVoertuigkeringField.definition = "Video-opname van de crashtesten op de voertuigkerende constructie."
        videoVoertuigkeringField.constraints = ""
        videoVoertuigkeringField.usagenote = ""
        videoVoertuigkeringField.deprecated_version = ""
        self.videoVoertuigkering = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=videoVoertuigkeringField)
        """Video-opname van de crashtesten op de voertuigkerende constructie."""

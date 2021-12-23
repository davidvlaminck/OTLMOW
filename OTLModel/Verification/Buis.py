from abc import abstractmethod
from OTLModel.Verification.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField

class Buis(AIMObject):  # ABC or the class it inherits from
    """Abstracte om de gemeenschappelijke eigenschappen en relaties van de verschillende soorten buizen onder één noemer te houden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.aantalTelwerken = BooleanField(naam="isManToegankelijk",
                                            label="is man toegankelijk",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.isManToegankelijk",
                                            definition="Bepaalt of de buis toegankelijk is voor een persoon.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bepaalt of de buis toegankelijk is voor een persoon."""

    # TODO aanvullen andere attributen

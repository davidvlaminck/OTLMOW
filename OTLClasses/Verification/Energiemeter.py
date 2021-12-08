from abc import abstractmethod, ABC

from ModelGenerator.BaseClasses.IntField import IntField
from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField
from ModelGenerator.BaseClasses.StringField import StringField
from OTLClasses.Verification.AIMObject import AIMObject
from OTLClasses.Verification.KlEnergiemeterMetertype import KlEnergiemeterMetertype


class Energiemeter(AIMObject, ABC):
    """Abstracte voor alle energiemeters."""

    typeUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Energiemeter"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.aantalTelwerken = IntField(naam="aantalTelwerken", label="aantal telwerken",
                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter.aantalTelwerken",
                            definition="Het aantal telwerken dat de energiemeter bevat: 1 bij enkelvoudige meter, 2 bij een dag- en nacht-meter."
                            , constraints="", usagenote="", deprecated_version="")
        """Het aantal telwerken dat de energiemeter bevat: 1 bij enkelvoudige meter, 2 bij een dag- en nacht-meter."""

        self.meternummer = StringField(naam="meternummer", label="meternummer",
                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter.meternummer",
                                definition="Het serienummer (nummer van het fabrikaat) op de meter."
                                , constraints="", usagenote="", deprecated_version="")
        """Het serienummer (nummer van het fabrikaat) op de meter."""

        self.metertype = KlEnergiemeterMetertype()
        """Type meter (mechanisch, elektronisch)."""

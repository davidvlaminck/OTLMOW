# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEnergiemeterMetertype import KlEnergiemeterMetertype
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Energiemeter(AIMNaamObject):
    """Abstracte voor alle energiemeters."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.aantalTelwerken = IntegerField(naam="aantalTelwerken",
                                            label="aantal telwerken",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter.aantalTelwerken",
                                            definition="Het aantal telwerken dat de energiemeter bevat: 1 bij enkelvoudige meter, 2 bij een dag- en nacht-meter.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Het aantal telwerken dat de energiemeter bevat: 1 bij enkelvoudige meter, 2 bij een dag- en nacht-meter."""

        self.meternummer = StringField(naam="meternummer",
                                       label="meternummer",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter.meternummer",
                                       definition="Het serienummer (nummer van het fabrikaat) op de meter.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Het serienummer (nummer van het fabrikaat) op de meter."""

        self.metertype = KeuzelijstField(naam="metertype",
                                         label="metertype",
                                         lijst=KlEnergiemeterMetertype(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter.metertype",
                                         definition="Type meter (mechanisch, elektronisch).",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Type meter (mechanisch, elektronisch)."""

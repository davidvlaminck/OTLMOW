import abc
from abc import abstractmethod

from ModelGenerator.BaseClasses.IntField import IntField
from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField
from ModelGenerator.BaseClasses.StringField import StringField
from OTLClasses.Verification.AIMObject import AIMObject
from OTLClasses.Verification.KlEnergiemeterMetertype import KlEnergiemeterMetertype


class Energiemeter(AIMObject):
    """Abstracte voor alle energiemeters."""
    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Energiemeter"

    antalTelwerken = IntField()
    """Het aantal telwerken dat de energiemeter bevat: 1 bij enkelvoudige meter, 2 bij een dag- en nacht-meter."""
    meternummer = StringField()
    """Het serienummer (nummer van het fabrikaat) op de meter."""
    metertype = KeuzelijstField(KlEnergiemeterMetertype())
    """Type meter (mechanisch, elektronisch)."""

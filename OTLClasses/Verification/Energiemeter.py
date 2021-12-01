from ModelGenerator.BaseClasses.IntField import IntField
from ModelGenerator.BaseClasses.KeuzelijstField import KeuzelijstField
from ModelGenerator.BaseClasses.StringField import StringField
from OTLClasses.Verification.AIMObject import AIMObject
from OTLClasses.Verification.KlEnergiemeterMetertype import KlEnergiemeterMetertype


class Energiemeter(AIMObject):
    """Abstracte voor alle energiemeters."""
    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Energiemeter"
    aantalTelwerken = IntField()
    """Het aantal telwerken dat de energiemeter bevat: 1 bij enkelvoudige meter, 2 bij een dag- en nacht-meter."""
    meternummer = StringField()
    """Het serienummer (nummer van het fabrikaat) op de meter."""
    metertype = KeuzelijstField(KlEnergiemeterMetertype())
    """Type meter (mechanisch, elektronisch)."""
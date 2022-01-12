# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Put import Put
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPutMateriaal import KlPutMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class BlindePut(AIMObject, Put):
    """Een put waar de riolering op aangesloten is maar die niet meer zichtbaar is."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BlindePut"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Put.__init__(self)

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlPutMateriaal(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BlindePut.materiaal",
                                         definition="Het materiaal waaruit de blinde put is vervaardigd.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal waaruit de blinde put is vervaardigd."""

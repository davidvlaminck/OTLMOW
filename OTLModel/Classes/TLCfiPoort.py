# coding=utf-8
from OTLModel.Classes.IVRIComponent import IVRIComponent
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlIVRIMerkTLCfi import KlIVRIMerkTLCfi
from OTLModel.Datatypes.KlIVRIModelTLCfi import KlIVRIModelTLCfi


# Generated with OTLClassCreator. To modify: extend, do not edit
class TLCfiPoort(IVRIComponent):
    """Functionele software component die een TLC-FI interface aanbiedt waardoor data kan uitgewisseld worden voor intelligente verkeersregelaars."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlIVRIMerkTLCfi(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort.merk",
                                    definition="De merknaam van de TLC-fi poort; duidt op de leverancier of producent van de iVRI component.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De merknaam van de TLC-fi poort; duidt op de leverancier of producent van de iVRI component."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlIVRIModelTLCfi(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort.modelnaam",
                                         definition="De modelnaam/product range van de TLC-fi poort.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van de TLC-fi poort."""

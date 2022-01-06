# coding=utf-8
from OTLModel.Classes.IVRIComponent import IVRIComponent
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlIVRIMerkRIS import KlIVRIMerkRIS
from OTLModel.Datatypes.KlIVRIModelRIS import KlIVRIModelRIS


# Generated with OTLClassCreator. To modify: extend, do not edit
class RIS(IVRIComponent):
    """Afkorting van Roadside ITS Station. Functionele software component die een RIS aanbiedt voor de werking van intelligente verkeersregelaars."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlIVRIMerkRIS(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS.merk",
                                    definition="De merknaam van de RIS; duidt op de leverancier of producent van de iVRI component.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De merknaam van de RIS; duidt op de leverancier of producent van de iVRI component."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlIVRIModelRIS(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS.modelnaam",
                                         definition="De modelnaam/product range van de RIS.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van de RIS."""

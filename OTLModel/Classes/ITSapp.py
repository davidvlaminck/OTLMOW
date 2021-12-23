from OTLModel.Classes.IVRIComponent import IVRIComponent
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlIVRIMerkITSapp import KlIVRIMerkITSapp
from OTLModel.Datatypes.KlIVRIModelITSapp import KlIVRIModelITSapp


# Generated with OTLClassCreator
class ITSapp(IVRIComponent):
    """Functionele software component die de intelligente regel applicaties aanbiedt aan de intelligente verkeersregelaars."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ITSapp"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlIVRIMerkITSapp(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ITSapp.merk",
                                    definition="De merknaam van de ITSapp; duidt op de leverancier of producent van de iVRI component.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De merknaam van de ITSapp; duidt op de leverancier of producent van de iVRI component."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlIVRIModelITSapp(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ITSapp.modelnaam",
                                         definition="De modelnaam/product range van de ITSapp.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van de ITSapp."""

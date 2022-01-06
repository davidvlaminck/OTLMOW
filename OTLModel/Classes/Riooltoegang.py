from OTLModel.Classes.Put import Put
from OTLModel.Classes.PutRelatie import PutRelatie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlUitlaatType import KlUitlaatType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riooltoegang(Put, PutRelatie):
    """Het uiteinde van een rioolbuis."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)

        self.typeRiooltoegang = KeuzelijstField(naam="typeRiooltoegang",
                                                label="type riooltoegang",
                                                lijst=KlUitlaatType(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang.typeRiooltoegang",
                                                definition="Bepaalt het type van een riooltoegang.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Bepaalt het type van een riooltoegang."""

from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DecimalFloatField import DecimalFloatField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuminantie(Proef):
    """Bij gebrek aan Qd-meting kan de luminantiefactor ß van wegmarkeringen gebruikt worden om het contrast met het wegdek en bijgevolg de dagzichtbaarheid te bepalen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuminantie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.luminantiefactor = DecimalFloatField(naam="luminantiefactor",
                                                  label="luminantiefactor",
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuminantie.luminantiefactor",
                                                  definition="Waarde om het contrast met het wegdek en bijgevolg de dagzichtbaarheid te bepalen.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """Waarde om het contrast met het wegdek en bijgevolg de dagzichtbaarheid te bepalen."""

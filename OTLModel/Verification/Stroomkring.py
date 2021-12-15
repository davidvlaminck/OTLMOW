from OTLModel.Datatypes.StringField import StringField
from OTLModel.Verification.AIMNaamObject import AIMNaamObject


class Stroomkring(AIMNaamObject):
    """Ook wel vertrek of vertrekkende kabel genoemd. Afgezekerde elektrische geleiders waarmee de applicaties voorzien worden
    van de nodige voeding. """
    def __init__(self):
        super().__init__()
        self.stroomkringnummer = StringField(naam="stroomkringnummer", label="stroomkringnummer",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring.stroomkringnummer",
                                       definition="De identificatie van de stroomkring.", constraints="", usagenote="", deprecated_version="")
        """De identificatie van de stroomkring."""

    typeUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

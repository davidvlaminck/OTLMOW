# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stroomkring(AIMNaamObject):
    """Ook wel vertrek of vertrekkende kabel genoemd. Afgezekerde elektrische geleiders waarmee de applicaties voorzien worden van de nodige voeding."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.stroomkringnummer = StringField(naam="stroomkringnummer",
                                             label="stroomkringnummer",
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring.stroomkringnummer",
                                             definition="De identificatie van de stroomkring.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """De identificatie van de stroomkring."""

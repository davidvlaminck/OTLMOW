from ModelGenerator.BaseClasses.StringField import StringField
from OTLClasses.Verification.AIMNaamObject import AIMNaamObject


class Stroomkring(AIMNaamObject):
    """Ook wel vertrek of vertrekkende kabel genoemd. Afgezekerde elektrische geleiders waarmee de applicaties voorzien worden
    van de nodige voeding. """
    def __init__(self):
        pass

    stroomkringnummer = StringField()
    """De identificatie van de stroomkring."""

    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring"

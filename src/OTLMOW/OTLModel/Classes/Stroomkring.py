# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stroomkring(AIMNaamObject):
    """Ook wel vertrek of vertrekkende kabel genoemd. Afgezekerde elektrische geleiders waarmee de applicaties voorzien worden van de nodige voeding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._stroomkringnummer = OTLAttribuut(field=StringField,
                                               naam='stroomkringnummer',
                                               label='stroomkringnummer',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring.stroomkringnummer',
                                               definition='De identificatie van de stroomkring.')

    @property
    def stroomkringnummer(self):
        """De identificatie van de stroomkring."""
        return self._stroomkringnummer.waarde

    @stroomkringnummer.setter
    def stroomkringnummer(self, value):
        self._stroomkringnummer.set_waarde(value, owner=self)

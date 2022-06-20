# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stroomkring(AIMNaamObject, PuntGeometrie):
    """Ook wel vertrek of vertrekkende kabel genoemd. Afgezekerde elektrische geleiders waarmee de applicaties voorzien worden van de nodige voeding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._stroomkringnummer = OTLAttribuut(field=StringField,
                                               naam='stroomkringnummer',
                                               label='stroomkringnummer',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring.stroomkringnummer',
                                               definition='De identificatie van de stroomkring.',
                                               owner=self)

    @property
    def stroomkringnummer(self):
        """De identificatie van de stroomkring."""
        return self._stroomkringnummer.get_waarde()

    @stroomkringnummer.setter
    def stroomkringnummer(self, value):
        self._stroomkringnummer.set_waarde(value, owner=self)

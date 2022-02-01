# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class DtcToezichtGroepWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://tz.data.wegenenverkeer.be/ns/implementatieelement#DtcToezichtGroep.naam',
                                  definition='De naam van de toezichtgroep.')

        self._referentie = OTLAttribuut(field=StringField,
                                        naam='referentie',
                                        label='referentie',
                                        objectUri='https://tz.data.wegenenverkeer.be/ns/implementatieelement#DtcToezichtGroep.referentie',
                                        definition='De unieke referentie van de toezichtgroep.')

    @property
    def naam(self):
        """De naam van de toezichtgroep."""
        return self._naam.waarde

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self._parent)

    @property
    def referentie(self):
        """De unieke referentie van de toezichtgroep."""
        return self._referentie.waarde

    @referentie.setter
    def referentie(self, value):
        self._referentie.set_waarde(value, owner=self._parent)


class DtcToezichtGroep(ComplexField, AttributeInfo):
    """De toezichtgroep van een asset."""
    naam = 'DtcToezichtGroep'
    label = 'ToezichtGroep'
    objectUri = 'https://tz.data.wegenenverkeer.be/ns/dt#DtcToezichtGroep'
    definition = 'De toezichtgroep van een asset..'
    waardeObject = DtcToezichtGroepWaarden

    def __str__(self):
        return ComplexField.__str__(self)

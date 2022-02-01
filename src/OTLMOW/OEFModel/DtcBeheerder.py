# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class DtcBeheerderWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://tz.data.wegenenverkeer.be/ns/implementatieelement#DtcBeheerder.naam',
                                  definition='De naam van de schadebeheerder.')

        self._referentie = OTLAttribuut(field=StringField,
                                        naam='referentie',
                                        label='referentie',
                                        objectUri='https://tz.data.wegenenverkeer.be/ns/implementatieelement#DtcBeheerder.referentie',
                                        definition='De unieke referentie van de schadebeheerder.')

    @property
    def naam(self):
        """De naam van de schadebeheerder."""
        return self._naam.waarde

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self._parent)

    @property
    def referentie(self):
        """De unieke referentie van de schadebeheerder."""
        return self._referentie.waarde

    @referentie.setter
    def referentie(self, value):
        self._referentie.set_waarde(value, owner=self._parent)


class DtcBeheerder(ComplexField, AttributeInfo):
    """De schadebeheerder van een asset."""
    naam = 'schadebeheerder'
    label = 'schadebeheerder'
    objectUri = 'https://tz.data.wegenenverkeer.be/ns/implementatieelement#Schadebeheerder.schadebeheerder'
    definition = 'De schadebeheerder van een asset.'
    waardeObject = DtcBeheerderWaarden

    def __str__(self):
        return ComplexField.__str__(self)

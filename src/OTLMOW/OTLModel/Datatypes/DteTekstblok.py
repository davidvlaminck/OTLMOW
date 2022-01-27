# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteTekstblokWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._waarde = OTLAttribuut(field=StringField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok.waarde',
                                    definition='De string welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters.')

    @property
    def waarde(self):
        """De string welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class DteTekstblok(OTLField, AttributeInfo):
    """Een tekst welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters."""
    naam = 'DteTekstblok'
    label = 'Tekstblok'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok'
    definition = 'Een tekst welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters.'
    waardeObject = DteTekstblokWaarden

    def __str__(self):
        return OTLField.__str__(self)


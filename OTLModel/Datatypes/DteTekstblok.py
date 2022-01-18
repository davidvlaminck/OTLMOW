# coding=utf-8
from OTLModel.Datatypes.StringField import StringField


class DteTekstblok(StringField):
    """Een tekst welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters."""
    naam = 'DteTekstblok'
    label = 'Tekstblok'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTekstblok'
    definition = 'Een tekst welke uit meerdere zinnen bestaat, en ook regeleindes kan bevatten. Een tekstblok bevat maximaal 65.000 karakters.'
    usagenote = ''
    deprecated_version = ''

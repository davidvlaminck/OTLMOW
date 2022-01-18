# coding=utf-8
from OTLModel.Datatypes.StringField import StringField


class DteKleurRAL(StringField):
    """Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999."""
    naam = 'DteKleurRAL'
    label = 'RAL-kleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteKleurRAL'
    definition = 'Beschrijft een kleur volgens het RAL classificatiesysteem. De waarde is een natuurlijk getal tussen 1000 en 9999.'
    usagenote = ''
    deprecated_version = ''

    @staticmethod
    def validate(value, attribuut):
        return StringField.validate(value, attribuut)

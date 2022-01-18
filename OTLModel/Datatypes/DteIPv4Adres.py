# coding=utf-8
from OTLModel.Datatypes.StringField import StringField


class DteIPv4Adres(StringField):
    """Beschrijft een ip-adres volgens de ipv4 specificatie."""
    naam = 'DteIPv4Adres'
    label = 'IPv4-adres'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteIPv4Adres'
    definition = 'Beschrijft een ip-adres volgens de ipv4 specificatie.'
    usagenote = ''
    deprecated_version = ''

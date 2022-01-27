# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from src.OTLMOW.OTLModel.Datatypes.KlAlgGemeente import KlAlgGemeente
from src.OTLMOW.OTLModel.Datatypes.KlAlgProvincie import KlAlgProvincie
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAdresWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._bus = OTLAttribuut(field=StringField,
                                 naam='bus',
                                 label='bus',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.bus',
                                 definition='Een nummer dat de postbus aanduidt.')

        self._gemeente = OTLAttribuut(field=KlAlgGemeente,
                                      naam='gemeente',
                                      label='gemeente',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.gemeente',
                                      definition='De bestuurlijke eenheid waarin het adres gelegen is.')

        self._huisnummer = OTLAttribuut(field=StringField,
                                        naam='huisnummer',
                                        label='huisnummer',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.huisnummer',
                                        definition='Een nummer dat door de gemeente aan bv. een huis wordt toegekend.')

        self._postcode = OTLAttribuut(field=StringField,
                                      naam='postcode',
                                      label='postcode',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.postcode',
                                      definition='Een korte reeks tekens die in het postadres wordt opgenomen.')

        self._provincie = OTLAttribuut(field=KlAlgProvincie,
                                       naam='provincie',
                                       label='provincie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.provincie',
                                       definition='Het deelgebied waarin het adres gelegen is.')

        self._straatnaam = OTLAttribuut(field=StringField,
                                        naam='straatnaam',
                                        label='straatnaam',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres.straatnaam',
                                        definition='De naam van de straat.')

    @property
    def bus(self):
        """Een nummer dat de postbus aanduidt."""
        return self._bus.waarde

    @bus.setter
    def bus(self, value):
        self._bus.set_waarde(value, owner=self._parent)

    @property
    def gemeente(self):
        """De bestuurlijke eenheid waarin het adres gelegen is."""
        return self._gemeente.waarde

    @gemeente.setter
    def gemeente(self, value):
        self._gemeente.set_waarde(value, owner=self._parent)

    @property
    def huisnummer(self):
        """Een nummer dat door de gemeente aan bv. een huis wordt toegekend."""
        return self._huisnummer.waarde

    @huisnummer.setter
    def huisnummer(self, value):
        self._huisnummer.set_waarde(value, owner=self._parent)

    @property
    def postcode(self):
        """Een korte reeks tekens die in het postadres wordt opgenomen."""
        return self._postcode.waarde

    @postcode.setter
    def postcode(self, value):
        self._postcode.set_waarde(value, owner=self._parent)

    @property
    def provincie(self):
        """Het deelgebied waarin het adres gelegen is."""
        return self._provincie.waarde

    @provincie.setter
    def provincie(self, value):
        self._provincie.set_waarde(value, owner=self._parent)

    @property
    def straatnaam(self):
        """De naam van de straat."""
        return self._straatnaam.waarde

    @straatnaam.setter
    def straatnaam(self, value):
        self._straatnaam.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAdres(ComplexField, AttributeInfo):
    """Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde."""
    naam = 'DtcAdres'
    label = 'Adres'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAdres'
    definition = 'Complex datatype voor de aanduiding van een bepaalde locatie, doorgaans van een huis, woning, gebouw of faciliteit, op de aarde.'
    waardeObject = DtcAdresWaarden

    def __str__(self):
        return ComplexField.__str__(self)


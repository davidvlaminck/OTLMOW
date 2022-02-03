# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcRechtspersoonWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._adres = OTLAttribuut(field=DtcAdres,
                                   naam='adres',
                                   label='adres',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon.adres',
                                   definition='Het adres.',
                                   owner=self)

        self._afdeling = OTLAttribuut(field=StringField,
                                      naam='afdeling',
                                      label='afdeling',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon.afdeling',
                                      definition='De afdeling waartoe een rechtspersoon behoort.',
                                      owner=self)

        self._organisatie = OTLAttribuut(field=StringField,
                                         naam='organisatie',
                                         label='organisatie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon.organisatie',
                                         definition='De naam van de organisatie of rechtspersoon.',
                                         owner=self)

        self._telefoonnnummer = OTLAttribuut(field=StringField,
                                             naam='telefoonnnummer',
                                             label='telefoonnnummer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon.telefoonnnummer',
                                             definition='Het telefoonnummer.',
                                             owner=self)

    @property
    def adres(self):
        """Het adres."""
        return self._adres.waarde

    @adres.setter
    def adres(self, value):
        self._adres.set_waarde(value, owner=self._parent)

    @property
    def afdeling(self):
        """De afdeling waartoe een rechtspersoon behoort."""
        return self._afdeling.waarde

    @afdeling.setter
    def afdeling(self, value):
        self._afdeling.set_waarde(value, owner=self._parent)

    @property
    def organisatie(self):
        """De naam van de organisatie of rechtspersoon."""
        return self._organisatie.waarde

    @organisatie.setter
    def organisatie(self, value):
        self._organisatie.set_waarde(value, owner=self._parent)

    @property
    def telefoonnnummer(self):
        """Het telefoonnummer."""
        return self._telefoonnnummer.waarde

    @telefoonnnummer.setter
    def telefoonnnummer(self, value):
        self._telefoonnnummer.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcRechtspersoon(ComplexField, AttributeInfo):
    """Complex datatype voor een rechtspersoon."""
    naam = 'DtcRechtspersoon'
    label = 'Rechtspersoon'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcRechtspersoon'
    definition = 'Complex datatype voor een rechtspersoon.'
    waardeObject = DtcRechtspersoonWaarden

    def __str__(self):
        return ComplexField.__str__(self)


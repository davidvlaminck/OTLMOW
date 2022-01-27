# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLMOW.OTLModel.Datatypes.DtcOpeningsurenSpecificatie import DtcOpeningsurenSpecificatie
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcContactinfoWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._adres = OTLAttribuut(field=DtcAdres,
                                   naam='adres',
                                   label='adres',
                                   objectUri='https://schema.org/ContactPoint.adres',
                                   kardinaliteit_min='0',
                                   definition='Adres dat men kan aanschrijven of bezoeken.')

        self._beschikbaarheid = OTLAttribuut(field=DtcOpeningsurenSpecificatie,
                                             naam='beschikbaarheid',
                                             label='beschikbaarheid',
                                             objectUri='https://schema.org/ContactPoint.beschikbaarheid',
                                             kardinaliteit_min='0',
                                             kardinaliteit_max='*',
                                             definition='Periode waarin contact kan worden opgenomen.')

        self._contactnaam = OTLAttribuut(field=StringField,
                                         naam='contactnaam',
                                         label='contactnaam',
                                         objectUri='https://schema.org/ContactPoint.contactnaam',
                                         kardinaliteit_min='0',
                                         definition='Naam van bv. de persoon die men kan contacteren.')

        self._email = OTLAttribuut(field=StringField,
                                   naam='email',
                                   label='email',
                                   objectUri='https://schema.org/ContactPoint.email',
                                   kardinaliteit_min='0',
                                   definition='Email-adres waarnaar men kan mailen.')

        self._fax = OTLAttribuut(field=StringField,
                                 naam='fax',
                                 label='fax',
                                 objectUri='https://schema.org/ContactPoint.fax',
                                 kardinaliteit_min='0',
                                 definition='Faxnummer waarnaar men kan faxen.')

        self._opmerkingen = OTLAttribuut(field=StringField,
                                         naam='opmerkingen',
                                         label='opmerkingen',
                                         objectUri='https://schema.org/ContactPoint.opmerkingen',
                                         kardinaliteit_min='0',
                                         definition='Bijkomende informatie met betrekking tot het gebruik van de contactgegevens.')

        self._telefoon = OTLAttribuut(field=StringField,
                                      naam='telefoon',
                                      label='telefoon',
                                      objectUri='https://schema.org/ContactPoint.telefoon',
                                      kardinaliteit_min='0',
                                      definition='Telefoonnummer waarop men kan bellen.')

        self._website = OTLAttribuut(field=StringField,
                                     naam='website',
                                     label='website',
                                     objectUri='https://schema.org/ContactPoint.website',
                                     kardinaliteit_min='0',
                                     definition='Website waarnaar men kan surfen.')

    @property
    def adres(self):
        """Adres dat men kan aanschrijven of bezoeken."""
        return self._adres.waarde

    @adres.setter
    def adres(self, value):
        self._adres.set_waarde(value, owner=self._parent)

    @property
    def beschikbaarheid(self):
        """Periode waarin contact kan worden opgenomen."""
        return self._beschikbaarheid.waarde

    @beschikbaarheid.setter
    def beschikbaarheid(self, value):
        self._beschikbaarheid.set_waarde(value, owner=self._parent)

    @property
    def contactnaam(self):
        """Naam van bv. de persoon die men kan contacteren."""
        return self._contactnaam.waarde

    @contactnaam.setter
    def contactnaam(self, value):
        self._contactnaam.set_waarde(value, owner=self._parent)

    @property
    def email(self):
        """Email-adres waarnaar men kan mailen."""
        return self._email.waarde

    @email.setter
    def email(self, value):
        self._email.set_waarde(value, owner=self._parent)

    @property
    def fax(self):
        """Faxnummer waarnaar men kan faxen."""
        return self._fax.waarde

    @fax.setter
    def fax(self, value):
        self._fax.set_waarde(value, owner=self._parent)

    @property
    def opmerkingen(self):
        """Bijkomende informatie met betrekking tot het gebruik van de contactgegevens."""
        return self._opmerkingen.waarde

    @opmerkingen.setter
    def opmerkingen(self, value):
        self._opmerkingen.set_waarde(value, owner=self._parent)

    @property
    def telefoon(self):
        """Telefoonnummer waarop men kan bellen."""
        return self._telefoon.waarde

    @telefoon.setter
    def telefoon(self, value):
        self._telefoon.set_waarde(value, owner=self._parent)

    @property
    def website(self):
        """Website waarnaar men kan surfen."""
        return self._website.waarde

    @website.setter
    def website(self, value):
        self._website.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcContactinfo(ComplexField, AttributeInfo):
    """Complex datatype voor de informatie zoals email, telefoon, adres die toelaat om iemand of iets te contacteren."""
    naam = 'DtcContactinfo'
    label = 'Contactinfo'
    objectUri = 'https://schema.org/ContactPoint'
    definition = 'Complex datatype voor de informatie zoals email, telefoon, adres die toelaat om iemand of iets te contacteren.'
    waardeObject = DtcContactinfoWaarden

    def __str__(self):
        return ComplexField.__str__(self)


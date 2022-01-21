# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcNatuurlijkPersoonWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._achternaam = OTLAttribuut(field=StringField,
                                        naam='achternaam',
                                        label='achternaam',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.achternaam',
                                        definition='De achternaam.')

        self._adres = OTLAttribuut(field=DtcAdres,
                                   naam='adres',
                                   label='adres',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.adres',
                                   kardinaliteit_max='*',
                                   definition='Het adres.')

        self._emailadres = OTLAttribuut(field=StringField,
                                        naam='emailadres',
                                        label='emailadres',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.emailadres',
                                        kardinaliteit_max='*',
                                        definition='Het emailadres.')

        self._fax = OTLAttribuut(field=StringField,
                                 naam='fax',
                                 label='fax',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.fax',
                                 kardinaliteit_max='*',
                                 definition='De faxnummer.')

        self._heeftEmailVoorkeur = OTLAttribuut(field=BooleanField,
                                                naam='heeftEmailVoorkeur',
                                                label='heeft email voorkeur',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.heeftEmailVoorkeur',
                                                definition='Aanduiding of een persoon de voorkeur heeft om via email gecontacteerd te worden.')

        self._heeftFaxVoorkeur = OTLAttribuut(field=BooleanField,
                                              naam='heeftFaxVoorkeur',
                                              label='heeft fax voorkeur',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.heeftFaxVoorkeur',
                                              definition='Aanduiding of een persoon een voorkeur heeft om via fax gegevens te ontvangen.')

        self._telefoonnnummer = OTLAttribuut(field=StringField,
                                             naam='telefoonnnummer',
                                             label='telefoonnnummer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.telefoonnnummer',
                                             kardinaliteit_max='*',
                                             definition='Het telefoonnummer.')

        self._voornaam = OTLAttribuut(field=StringField,
                                      naam='voornaam',
                                      label='voornaam',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon.voornaam',
                                      definition='De voornaam.')

    @property
    def achternaam(self):
        """De achternaam."""
        return self._achternaam.waarde

    @achternaam.setter
    def achternaam(self, value):
        self._achternaam.set_waarde(value, owner=self._parent)

    @property
    def adres(self):
        """Het adres."""
        return self._adres.waarde

    @adres.setter
    def adres(self, value):
        self._adres.set_waarde(value, owner=self._parent)

    @property
    def emailadres(self):
        """Het emailadres."""
        return self._emailadres.waarde

    @emailadres.setter
    def emailadres(self, value):
        self._emailadres.set_waarde(value, owner=self._parent)

    @property
    def fax(self):
        """De faxnummer."""
        return self._fax.waarde

    @fax.setter
    def fax(self, value):
        self._fax.set_waarde(value, owner=self._parent)

    @property
    def heeftEmailVoorkeur(self):
        """Aanduiding of een persoon de voorkeur heeft om via email gecontacteerd te worden."""
        return self._heeftEmailVoorkeur.waarde

    @heeftEmailVoorkeur.setter
    def heeftEmailVoorkeur(self, value):
        self._heeftEmailVoorkeur.set_waarde(value, owner=self._parent)

    @property
    def heeftFaxVoorkeur(self):
        """Aanduiding of een persoon een voorkeur heeft om via fax gegevens te ontvangen."""
        return self._heeftFaxVoorkeur.waarde

    @heeftFaxVoorkeur.setter
    def heeftFaxVoorkeur(self, value):
        self._heeftFaxVoorkeur.set_waarde(value, owner=self._parent)

    @property
    def telefoonnnummer(self):
        """Het telefoonnummer."""
        return self._telefoonnnummer.waarde

    @telefoonnnummer.setter
    def telefoonnnummer(self, value):
        self._telefoonnnummer.set_waarde(value, owner=self._parent)

    @property
    def voornaam(self):
        """De voornaam."""
        return self._voornaam.waarde

    @voornaam.setter
    def voornaam(self, value):
        self._voornaam.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcNatuurlijkPersoon(ComplexField, AttributeInfo):
    """Complex datatype dat een natuurlijk persoon beschrijft."""
    naam = 'DtcNatuurlijkPersoon'
    label = 'Natuurlijk persoon'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcNatuurlijkPersoon'
    definition = 'Complex datatype dat een natuurlijk persoon beschrijft.'
    waardeObject = DtcNatuurlijkPersoonWaarden

    def __str__(self):
        return ComplexField.__str__(self)


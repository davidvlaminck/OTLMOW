# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMToestand import AIMToestand
from OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Derdenobject(AIMToestand, AIMDBStatus, AttributeInfo):
    """Object niet in eigendom van de assetbeheerder dat zonder verdere typering bewaard wordt om relaties met getypeerde assets te kunnen beheren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMDBStatus.__init__(self)
        AIMToestand.__init__(self)
        AttributeInfo.__init__(self)

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='asset-id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.assetId',
                                     definition='Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.')

        self._contactgegevens = OTLAttribuut(field=StringField,
                                             naam='contactgegevens',
                                             label='contactgegevens',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.contactgegevens',
                                             definition='Naam, voornaam, telefoonnummer en/of e-mailadres van de contactpersoon.')

        self._foto = OTLAttribuut(field=DtcDocument,
                                  naam='foto',
                                  label='foto',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.foto',
                                  usagenote='Enkel bestanden die een foto zijn.',
                                  kardinaliteit_max='*',
                                  definition='Een foto van het derdenobject die eventuele detailinformatie weergeeft.')

        self._heeftAansluitkastGeintegreerd = OTLAttribuut(field=BooleanField,
                                                           naam='heeftAansluitkastGeintegreerd',
                                                           label='heeft aansluitkast geïntegreerd',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.heeftAansluitkastGeintegreerd',
                                                           definition='Aanduiding of de aansluitkast geïntegreerd is.')

        self._omschrijving = OTLAttribuut(field=StringField,
                                          naam='omschrijving',
                                          label='omschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.omschrijving',
                                          definition='Omschrijving van het derdenobject.')

    @property
    def assetId(self):
        """Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier."""
        return self._assetId.waarde

    @assetId.setter
    def assetId(self, value):
        self._assetId.set_waarde(value, owner=self)

    @property
    def contactgegevens(self):
        """Naam, voornaam, telefoonnummer en/of e-mailadres van de contactpersoon."""
        return self._contactgegevens.waarde

    @contactgegevens.setter
    def contactgegevens(self, value):
        self._contactgegevens.set_waarde(value, owner=self)

    @property
    def foto(self):
        """Een foto van het derdenobject die eventuele detailinformatie weergeeft."""
        return self._foto.waarde

    @foto.setter
    def foto(self, value):
        self._foto.set_waarde(value, owner=self)

    @property
    def heeftAansluitkastGeintegreerd(self):
        """Aanduiding of de aansluitkast geïntegreerd is."""
        return self._heeftAansluitkastGeintegreerd.waarde

    @heeftAansluitkastGeintegreerd.setter
    def heeftAansluitkastGeintegreerd(self, value):
        self._heeftAansluitkastGeintegreerd.set_waarde(value, owner=self)

    @property
    def omschrijving(self):
        """Omschrijving van het derdenobject."""
        return self._omschrijving.waarde

    @omschrijving.setter
    def omschrijving(self, value):
        self._omschrijving.set_waarde(value, owner=self)

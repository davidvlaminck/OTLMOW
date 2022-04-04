# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMToestand import AIMToestand
from OTLMOW.OTLModel.Classes.AIMDBStatus import AIMDBStatus
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAsset import OTLAsset
from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Derdenobject(AIMToestand, AIMDBStatus, AttributeInfo, OTLAsset, RelatieInteractor, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Object niet in eigendom van de assetbeheerder dat zonder verdere typering bewaard wordt om relaties met getypeerde assets te kunnen beheren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMDBStatus.__init__(self)
        AIMToestand.__init__(self)
        AttributeInfo.__init__(self)
        OTLAsset.__init__(self)
        RelatieInteractor.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._assetId = OTLAttribuut(field=DtcIdentificator,
                                     naam='assetId',
                                     label='asset-id',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.assetId',
                                     definition='Unieke identificatie van de asset zoals toegekend door de assetbeheerder of n.a.v. eerste aanlevering door de leverancier.',
                                     owner=self)

        self._contactgegevens = OTLAttribuut(field=StringField,
                                             naam='contactgegevens',
                                             label='contactgegevens',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.contactgegevens',
                                             definition='Naam, voornaam, telefoonnummer en/of e-mailadres van de contactpersoon.',
                                             owner=self)

        self._foto = OTLAttribuut(field=DtcDocument,
                                  naam='foto',
                                  label='foto',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.foto',
                                  usagenote='Enkel bestanden die een foto zijn.',
                                  kardinaliteit_max='*',
                                  definition='Een foto van het derdenobject die eventuele detailinformatie weergeeft.',
                                  owner=self)

        self._heeftAansluitkastGeintegreerd = OTLAttribuut(field=BooleanField,
                                                           naam='heeftAansluitkastGeintegreerd',
                                                           label='heeft aansluitkast geïntegreerd',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.heeftAansluitkastGeintegreerd',
                                                           definition='Aanduiding of de aansluitkast geïntegreerd is.',
                                                           owner=self)

        self._omschrijving = OTLAttribuut(field=StringField,
                                          naam='omschrijving',
                                          label='omschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject.omschrijving',
                                          definition='Omschrijving van het derdenobject.',
                                          owner=self)

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

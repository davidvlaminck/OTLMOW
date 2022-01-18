# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.NaampadObject import NaampadObject
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KlNetwerklinkMediumtype import KlNetwerklinkMediumtype
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Link(NaampadObject, AttributeInfo):
    """Het (glasvezel) traject tussen twee toestellen (NetwerkElementen) die rechtstreeks met mekaar communiceren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        NaampadObject.__init__(self)

        self._geleidingsgroepTnummer = OTLAttribuut(field=IntegerField,
                                                    naam='geleidingsgroepTnummer',
                                                    label='geleidingsgroep T-nummer',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link.geleidingsgroepTnummer',
                                                    definition='T-nummer van de geleidingsgroep in de kabelnet toepassing.')

        self._mediumtype = OTLAttribuut(field=KlNetwerklinkMediumtype,
                                        naam='mediumtype',
                                        label='mediumtype',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link.mediumtype',
                                        definition='Geeft aan hoe de verbinding tussen Netwerkelementen fysiek gerealiseerd wordt')

        self._ring = OTLAttribuut(field=StringField,
                                  naam='ring',
                                  label='ring',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link.ring',
                                  definition='Naam van de ringstructuur in het transport netwerk.')

    @property
    def geleidingsgroepTnummer(self):
        """T-nummer van de geleidingsgroep in de kabelnet toepassing."""
        return self._geleidingsgroepTnummer.waarde

    @geleidingsgroepTnummer.setter
    def geleidingsgroepTnummer(self, value):
        self._geleidingsgroepTnummer.set_waarde(value, owner=self)

    @property
    def mediumtype(self):
        """Geeft aan hoe de verbinding tussen Netwerkelementen fysiek gerealiseerd wordt"""
        return self._mediumtype.waarde

    @mediumtype.setter
    def mediumtype(self, value):
        self._mediumtype.set_waarde(value, owner=self)

    @property
    def ring(self):
        """Naam van de ringstructuur in het transport netwerk."""
        return self._ring.waarde

    @ring.setter
    def ring(self, value):
        self._ring.set_waarde(value, owner=self)

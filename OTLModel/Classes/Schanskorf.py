# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AndereVerharding import AndereVerharding
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlSchanskorfVorm import KlSchanskorfVorm
from OTLModel.Datatypes.KlStortsteenKaliber import KlStortsteenKaliber
from OTLModel.Datatypes.KlStortsteenType import KlStortsteenType
from OTLModel.Datatypes.KlTypeSchanskorf import KlTypeSchanskorf


# Generated with OTLClassCreator. To modify: extend, do not edit
class Schanskorf(AndereVerharding, AttributeInfo):
    """Een schanskorf bestaat uit een metalen gaasnet dat wordt gevuld met steenachtige materialen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereVerharding.__init__(self)
        AttributeInfo.__init__(self)

        self._heeftVerankeringspalen = OTLAttribuut(field=BooleanField,
                                                    naam='heeftVerankeringspalen',
                                                    label='heeft verankeringspalen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.heeftVerankeringspalen',
                                                    definition='Aanduiding of de palen de functie hebben om een schanskorf te verankeren.')

        self._isGegalvaniseerd = OTLAttribuut(field=BooleanField,
                                              naam='isGegalvaniseerd',
                                              label='is gegalvaniseerd',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.isGegalvaniseerd',
                                              definition='Aanduiding of de schanskorf gegalvaniseerd is.')

        self._isGelast = OTLAttribuut(field=BooleanField,
                                      naam='isGelast',
                                      label='is gelast',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.isGelast',
                                      definition='Aanduiding of de schanskorf gelast is.')

        self._kaliber = OTLAttribuut(field=KlStortsteenKaliber,
                                     naam='kaliber',
                                     label='kaliber',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.kaliber',
                                     definition='Het kaliber of gemiddelde diameter van de stenen in de schanskorf.')

        self._materiaalVulling = OTLAttribuut(field=KlStortsteenType,
                                              naam='materiaalVulling',
                                              label='materiaalvulling',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.materiaalVulling',
                                              definition='Het soort stenen waaruit de opvulling van een schanskorf bestaat.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de schanskorven als bijlage.')

        self._type = OTLAttribuut(field=KlTypeSchanskorf,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.type',
                                  definition='Duidt het type schanskorf aan.')

        self._vorm = OTLAttribuut(field=KlSchanskorfVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.vorm',
                                  definition='De gebruikte vorm van de schanskorf.')

    @property
    def heeftVerankeringspalen(self):
        """Aanduiding of de palen de functie hebben om een schanskorf te verankeren."""
        return self._heeftVerankeringspalen.waarde

    @heeftVerankeringspalen.setter
    def heeftVerankeringspalen(self, value):
        self._heeftVerankeringspalen.set_waarde(value, owner=self)

    @property
    def isGegalvaniseerd(self):
        """Aanduiding of de schanskorf gegalvaniseerd is."""
        return self._isGegalvaniseerd.waarde

    @isGegalvaniseerd.setter
    def isGegalvaniseerd(self, value):
        self._isGegalvaniseerd.set_waarde(value, owner=self)

    @property
    def isGelast(self):
        """Aanduiding of de schanskorf gelast is."""
        return self._isGelast.waarde

    @isGelast.setter
    def isGelast(self, value):
        self._isGelast.set_waarde(value, owner=self)

    @property
    def kaliber(self):
        """Het kaliber of gemiddelde diameter van de stenen in de schanskorf."""
        return self._kaliber.waarde

    @kaliber.setter
    def kaliber(self, value):
        self._kaliber.set_waarde(value, owner=self)

    @property
    def materiaalVulling(self):
        """Het soort stenen waaruit de opvulling van een schanskorf bestaat."""
        return self._materiaalVulling.waarde

    @materiaalVulling.setter
    def materiaalVulling(self, value):
        self._materiaalVulling.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de schanskorven als bijlage."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self):
        """Duidt het type schanskorf aan."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """De gebruikte vorm van de schanskorf."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)

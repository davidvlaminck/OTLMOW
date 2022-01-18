# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlCADOMerk import KlCADOMerk
from OTLModel.Datatypes.KlCADOModelnaam import KlCADOModelnaam
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Calamiteitendoorsteek(AIMNaamObject, AttributeInfo):
    """Een calamiteitendoorsteek, afgekort CADO, is een mechanische constructie voor het opklappen van een deel van de vangrail in de middenberm van een weg. Het primaire doel van de calamiteitendoorsteek is het doorlaten van hulpverleningsvoertuigen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

        self._isDubbelArmig = OTLAttribuut(field=BooleanField,
                                           naam='isDubbelArmig',
                                           label='is dubbelarmig',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.isDubbelArmig',
                                           definition='Aanduiding of de calamiteitendoorsteek dubbel armig is.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.lengte',
                                    definition='De totale lengte van de calamiteitendoorsteek constructie.')

        self._merk = OTLAttribuut(field=KlCADOMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.merk',
                                  definition='Het merk van de calamiteitendoorsteek.')

        self._modelnaam = OTLAttribuut(field=KlCADOModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.modelnaam',
                                       definition='De modelnaam van de calamiteitendoorsteek.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.technischeFiche',
                                             definition='De technische fiche van de calamiteitendoorsteek.')

    @property
    def isDubbelArmig(self):
        """Aanduiding of de calamiteitendoorsteek dubbel armig is."""
        return self._isDubbelArmig.waarde

    @isDubbelArmig.setter
    def isDubbelArmig(self, value):
        self._isDubbelArmig.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De totale lengte van de calamiteitendoorsteek constructie."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de calamiteitendoorsteek."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de calamiteitendoorsteek."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de calamiteitendoorsteek."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

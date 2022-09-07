# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlCADOMerk import KlCADOMerk
from OTLMOW.OTLModel.Datatypes.KlCADOModelnaam import KlCADOModelnaam
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Calamiteitendoorsteek(AIMNaamObject, LijnGeometrie):
    """Een calamiteitendoorsteek, afgekort CADO, is een mechanische constructie voor het opklappen van een deel van de vangrail in de middenberm van een weg. Het primaire doel van de calamiteitendoorsteek is het doorlaten van hulpverleningsvoertuigen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart')

        self._isDubbelArmig = OTLAttribuut(field=BooleanField,
                                           naam='isDubbelArmig',
                                           label='is dubbelarmig',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.isDubbelArmig',
                                           definition='Aanduiding of de calamiteitendoorsteek dubbel armig is.',
                                           owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.lengte',
                                    definition='De totale lengte van de calamiteitendoorsteek constructie.',
                                    owner=self)

        self._merk = OTLAttribuut(field=KlCADOMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.merk',
                                  definition='Het merk van de calamiteitendoorsteek.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlCADOModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.modelnaam',
                                       definition='De modelnaam van de calamiteitendoorsteek.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.technischeFiche',
                                             definition='De technische fiche van de calamiteitendoorsteek.',
                                             owner=self)

    @property
    def isDubbelArmig(self):
        """Aanduiding of de calamiteitendoorsteek dubbel armig is."""
        return self._isDubbelArmig.get_waarde()

    @isDubbelArmig.setter
    def isDubbelArmig(self, value):
        self._isDubbelArmig.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De totale lengte van de calamiteitendoorsteek constructie."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de calamiteitendoorsteek."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de calamiteitendoorsteek."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de calamiteitendoorsteek."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

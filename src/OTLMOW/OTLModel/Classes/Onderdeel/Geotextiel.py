# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AndereLaag import AndereLaag
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlGeotextielType import KlGeotextielType
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geotextiel(AndereLaag, VlakGeometrie):
    """Geotextiel om grondoppervlakken, taluds en/of bodems te beschermen tegen erosie door wind, golfslag en/of stroming van water, afkomstig hetzij van afstromende neerslag, hetzij van afvloeiend oppervlaktewater."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._heeftVulling = OTLAttribuut(field=BooleanField,
                                          naam='heeftVulling',
                                          label='heeft vulling',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.heeftVulling',
                                          definition='Aanduiding of er vulling zoals bv. houtsnippers, grind,... in een omhulsel van geotextiel aanwezig is.',
                                          owner=self)

        self._isBiodegradeerbaar = OTLAttribuut(field=BooleanField,
                                                naam='isBiodegradeerbaar',
                                                label='is biodegradeerbaar',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.isBiodegradeerbaar',
                                                definition='Aanduiding of het geotextiel al dan niet biologisch degradeerbaar is.',
                                                owner=self)

        self._isIngezaaid = OTLAttribuut(field=BooleanField,
                                         naam='isIngezaaid',
                                         label='is ingezaaid',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.isIngezaaid',
                                         definition='Aanduiding of er in het geotextiel zaden aanwezig zijn.',
                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van het geotextiel.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlGeotextielType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel.type',
                                  definition='Het type geotextiel.',
                                  owner=self)

    @property
    def heeftVulling(self):
        """Aanduiding of er vulling zoals bv. houtsnippers, grind,... in een omhulsel van geotextiel aanwezig is."""
        return self._heeftVulling.get_waarde()

    @heeftVulling.setter
    def heeftVulling(self, value):
        self._heeftVulling.set_waarde(value, owner=self)

    @property
    def isBiodegradeerbaar(self):
        """Aanduiding of het geotextiel al dan niet biologisch degradeerbaar is."""
        return self._isBiodegradeerbaar.get_waarde()

    @isBiodegradeerbaar.setter
    def isBiodegradeerbaar(self, value):
        self._isBiodegradeerbaar.set_waarde(value, owner=self)

    @property
    def isIngezaaid(self):
        """Aanduiding of er in het geotextiel zaden aanwezig zijn."""
        return self._isIngezaaid.get_waarde()

    @isIngezaaid.setter
    def isIngezaaid(self, value):
        self._isIngezaaid.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van het geotextiel."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type geotextiel."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

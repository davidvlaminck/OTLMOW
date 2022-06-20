# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLMOW.OTLModel.Datatypes.KlOmvormerMerk import KlOmvormerMerk
from OTLMOW.OTLModel.Datatypes.KlOmvormerModelnaam import KlOmvormerModelnaam
from OTLMOW.OTLModel.Datatypes.KlOmvormerType import KlOmvormerType
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Omvormer(AIMNaamObject, PuntGeometrie):
    """Een object, bijna altijd geplaatst in paar geplaatst, omvorming en "de"-omvorming, dat een signaal binnenneemt en terug uitstuurt maar dan  op een andere manier. Er zijn een hele reeks manieren.

- Omvorming waar er gewijzigd wordt van type kabel om dezelfde boodschap over te versturen, bv. omvorming van UTP naar Coax.

- Omvorming van codering bv. analoog naar digitaal en in omgekeerde richting digitaal naar analoog (omvorming van codering analoog-digitaal verschilt van een encoder omdat een encoder een eindproduct aflevert; in dit geval is de omvorming ter ondersteuning het transport en zal er altijd een omvorming zijn terug naar analoog)

- Omvorming  die de gegevens opnieuw versterkt zodat ze over een langere afstand kunnen getransporteerd worden. Deze variant heeft niet noodzakelijk een tweede omvormer om terug te gaan naar het origineel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.',
                                     owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.ipAdres',
                                     definition='Het IP-adres van de omvormer.',
                                     owner=self)

        self._merk = OTLAttribuut(field=KlOmvormerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.merk',
                                  definition='Het merk van de omvormer.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlOmvormerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.modelnaam',
                                       definition='De modelnaam van de omvormer.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.technischeFiche',
                                             usagenote='Bestanden van het type pdf.',
                                             definition='Technische fiche van de omvormer.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlOmvormerType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer.type',
                                  definition='De soort omvorming die gebeurt er in de omvormer.',
                                  owner=self)

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.get_waarde()

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """Het IP-adres van de omvormer."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de omvormer."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de omvormer."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """Technische fiche van de omvormer."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self):
        """De soort omvorming die gebeurt er in de omvormer."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLMOW.OTLModel.Datatypes.KlANPRMerk import KlANPRMerk
from OTLMOW.OTLModel.Datatypes.KlANPRModelnaam import KlANPRModelnaam
from OTLMOW.OTLModel.Datatypes.KlAlgRijrichting import KlAlgRijrichting
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ANPRCamera(AIMNaamObject, PuntGeometrie):
    """Nummerplaatherkenningscamera: een camera die als output de nummerplaat van een voertuig in tekst geeft en een foto van het deel van het voertuig waar de nummerplaat zich bevindt. Afhankelijk van het merk en type gecombineerd met een al dan niet bewegend overzichtsbeeld."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.',
                                     owner=self)

        self._heeftFlits = OTLAttribuut(field=BooleanField,
                                        naam='heeftFlits',
                                        label='heeft flits',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.heeftFlits',
                                        definition='Geeft aan of de camera een externe infrarood flits heeft.',
                                        owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.ipAdres',
                                     definition='IP-adres van de ANPR-camera.',
                                     owner=self)

        self._merk = OTLAttribuut(field=KlANPRMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.merk',
                                  definition='Het merk van de ANPR-camera.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlANPRModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.modelnaam',
                                       definition='De modelnaam van de ANPR-camera.',
                                       owner=self)

        self._rijrichting = OTLAttribuut(field=KlAlgRijrichting,
                                         naam='rijrichting',
                                         label='rijrichting',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.rijrichting',
                                         definition='De rijrichting van de voertuigen die door de camera geregistreerd worden.',
                                         owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera.technischeFiche',
                                             usagenote='Bestanden van het type pdf.',
                                             definition='Technische fiche van dit element.',
                                             owner=self)

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.waarde

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def heeftFlits(self):
        """Geeft aan of de camera een externe infrarood flits heeft."""
        return self._heeftFlits.waarde

    @heeftFlits.setter
    def heeftFlits(self, value):
        self._heeftFlits.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """IP-adres van de ANPR-camera."""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de ANPR-camera."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de ANPR-camera."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def rijrichting(self):
        """De rijrichting van de voertuigen die door de camera geregistreerd worden."""
        return self._rijrichting.waarde

    @rijrichting.setter
    def rijrichting(self, value):
        self._rijrichting.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """Technische fiche van dit element."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

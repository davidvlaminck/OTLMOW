# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.Verkeersbord import Verkeersbord
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class LEDBord(AIMNaamObject, Verkeersbord):
    """Abstracte klasse die de gemeenschappelijke eigenschappen van verschillende types dynamische verkeersborden groepeert."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        Verkeersbord.__init__(self)

        self._aantalLichtsensoren = OTLAttribuut(field=IntegerField,
                                                 naam='aantalLichtsensoren',
                                                 label='aantal lichtsensoren',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.aantalLichtsensoren',
                                                 definition='Het aantal lichtsensoren waar het bord over beschikt die continu de intensiteit van het invallend licht meten.')

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.')

        self._heeftDeurcontact = OTLAttribuut(field=BooleanField,
                                              naam='heeftDeurcontact',
                                              label='heeft deurcontact',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.heeftDeurcontact',
                                              definition='Het LEDBord is beveiligd met een deurcontact dat waarschuwt voor ongeoorloofd openen van het bord door middel van een software-matig alarm.')

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.ipAdres',
                                     definition='Het IP netwerkadres van het LEDBord.')

        self._logischeGroepVerkeerscentrum = OTLAttribuut(field=StringField,
                                                          naam='logischeGroepVerkeerscentrum',
                                                          label='logische groep verkeerscentrum',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.logischeGroepVerkeerscentrum',
                                                          definition='Identificator van de logische groep toegekend door het Verkeerscentrum.')

        self._protocol = OTLAttribuut(field=StringField,
                                      naam='protocol',
                                      label='protocol',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.protocol',
                                      definition='Communicatieprotocol waarmee het LEDBord wordt aangestuurd.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.technischeFiche',
                                             definition='Document met technische informatie over het LEDBord.')

        self._versie = OTLAttribuut(field=StringField,
                                    naam='versie',
                                    label='versie',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord.versie',
                                    definition='Versie van het LEDBord.')

    @property
    def aantalLichtsensoren(self):
        """Het aantal lichtsensoren waar het bord over beschikt die continu de intensiteit van het invallend licht meten."""
        return self._aantalLichtsensoren.waarde

    @aantalLichtsensoren.setter
    def aantalLichtsensoren(self, value):
        self._aantalLichtsensoren.set_waarde(value, owner=self)

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.waarde

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def heeftDeurcontact(self):
        """Het LEDBord is beveiligd met een deurcontact dat waarschuwt voor ongeoorloofd openen van het bord door middel van een software-matig alarm."""
        return self._heeftDeurcontact.waarde

    @heeftDeurcontact.setter
    def heeftDeurcontact(self, value):
        self._heeftDeurcontact.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """Het IP netwerkadres van het LEDBord."""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def logischeGroepVerkeerscentrum(self):
        """Identificator van de logische groep toegekend door het Verkeerscentrum."""
        return self._logischeGroepVerkeerscentrum.waarde

    @logischeGroepVerkeerscentrum.setter
    def logischeGroepVerkeerscentrum(self, value):
        self._logischeGroepVerkeerscentrum.set_waarde(value, owner=self)

    @property
    def protocol(self):
        """Communicatieprotocol waarmee het LEDBord wordt aangestuurd."""
        return self._protocol.waarde

    @protocol.setter
    def protocol(self, value):
        self._protocol.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """Document met technische informatie over het LEDBord."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def versie(self):
        """Versie van het LEDBord."""
        return self._versie.waarde

    @versie.setter
    def versie(self, value):
        self._versie.set_waarde(value, owner=self)

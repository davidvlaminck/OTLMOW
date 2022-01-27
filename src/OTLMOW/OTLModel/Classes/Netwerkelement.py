# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from src.OTLMOW.OTLModel.Datatypes.KlNetwerkMerk import KlNetwerkMerk
from src.OTLMOW.OTLModel.Datatypes.KlNetwerkelemGebruik import KlNetwerkelemGebruik
from src.OTLMOW.OTLModel.Datatypes.KlNetwerkelemModelnaam import KlNetwerkelemModelnaam
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Netwerkelement(AIMNaamObject):
    """Toestel,onderdeel van het netwerk,waarop netwerkverbindingen kunnen aangelegd worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._beschrijvingFabrikant = OTLAttribuut(field=StringField,
                                                   naam='beschrijvingFabrikant',
                                                   label='beschrijving fabrikant',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.beschrijvingFabrikant',
                                                   definition='Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant.')

        self._gebruik = OTLAttribuut(field=KlNetwerkelemGebruik,
                                     naam='gebruik',
                                     label='gebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.gebruik',
                                     definition='Toestel, onderdeel van het netwerk, waarop netwerkverbindingen kunnen aangelegd worden.')

        self._ipAddressBeheer = OTLAttribuut(field=DteIPv4Adres,
                                             naam='ipAddressBeheer',
                                             label='IP address beheer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.ipAddressBeheer',
                                             definition='IP adres van het toestel.')

        self._ipAddressMask = OTLAttribuut(field=DteIPv4Adres,
                                           naam='ipAddressMask',
                                           label='IP address mask',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.ipAddressMask',
                                           definition='IP adres mask van het toestel.')

        self._ipGateway = OTLAttribuut(field=DteIPv4Adres,
                                       naam='ipGateway',
                                       label='IP gateway',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.ipGateway',
                                       definition='IP adres van gateway.')

        self._merk = OTLAttribuut(field=KlNetwerkMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.merk',
                                  definition='Merk waarmee de fabrikant het netwerkelement identificeert.')

        self._modelnaam = OTLAttribuut(field=KlNetwerkelemModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.modelnaam',
                                       definition='Modelnaam waarmee de fabrikant dit type toestel identificeert.')

        self._nSAPAddress = OTLAttribuut(field=StringField,
                                         naam='nSAPAddress',
                                         label='NSAP-address',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.nSAPAddress',
                                         definition='Netwerkadres van deze component.')

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.serienummer',
                                         definition='Unieke identificatiecode van het toestel, toegekend door de fabrikant.')

        self._softwareVersie = OTLAttribuut(field=StringField,
                                            naam='softwareVersie',
                                            label='software versie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement.softwareVersie',
                                            definition='Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook de firmwareversie zijn.')

    @property
    def beschrijvingFabrikant(self):
        """Bijkomende specificaties over het apparaat of onderdeel type van de fabrikant."""
        return self._beschrijvingFabrikant.waarde

    @beschrijvingFabrikant.setter
    def beschrijvingFabrikant(self, value):
        self._beschrijvingFabrikant.set_waarde(value, owner=self)

    @property
    def gebruik(self):
        """Toestel, onderdeel van het netwerk, waarop netwerkverbindingen kunnen aangelegd worden."""
        return self._gebruik.waarde

    @gebruik.setter
    def gebruik(self, value):
        self._gebruik.set_waarde(value, owner=self)

    @property
    def ipAddressBeheer(self):
        """IP adres van het toestel."""
        return self._ipAddressBeheer.waarde

    @ipAddressBeheer.setter
    def ipAddressBeheer(self, value):
        self._ipAddressBeheer.set_waarde(value, owner=self)

    @property
    def ipAddressMask(self):
        """IP adres mask van het toestel."""
        return self._ipAddressMask.waarde

    @ipAddressMask.setter
    def ipAddressMask(self, value):
        self._ipAddressMask.set_waarde(value, owner=self)

    @property
    def ipGateway(self):
        """IP adres van gateway."""
        return self._ipGateway.waarde

    @ipGateway.setter
    def ipGateway(self, value):
        self._ipGateway.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merk waarmee de fabrikant het netwerkelement identificeert."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam waarmee de fabrikant dit type toestel identificeert."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def nSAPAddress(self):
        """Netwerkadres van deze component."""
        return self._nSAPAddress.waarde

    @nSAPAddress.setter
    def nSAPAddress(self, value):
        self._nSAPAddress.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """Unieke identificatiecode van het toestel, toegekend door de fabrikant."""
        return self._serienummer.waarde

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def softwareVersie(self):
        """Identificatie van de softwareversie die op dit apparaat of onderdeel geladen is. Dit kan ook de firmwareversie zijn."""
        return self._softwareVersie.waarde

    @softwareVersie.setter
    def softwareVersie(self, value):
        self._softwareVersie.set_waarde(value, owner=self)

# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KlHardwareCdDvdTape import KlHardwareCdDvdTape
from OTLModel.Datatypes.KlHardwareDomein import KlHardwareDomein
from OTLModel.Datatypes.KlHardwareOS import KlHardwareOS
from OTLModel.Datatypes.KwantWrdInGigabyte import KwantWrdInGigabyte
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class HardwareToegang(AIMNaamObject):
    """Een abstracte die de gemeenschappelijke kenmerken bevat voor zowel fysieke als virtuele hardware."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._CPU = OTLAttribuut(field=StringField,
                                 naam='CPU',
                                 label='CPU',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.CPU',
                                 definition='Centrale verwerkingseenheid.')

        self._cdDvdTape = OTLAttribuut(field=KlHardwareCdDvdTape,
                                       naam='cdDvdTape',
                                       label='CD DVD Tape',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.cdDvdTape',
                                       definition='De hardware uitgerust met CD/DVD/Tape.')

        self._disk = OTLAttribuut(field=KwantWrdInGigabyte,
                                  naam='disk',
                                  label='disk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.disk',
                                  definition='De disk config van de hardware, HD, RAID, ...')

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.')

        self._domein = OTLAttribuut(field=KlHardwareDomein,
                                    naam='domein',
                                    label='domein',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.domein',
                                    definition='Administratieve groepering van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur.')

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.ipAdres',
                                     kardinaliteit_max='*',
                                     definition='Het IP-adres van de hardware.')

        self._licentie = OTLAttribuut(field=StringField,
                                      naam='licentie',
                                      label='licentie',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.licentie',
                                      definition='De licentie van het OS of de licentie van de hardware voor support/garantie op componenten.')

        self._os = OTLAttribuut(field=KlHardwareOS,
                                naam='os',
                                label='OS',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.os',
                                definition='Het besturingssysteem dat op de hardware draait.')

        self._ram = OTLAttribuut(field=KwantWrdInGigabyte,
                                 naam='ram',
                                 label='RAM',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.ram',
                                 definition='De grootte van het werkgeheugen.')

    @property
    def CPU(self):
        """Centrale verwerkingseenheid."""
        return self._CPU.waarde

    @CPU.setter
    def CPU(self, value):
        self._CPU.set_waarde(value, owner=self)

    @property
    def cdDvdTape(self):
        """De hardware uitgerust met CD/DVD/Tape."""
        return self._cdDvdTape.waarde

    @cdDvdTape.setter
    def cdDvdTape(self, value):
        self._cdDvdTape.set_waarde(value, owner=self)

    @property
    def disk(self):
        """De disk config van de hardware, HD, RAID, ..."""
        return self._disk.waarde

    @disk.setter
    def disk(self, value):
        self._disk.set_waarde(value, owner=self)

    @property
    def dnsNaam(self):
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.waarde

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def domein(self):
        """Administratieve groepering van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur."""
        return self._domein.waarde

    @domein.setter
    def domein(self, value):
        self._domein.set_waarde(value, owner=self)

    @property
    def ipAdres(self):
        """Het IP-adres van de hardware."""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def licentie(self):
        """De licentie van het OS of de licentie van de hardware voor support/garantie op componenten."""
        return self._licentie.waarde

    @licentie.setter
    def licentie(self, value):
        self._licentie.set_waarde(value, owner=self)

    @property
    def os(self):
        """Het besturingssysteem dat op de hardware draait."""
        return self._os.waarde

    @os.setter
    def os(self, value):
        self._os.set_waarde(value, owner=self)

    @property
    def ram(self):
        """De grootte van het werkgeheugen."""
        return self._ram.waarde

    @ram.setter
    def ram(self, value):
        self._ram.set_waarde(value, owner=self)

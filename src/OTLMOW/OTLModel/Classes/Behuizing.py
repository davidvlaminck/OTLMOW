# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Behuizing(AIMNaamObject):
    """Abstracte voor alle types van behuizing voor het beschermen van technieken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._adres = OTLAttribuut(field=DtcAdres,
                                   naam='adres',
                                   label='adres',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing.adres',
                                   definition='Adres (aanduiding van de locatie) van de behuizing. Indien deze geen adres heeft, wordt net zoals door Fluvius voor cabines, het adres van een nabijgelegen straat genomen.',
                                   owner=self)

        self._risicoanalyse = OTLAttribuut(field=DtcDocument,
                                           naam='risicoanalyse',
                                           label='risicoanalyse',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing.risicoanalyse',
                                           usagenote='De risicoanalyse heeft in eerste instantie betrekking op werken in en rond een behuziing met elektrische installaties. Voor behuizingen met installaties van de distributienetbeheerder wordt de risicoanalyse bestemd voor die beheerder, bewaard in het gelijknamig attribuut van het onderdeel van die beheerder, bv. EnergiemeterDNB.',
                                           definition='Een bestandsbijlage met de risicoanalyse voor werken in en rond een behuizing.',
                                           owner=self)

        self._tabelUitwendigeInvloeden = OTLAttribuut(field=DtcDocument,
                                                      naam='tabelUitwendigeInvloeden',
                                                      label='tabel uitwendige invloeden',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing.tabelUitwendigeInvloeden',
                                                      usagenote='De tabel is in eerste instantie enkel vereist voor behuizingen die elektrische installaties bevatten die onder het AREI vallen. ',
                                                      definition='Een bestandsbijlage met de ingevulde en actuele tabel uitwendige invloeden zoals vereist door het AREI voor bepaalde elektrische installaties.',
                                                      owner=self)

    @property
    def adres(self):
        """Adres (aanduiding van de locatie) van de behuizing. Indien deze geen adres heeft, wordt net zoals door Fluvius voor cabines, het adres van een nabijgelegen straat genomen."""
        return self._adres.waarde

    @adres.setter
    def adres(self, value):
        self._adres.set_waarde(value, owner=self)

    @property
    def risicoanalyse(self):
        """Een bestandsbijlage met de risicoanalyse voor werken in en rond een behuizing."""
        return self._risicoanalyse.waarde

    @risicoanalyse.setter
    def risicoanalyse(self, value):
        self._risicoanalyse.set_waarde(value, owner=self)

    @property
    def tabelUitwendigeInvloeden(self):
        """Een bestandsbijlage met de ingevulde en actuele tabel uitwendige invloeden zoals vereist door het AREI voor bepaalde elektrische installaties."""
        return self._tabelUitwendigeInvloeden.waarde

    @tabelUitwendigeInvloeden.setter
    def tabelUitwendigeInvloeden(self, value):
        self._tabelUitwendigeInvloeden.set_waarde(value, owner=self)

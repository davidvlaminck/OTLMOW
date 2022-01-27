# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxhInM import DtcAfmetingBxhInM
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlDeurFabrikant import KlDeurFabrikant
from OTLMOW.OTLModel.Datatypes.KlDeurHandgreeptype import KlDeurHandgreeptype
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInSeconde import KwantWrdInSeconde
from OTLMOW.OTLModel.Datatypes.KwantWrdInUur import KwantWrdInUur


# Generated with OTLClassCreator. To modify: extend, do not edit
class Deur(ABC):
    """Een beweegbaar element ter afsluiting van een ruimte. In een gebouw is een deur meestal bevestigd in een kozijn,dat weer in een muur of wand is aangebracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._afmetingDeuropening = OTLAttribuut(field=DtcAfmetingBxhInM,
                                                 naam='afmetingDeuropening',
                                                 label='afmeting deuropening',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.afmetingDeuropening',
                                                 definition='Afmeting van de vrije ruimte die ontstaat wanneer de deur volledig geopend is.')

        self._brandweerstand = OTLAttribuut(field=KwantWrdInUur,
                                            naam='brandweerstand',
                                            label='brandweerstand',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.brandweerstand',
                                            definition='Brandwerendheid is een maat voor de tijd die een constructie heeft voor dat deze bezwijkt onder invloed van een brand.')

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.breedte',
                                     definition='De afmeting van de rechtopstaande deur gemeten van de ene zijkant naar de andere.')

        self._dikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.dikte',
                                   definition='De dikte van de deur gemeten van de ene buitenzijde van de deur tot de andere.')

        self._fabrikant = OTLAttribuut(field=KlDeurFabrikant,
                                       naam='fabrikant',
                                       label='fabrikant',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.fabrikant',
                                       definition='Naam van de producent van de deur.')

        self._handgreeptype = OTLAttribuut(field=KlDeurHandgreeptype,
                                           naam='handgreeptype',
                                           label='handgreeptype',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.handgreeptype',
                                           definition='Soort greep aan waarmee de deur geopend wordt.')

        self._heeftDeurcontact = OTLAttribuut(field=BooleanField,
                                              naam='heeftDeurcontact',
                                              label='heeft deurcontact',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.heeftDeurcontact',
                                              definition='Geeft aan of de deur voorzien is van een contact dat bewaakt of de deur open of dicht is.')

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.hoogte',
                                    definition='De afmeting van de rechtopstaande deur gemeten van de onderkant tot de bovenkant.')

        self._isZelfsluitend = OTLAttribuut(field=BooleanField,
                                            naam='isZelfsluitend',
                                            label='is zelfsluitend',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.isZelfsluitend',
                                            definition='Geeft aan of de deur voorzien is van een mechanisme dat er voor zorgt dat de deur sluit zonder tussenkomst van een gebruiker.')

        self._ophangconstructie = OTLAttribuut(field=DtcDocument,
                                               naam='ophangconstructie',
                                               label='ophangconstructie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.ophangconstructie',
                                               definition='Documentatie met betrekking tot de manier waarop de deur met het kozijn bevestigd is aan de ruimte waartoe ze toegang biedt.')

        self._sluitingstijd = OTLAttribuut(field=KwantWrdInSeconde,
                                           naam='sluitingstijd',
                                           label='sluitingstijd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Deur.sluitingstijd',
                                           definition='Duurtijd voor het automatische sluiten van een zelfsluitende deur die volledig open staat.')

    @property
    def afmetingDeuropening(self):
        """Afmeting van de vrije ruimte die ontstaat wanneer de deur volledig geopend is."""
        return self._afmetingDeuropening.waarde

    @afmetingDeuropening.setter
    def afmetingDeuropening(self, value):
        self._afmetingDeuropening.set_waarde(value, owner=self)

    @property
    def brandweerstand(self):
        """Brandwerendheid is een maat voor de tijd die een constructie heeft voor dat deze bezwijkt onder invloed van een brand."""
        return self._brandweerstand.waarde

    @brandweerstand.setter
    def brandweerstand(self, value):
        self._brandweerstand.set_waarde(value, owner=self)

    @property
    def breedte(self):
        """De afmeting van de rechtopstaande deur gemeten van de ene zijkant naar de andere."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dikte(self):
        """De dikte van de deur gemeten van de ene buitenzijde van de deur tot de andere."""
        return self._dikte.waarde

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def fabrikant(self):
        """Naam van de producent van de deur."""
        return self._fabrikant.waarde

    @fabrikant.setter
    def fabrikant(self, value):
        self._fabrikant.set_waarde(value, owner=self)

    @property
    def handgreeptype(self):
        """Soort greep aan waarmee de deur geopend wordt."""
        return self._handgreeptype.waarde

    @handgreeptype.setter
    def handgreeptype(self, value):
        self._handgreeptype.set_waarde(value, owner=self)

    @property
    def heeftDeurcontact(self):
        """Geeft aan of de deur voorzien is van een contact dat bewaakt of de deur open of dicht is."""
        return self._heeftDeurcontact.waarde

    @heeftDeurcontact.setter
    def heeftDeurcontact(self, value):
        self._heeftDeurcontact.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De afmeting van de rechtopstaande deur gemeten van de onderkant tot de bovenkant."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def isZelfsluitend(self):
        """Geeft aan of de deur voorzien is van een mechanisme dat er voor zorgt dat de deur sluit zonder tussenkomst van een gebruiker."""
        return self._isZelfsluitend.waarde

    @isZelfsluitend.setter
    def isZelfsluitend(self, value):
        self._isZelfsluitend.set_waarde(value, owner=self)

    @property
    def ophangconstructie(self):
        """Documentatie met betrekking tot de manier waarop de deur met het kozijn bevestigd is aan de ruimte waartoe ze toegang biedt."""
        return self._ophangconstructie.waarde

    @ophangconstructie.setter
    def ophangconstructie(self, value):
        self._ophangconstructie.set_waarde(value, owner=self)

    @property
    def sluitingstijd(self):
        """Duurtijd voor het automatische sluiten van een zelfsluitende deur die volledig open staat."""
        return self._sluitingstijd.waarde

    @sluitingstijd.setter
    def sluitingstijd(self, value):
        self._sluitingstijd.set_waarde(value, owner=self)

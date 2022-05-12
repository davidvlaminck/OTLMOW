# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.SelNietSelLus import SelNietSelLus
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlVriLusFunctie import KlVriLusFunctie
from OTLMOW.OTLModel.Datatypes.KlVriLusSoortvoertuig import KlVriLusSoortvoertuig


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietSelectieveDetectielus(SelNietSelLus):
    """Een niet-selectieve detectielus werkt onder invloed van een wijziging in de zelfinductie van een lus in het wegdek wanneer het metaal van een voertuig binnen het gevoeligheidsgebied van de lus komt. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._functie = OTLAttribuut(field=KlVriLusFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.functie',
                                     definition='Type niet-selectieve detectielus bv. file, afstand, hiaat,...',
                                     owner=self)

        self._isMotorgevoelig = OTLAttribuut(field=BooleanField,
                                             naam='isMotorgevoelig',
                                             label='is motorgevoelig',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.isMotorgevoelig',
                                             definition='Geeft aan of de lus motorgevoelig is of niet.',
                                             owner=self)

        self._isRichtingsgevoelig = OTLAttribuut(field=BooleanField,
                                                 naam='isRichtingsgevoelig',
                                                 label='is richtingsgevoelig',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.isRichtingsgevoelig',
                                                 definition='Is de detectielus gevoelig voor de richting waarin het voertuig het gevoeligheidsgebied van de lus binnenkomt?',
                                                 owner=self)

        self._soortVoertuig = OTLAttribuut(field=KlVriLusSoortvoertuig,
                                           naam='soortVoertuig',
                                           label='soort voertuig',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.soortVoertuig',
                                           kardinaliteit_max='*',
                                           definition='Type voertuig dat de detectielus volgens zijn instellingen kan detecteren.',
                                           owner=self)

    @property
    def functie(self):
        """Type niet-selectieve detectielus bv. file, afstand, hiaat,..."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)

    @property
    def isMotorgevoelig(self):
        """Geeft aan of de lus motorgevoelig is of niet."""
        return self._isMotorgevoelig.get_waarde()

    @isMotorgevoelig.setter
    def isMotorgevoelig(self, value):
        self._isMotorgevoelig.set_waarde(value, owner=self)

    @property
    def isRichtingsgevoelig(self):
        """Is de detectielus gevoelig voor de richting waarin het voertuig het gevoeligheidsgebied van de lus binnenkomt?"""
        return self._isRichtingsgevoelig.get_waarde()

    @isRichtingsgevoelig.setter
    def isRichtingsgevoelig(self, value):
        self._isRichtingsgevoelig.set_waarde(value, owner=self)

    @property
    def soortVoertuig(self):
        """Type voertuig dat de detectielus volgens zijn instellingen kan detecteren."""
        return self._soortVoertuig.get_waarde()

    @soortVoertuig.setter
    def soortVoertuig(self, value):
        self._soortVoertuig.set_waarde(value, owner=self)

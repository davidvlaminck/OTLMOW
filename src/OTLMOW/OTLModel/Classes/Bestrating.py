# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ArtificieleLaag import ArtificieleLaag
from OTLMOW.OTLModel.Datatypes.KlBestratingSteenverband import KlBestratingSteenverband
from OTLMOW.OTLModel.Datatypes.KlBestratingVoegvulling import KlBestratingVoegvulling
from OTLMOW.OTLModel.Datatypes.KlKleurSupp import KlKleurSupp


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bestrating(ArtificieleLaag):
    """Verhardingstype opgebouwd uit bestratingen (rechthoekige of vierkante componenten van beperkte afmetingen) waardoor een aanzienlijk aantal voegen tussen de componenten zitten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.kleur',
                                   definition='De kleur van de bestrating.')

        self._steenverband = OTLAttribuut(field=KlBestratingSteenverband,
                                          naam='steenverband',
                                          label='steenverband',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.steenverband',
                                          definition='Het patroon waarin de bestrating gelegd werd.')

        self._voegvulling = OTLAttribuut(field=KlBestratingVoegvulling,
                                         naam='voegvulling',
                                         label='voegvulling',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.voegvulling',
                                         definition='De gebruikte voegvulling van de bestrating.')

    @property
    def kleur(self):
        """De kleur van de bestrating."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def steenverband(self):
        """Het patroon waarin de bestrating gelegd werd."""
        return self._steenverband.waarde

    @steenverband.setter
    def steenverband(self, value):
        self._steenverband.set_waarde(value, owner=self)

    @property
    def voegvulling(self):
        """De gebruikte voegvulling van de bestrating."""
        return self._voegvulling.waarde

    @voegvulling.setter
    def voegvulling(self, value):
        self._voegvulling.set_waarde(value, owner=self)

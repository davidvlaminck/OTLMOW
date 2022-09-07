# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Luchtkwaliteittoestel import Luchtkwaliteittoestel
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlAlgIngressProtectionCode import KlAlgIngressProtectionCode


# Generated with OTLClassCreator. To modify: extend, do not edit
class LuchtkwaliteitZenderOntvanger(Luchtkwaliteittoestel):
    """Onderdeel van de luchtkwaliteitsensor dat het signaal uitstuurt en ontvangt op basis waarvan de luchtkwaliteit gemeten wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Luchtkwaliteitsensor')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitControleUnit')

        self._ipKlasse = OTLAttribuut(field=KlAlgIngressProtectionCode,
                                      naam='ipKlasse',
                                      label='ingress protection klasse',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.ipKlasse',
                                      definition='De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529.',
                                      owner=self)

        self._isBeschermd = OTLAttribuut(field=BooleanField,
                                         naam='isBeschermd',
                                         label='is beschermd',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.isBeschermd',
                                         definition='Geeft aan of het toestel beschermd wordt tegen aanrijdingen of niet.',
                                         owner=self)

        self._meetCO = OTLAttribuut(field=BooleanField,
                                    naam='meetCO',
                                    label='meet CO',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.meetCO',
                                    definition='Geeft aan of het meettoestel CO in de lucht meet of niet.',
                                    owner=self)

        self._meetNoX = OTLAttribuut(field=BooleanField,
                                     naam='meetNoX',
                                     label='meet NOx',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.meetNoX',
                                     definition='Geeft aan of het meettoestel NOx in de lucht meet of niet.',
                                     owner=self)

        self._meetTemperatuur = OTLAttribuut(field=BooleanField,
                                             naam='meetTemperatuur',
                                             label='meet temperatuur',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.meetTemperatuur',
                                             definition='Geeft aan of het meettoestel de omgevingstemperatuur meet of niet.',
                                             owner=self)

        self._meetZicht = OTLAttribuut(field=BooleanField,
                                       naam='meetZicht',
                                       label='meet zicht',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LuchtkwaliteitZenderOntvanger.meetZicht',
                                       definition='Geeft aan of het meettoestel zichtbaarheid meet of niet.',
                                       owner=self)

    @property
    def ipKlasse(self):
        """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in "vijandige omgevingen" en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""
        return self._ipKlasse.get_waarde()

    @ipKlasse.setter
    def ipKlasse(self, value):
        self._ipKlasse.set_waarde(value, owner=self)

    @property
    def isBeschermd(self):
        """Geeft aan of het toestel beschermd wordt tegen aanrijdingen of niet."""
        return self._isBeschermd.get_waarde()

    @isBeschermd.setter
    def isBeschermd(self, value):
        self._isBeschermd.set_waarde(value, owner=self)

    @property
    def meetCO(self):
        """Geeft aan of het meettoestel CO in de lucht meet of niet."""
        return self._meetCO.get_waarde()

    @meetCO.setter
    def meetCO(self, value):
        self._meetCO.set_waarde(value, owner=self)

    @property
    def meetNoX(self):
        """Geeft aan of het meettoestel NOx in de lucht meet of niet."""
        return self._meetNoX.get_waarde()

    @meetNoX.setter
    def meetNoX(self, value):
        self._meetNoX.set_waarde(value, owner=self)

    @property
    def meetTemperatuur(self):
        """Geeft aan of het meettoestel de omgevingstemperatuur meet of niet."""
        return self._meetTemperatuur.get_waarde()

    @meetTemperatuur.setter
    def meetTemperatuur(self, value):
        self._meetTemperatuur.set_waarde(value, owner=self)

    @property
    def meetZicht(self):
        """Geeft aan of het meettoestel zichtbaarheid meet of niet."""
        return self._meetZicht.get_waarde()

    @meetZicht.setter
    def meetZicht(self, value):
        self._meetZicht.set_waarde(value, owner=self)

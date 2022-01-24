# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Luchtkwaliteittoestel import Luchtkwaliteittoestel
from OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luchtkwaliteitreflector(Luchtkwaliteittoestel):
    """Onderdeel van de luchtkwaliteitsensor dat het signaal uitgestuurd door de LuchtkwaliteitZenderOntvanger reflecteert om de luchtkwaliteit tussen beiden onderdelen te kunnen meten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luchtkwaliteitreflector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._isBeschermd = OTLAttribuut(field=BooleanField,
                                         naam='isBeschermd',
                                         label='is beschermd',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luchtkwaliteitreflector.isBeschermd',
                                         definition='Geeft aan of de sensor beschermd is tegen beschadiging, bv. door een aanrijding.')

    @property
    def isBeschermd(self):
        """Geeft aan of de sensor beschermd is tegen beschadiging, bv. door een aanrijding."""
        return self._isBeschermd.waarde

    @isBeschermd.setter
    def isBeschermd(self, value):
        self._isBeschermd.set_waarde(value, owner=self)

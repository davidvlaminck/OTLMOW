# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.ZenderOntvangerToegang import ZenderOntvangerToegang
from OTLMOW.OTLModel.Datatypes.DteTekstblok import DteTekstblok
from OTLMOW.OTLModel.Datatypes.KlRepeaterMerk import KlRepeaterMerk
from OTLMOW.OTLModel.Datatypes.KlRepeaterModelnaam import KlRepeaterModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Repeater(ZenderOntvangerToegang):
    """Apparatuur die het ontvangen signaal versterkt doorgeeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Repeater'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlRepeaterMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Repeater.merk',
                                  definition='Het merk van de repeater.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlRepeaterModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Repeater.modelnaam',
                                       definition='De modelnaam/product range van een repeater.',
                                       owner=self)

        self._toepassing = OTLAttribuut(field=DteTekstblok,
                                        naam='toepassing',
                                        label='toepassing',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Repeater.toepassing',
                                        definition='De techniek of standaard waarmee signalen over het netwerk verstuurd worden. Mogelijke waarden zijn onder andere: KAR,  wifi, GPRS of GSM..',
                                        owner=self)

    @property
    def merk(self):
        """Het merk van de repeater."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van een repeater."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def toepassing(self):
        """De techniek of standaard waarmee signalen over het netwerk verstuurd worden. Mogelijke waarden zijn onder andere: KAR,  wifi, GPRS of GSM.."""
        return self._toepassing.get_waarde()

    @toepassing.setter
    def toepassing(self, value):
        self._toepassing.set_waarde(value, owner=self)

# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Put import Put
from OTLModel.Classes.PutRelatie import PutRelatie
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlHuisaansluitputMateriaal import KlHuisaansluitputMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Huisaansluitput(Put, PutRelatie):
    """Het constructieonderdeel (putje of T-stuk) dat de verbinding vormt tussen de private riolering en de 
 huisaansluiting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)

        self._aansluitingsfiche = OTLAttribuut(field=DtcDocument,
                                               naam='aansluitingsfiche',
                                               label='aansluitingsfiche',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.aansluitingsfiche',
                                               definition='De aansluitingsfiche van de huisaansluitput.')

        self._heeftStankafsluiter = OTLAttribuut(field=BooleanField,
                                                 naam='heeftStankafsluiter',
                                                 label='heeft stankafsluiter',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.heeftStankafsluiter',
                                                 definition='Aanduiding of een huisaansluitput een stankafsluiter heeft of niet.')

        self._isInfiltrerend = OTLAttribuut(field=BooleanField,
                                            naam='isInfiltrerend',
                                            label='is infiltrerend',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.isInfiltrerend',
                                            definition='Wanneer de wanden van het putje poreus zijn (en het putje dus infiltrerend is), kan een deel van het water het water dat in het putje komt rechtstreeks in de grond infiltreren.')

        self._materiaal = OTLAttribuut(field=KlHuisaansluitputMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.materiaal',
                                       definition='Bepaalt het materiaal waaruit de huisaansluitput is vervaardigd.')

    @property
    def aansluitingsfiche(self):
        """De aansluitingsfiche van de huisaansluitput."""
        return self._aansluitingsfiche.waarde

    @aansluitingsfiche.setter
    def aansluitingsfiche(self, value):
        self._aansluitingsfiche.set_waarde(value, owner=self)

    @property
    def heeftStankafsluiter(self):
        """Aanduiding of een huisaansluitput een stankafsluiter heeft of niet."""
        return self._heeftStankafsluiter.waarde

    @heeftStankafsluiter.setter
    def heeftStankafsluiter(self, value):
        self._heeftStankafsluiter.set_waarde(value, owner=self)

    @property
    def isInfiltrerend(self):
        """Wanneer de wanden van het putje poreus zijn (en het putje dus infiltrerend is), kan een deel van het water het water dat in het putje komt rechtstreeks in de grond infiltreren."""
        return self._isInfiltrerend.waarde

    @isInfiltrerend.setter
    def isInfiltrerend(self, value):
        self._isInfiltrerend.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Bepaalt het materiaal waaruit de huisaansluitput is vervaardigd."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

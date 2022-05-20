# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Put import Put
from OTLMOW.OTLModel.Classes.PutRelatie import PutRelatie
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLMOW.OTLModel.Datatypes.KlPutRooster import KlPutRooster
from OTLMOW.OTLModel.Datatypes.KlRoosterIndeling import KlRoosterIndeling
from OTLMOW.OTLModel.Datatypes.KlRoosterOpeningswijze import KlRoosterOpeningswijze
from OTLMOW.OTLModel.Datatypes.KlStraatkolkBakType import KlStraatkolkBakType
from OTLMOW.OTLModel.Datatypes.KlStraatkolkType import KlStraatkolkType
from OTLMOW.OTLModel.Datatypes.KlStraatkolkTypeUitlaat import KlStraatkolkTypeUitlaat
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Straatkolk(Put, PutRelatie, PuntGeometrie):
    """De hemelwaterinlaatconstructie,meestal geplaatst in de straatgoot of watergreppel,waarlangs het hemelwater van de verhardingen wordt afgevoerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)
        PuntGeometrie.__init__(self)

        self._bakAfmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                           naam='bakAfmetingen',
                                           label='bak afmetingen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.bakAfmetingen',
                                           definition='De afmetingen van de bak van de straatkolk in mm.',
                                           owner=self)

        self._bakType = OTLAttribuut(field=KlStraatkolkBakType,
                                     naam='bakType',
                                     label='baktype',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.bakType',
                                     definition='Het type van bak van de straatkolk.',
                                     owner=self)

        self._heeftAfdekplaatReukafsluiter = OTLAttribuut(field=BooleanField,
                                                          naam='heeftAfdekplaatReukafsluiter',
                                                          label='heeft afdekplaat reukafsluiter',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.heeftAfdekplaatReukafsluiter',
                                                          definition='Dit attribuut geeft aan of de straatkolk een afdekplaat als reukafsluiter heeft.',
                                                          owner=self)

        self._isInfiltrerend = OTLAttribuut(field=BooleanField,
                                            naam='isInfiltrerend',
                                            label='is infiltrerend',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.isInfiltrerend',
                                            definition='Wanneer de wanden van de straatkolk poreus zijn (en de straatkolk dus infiltrerend is), kan een deel van het water het water dat in de straatkolk komt rechtstreeks in de grond infiltreren.',
                                            owner=self)

        self._rooster = OTLAttribuut(field=KlPutRooster,
                                     naam='rooster',
                                     label='rooster',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.rooster',
                                     usagenote='Attribuut uit gebruik sinds versie 2.1.0 ',
                                     deprecated_version='2.1.0',
                                     definition='Bepaalt het gebruikte type van rooster.',
                                     owner=self)

        self._roosterIndeling = OTLAttribuut(field=KlRoosterIndeling,
                                             naam='roosterIndeling',
                                             label='rooster indeling',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.roosterIndeling',
                                             definition='Dit attribuut geeft aan hoe het rooster ingedeeld is: met zijdelingse opvang of dat er sprake is van een 1-delig of 2-delig rooster.',
                                             owner=self)

        self._roosterOpeningswijze = OTLAttribuut(field=KlRoosterOpeningswijze,
                                                  naam='roosterOpeningswijze',
                                                  label='rooster openingswijze',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.roosterOpeningswijze',
                                                  definition='Dit attribuut geeft de manier aan hoe het rooster geopend kan worden.',
                                                  owner=self)

        self._type = OTLAttribuut(field=KlStraatkolkType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.type',
                                  definition='Het type van de straatkolk.',
                                  owner=self)

        self._typeUitlaat = OTLAttribuut(field=KlStraatkolkTypeUitlaat,
                                         naam='typeUitlaat',
                                         label='type uitlaat ',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.typeUitlaat',
                                         definition='Het type van uitlaat van de straatkolk.',
                                         owner=self)

    @property
    def bakAfmetingen(self):
        """De afmetingen van de bak van de straatkolk in mm."""
        return self._bakAfmetingen.get_waarde()

    @bakAfmetingen.setter
    def bakAfmetingen(self, value):
        self._bakAfmetingen.set_waarde(value, owner=self)

    @property
    def bakType(self):
        """Het type van bak van de straatkolk."""
        return self._bakType.get_waarde()

    @bakType.setter
    def bakType(self, value):
        self._bakType.set_waarde(value, owner=self)

    @property
    def heeftAfdekplaatReukafsluiter(self):
        """Dit attribuut geeft aan of de straatkolk een afdekplaat als reukafsluiter heeft."""
        return self._heeftAfdekplaatReukafsluiter.get_waarde()

    @heeftAfdekplaatReukafsluiter.setter
    def heeftAfdekplaatReukafsluiter(self, value):
        self._heeftAfdekplaatReukafsluiter.set_waarde(value, owner=self)

    @property
    def isInfiltrerend(self):
        """Wanneer de wanden van de straatkolk poreus zijn (en de straatkolk dus infiltrerend is), kan een deel van het water het water dat in de straatkolk komt rechtstreeks in de grond infiltreren."""
        return self._isInfiltrerend.get_waarde()

    @isInfiltrerend.setter
    def isInfiltrerend(self, value):
        self._isInfiltrerend.set_waarde(value, owner=self)

    @property
    def rooster(self):
        """Bepaalt het gebruikte type van rooster."""
        return self._rooster.get_waarde()

    @rooster.setter
    def rooster(self, value):
        self._rooster.set_waarde(value, owner=self)

    @property
    def roosterIndeling(self):
        """Dit attribuut geeft aan hoe het rooster ingedeeld is: met zijdelingse opvang of dat er sprake is van een 1-delig of 2-delig rooster."""
        return self._roosterIndeling.get_waarde()

    @roosterIndeling.setter
    def roosterIndeling(self, value):
        self._roosterIndeling.set_waarde(value, owner=self)

    @property
    def roosterOpeningswijze(self):
        """Dit attribuut geeft de manier aan hoe het rooster geopend kan worden."""
        return self._roosterOpeningswijze.get_waarde()

    @roosterOpeningswijze.setter
    def roosterOpeningswijze(self, value):
        self._roosterOpeningswijze.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de straatkolk."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def typeUitlaat(self):
        """Het type van uitlaat van de straatkolk."""
        return self._typeUitlaat.get_waarde()

    @typeUitlaat.setter
    def typeUitlaat(self, value):
        self._typeUitlaat.set_waarde(value, owner=self)

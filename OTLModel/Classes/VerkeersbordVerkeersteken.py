# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Verkeersteken import Verkeersteken
from OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeersbordVerkeersteken(Verkeersteken):
    """De voorstelling door middel van een verkeersbord van een aanwijzing ten behoeve van de weggebruikers die verbonden wordt aan het aankondigen of opleggen van een bepaalde verkeersmaatregel zoals bepaald in de wegcode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordVerkeersteken'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._isBeginZone = OTLAttribuut(field=BooleanField,
                                         naam='isBeginZone',
                                         label='is begin van een zone',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordVerkeersteken.isBeginZone',
                                         definition='Duidt aan of het verkeersteken het begin van een zone aanduidt.')

        self._isEindeZone = OTLAttribuut(field=BooleanField,
                                         naam='isEindeZone',
                                         label='is einde van een zone',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerkeersbordVerkeersteken.isEindeZone',
                                         definition='Duidt aan of het verkeersteken het einde van een zone aanduidt.')

    @property
    def isBeginZone(self):
        """Duidt aan of het verkeersteken het begin van een zone aanduidt."""
        return self._isBeginZone.waarde

    @isBeginZone.setter
    def isBeginZone(self, value):
        self._isBeginZone.set_waarde(value, owner=self)

    @property
    def isEindeZone(self):
        """Duidt aan of het verkeersteken het einde van een zone aanduidt."""
        return self._isEindeZone.waarde

    @isEindeZone.setter
    def isEindeZone(self, value):
        self._isEindeZone.set_waarde(value, owner=self)

# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KlRioleringStelsel import KlRioleringStelsel


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rioleringsstelsel(AIMObject, AttributeInfo):
    """De groepering van de objecten die behoren tot de riolering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._rioleringsstelsel = OTLAttribuut(field=KlRioleringStelsel,
                                               naam='rioleringsstelsel',
                                               label='rioleringsstelsel',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel.rioleringsstelsel',
                                               usagenote='Attribuut uit gebruik sinds versie 2.1.0',
                                               deprecated_version='2.1.0',
                                               definition='Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt.')

        self._systeemtype = OTLAttribuut(field=KlRioleringStelsel,
                                         naam='systeemtype',
                                         label='systeemtype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel.systeemtype',
                                         definition='Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt.')

    @property
    def rioleringsstelsel(self):
        """Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt."""
        return self._rioleringsstelsel.waarde

    @rioleringsstelsel.setter
    def rioleringsstelsel(self, value):
        self._rioleringsstelsel.set_waarde(value, owner=self)

    @property
    def systeemtype(self):
        """Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt."""
        return self._systeemtype.waarde

    @systeemtype.setter
    def systeemtype(self, value):
        self._systeemtype.set_waarde(value, owner=self)

# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AndereLaag import AndereLaag
from src.OTLMOW.OTLModel.Datatypes.KlKleurSupp import KlKleurSupp
from src.OTLMOW.OTLModel.Datatypes.KlSlemProductfamilie import KlSlemProductfamilie
from src.OTLMOW.OTLModel.Datatypes.KlSlemlaagsoort import KlSlemlaagsoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slemlaag(AndereLaag):
    """Een slemlaag (slem) is een oppervlaktebehandeling die bestaat uit een mengsel dat ter plaatse bereid en verwerkt wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag.kleur',
                                   definition='De kleur van de slemlaag.')

        self._productfamilie = OTLAttribuut(field=KlSlemProductfamilie,
                                            naam='productfamilie',
                                            label='productfamilie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag.productfamilie',
                                            definition='Bepaling tot welke productfamilie de slemlaag behoort. ')

        self._soort = OTLAttribuut(field=KlSlemlaagsoort,
                                   naam='soort',
                                   label='soort',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag.soort',
                                   definition='De soort slemlaag.')

    @property
    def kleur(self):
        """De kleur van de slemlaag."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def productfamilie(self):
        """Bepaling tot welke productfamilie de slemlaag behoort. """
        return self._productfamilie.waarde

    @productfamilie.setter
    def productfamilie(self, value):
        self._productfamilie.set_waarde(value, owner=self)

    @property
    def soort(self):
        """De soort slemlaag."""
        return self._soort.waarde

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)

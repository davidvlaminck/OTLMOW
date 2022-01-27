# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AndereLaag import AndereLaag
from src.OTLMOW.OTLModel.Datatypes.KlBestrijkingKaliber import KlBestrijkingKaliber
from src.OTLMOW.OTLModel.Datatypes.KlBestrijkingProductfamilie import KlBestrijkingProductfamilie
from src.OTLMOW.OTLModel.Datatypes.KlBestrijkingsoort import KlBestrijkingsoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bestrijking(AndereLaag):
    """Een bestrijking bestaat in het sproeien op een verharding of een fundering van één of twee eenvormige lagen bindmiddel met een geschikte viscositeit."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._kaliber = OTLAttribuut(field=KlBestrijkingKaliber,
                                     naam='kaliber',
                                     label='kaliber',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking.kaliber',
                                     definition='De korrelmaat gebruikt bij de bestrijking.')

        self._productfamilie = OTLAttribuut(field=KlBestrijkingProductfamilie,
                                            naam='productfamilie',
                                            label='productfamilie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking.productfamilie',
                                            definition='Bepaling tot welke productfamilie de bestrijking behoort. ')

        self._soort = OTLAttribuut(field=KlBestrijkingsoort,
                                   naam='soort',
                                   label='soort',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking.soort',
                                   definition='De soort bestrijking.')

    @property
    def kaliber(self):
        """De korrelmaat gebruikt bij de bestrijking."""
        return self._kaliber.waarde

    @kaliber.setter
    def kaliber(self, value):
        self._kaliber.set_waarde(value, owner=self)

    @property
    def productfamilie(self):
        """Bepaling tot welke productfamilie de bestrijking behoort. """
        return self._productfamilie.waarde

    @productfamilie.setter
    def productfamilie(self, value):
        self._productfamilie.set_waarde(value, owner=self)

    @property
    def soort(self):
        """De soort bestrijking."""
        return self._soort.waarde

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)

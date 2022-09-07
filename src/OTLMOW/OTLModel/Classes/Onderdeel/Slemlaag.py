# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AndereLaag import AndereLaag
from OTLMOW.OTLModel.Datatypes.KlKleurSupp import KlKleurSupp
from OTLMOW.OTLModel.Datatypes.KlSlemProductfamilie import KlSlemProductfamilie
from OTLMOW.OTLModel.Datatypes.KlSlemlaagsoort import KlSlemlaagsoort
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slemlaag(AndereLaag, VlakGeometrie):
    """Een slemlaag (slem) is een oppervlaktebehandeling die bestaat uit een mengsel dat ter plaatse bereid en verwerkt wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag.kleur',
                                   definition='De kleur van de slemlaag.',
                                   owner=self)

        self._productfamilie = OTLAttribuut(field=KlSlemProductfamilie,
                                            naam='productfamilie',
                                            label='productfamilie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag.productfamilie',
                                            definition='Bepaling tot welke productfamilie de slemlaag behoort. ',
                                            owner=self)

        self._soort = OTLAttribuut(field=KlSlemlaagsoort,
                                   naam='soort',
                                   label='soort',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag.soort',
                                   definition='De soort slemlaag.',
                                   owner=self)

    @property
    def kleur(self):
        """De kleur van de slemlaag."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def productfamilie(self):
        """Bepaling tot welke productfamilie de slemlaag behoort. """
        return self._productfamilie.get_waarde()

    @productfamilie.setter
    def productfamilie(self, value):
        self._productfamilie.set_waarde(value, owner=self)

    @property
    def soort(self):
        """De soort slemlaag."""
        return self._soort.get_waarde()

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)

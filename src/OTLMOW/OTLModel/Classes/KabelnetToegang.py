# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.KlKabelnettoegangNetwerksoort import KlKabelnettoegangNetwerksoort
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KabelnetToegang(AIMNaamObject, PuntGeometrie):
    """Knooppunt van Kabelnet dat toegang geeft tot de informatie die in Kabelnet bewaard wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._kabelnetToegangId = OTLAttribuut(field=IntegerField,
                                               naam='kabelnetToegangId',
                                               label='kabelnettoegang ID',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang.kabelnetToegangId',
                                               definition='Uniek nummer uit de Kabelnet toepassing dat deze toegang identificeert.',
                                               owner=self)

        self._netwerkSoort = OTLAttribuut(field=KlKabelnettoegangNetwerksoort,
                                          naam='netwerkSoort',
                                          label='netwerk soort',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang.netwerkSoort',
                                          kardinaliteit_max='*',
                                          definition='Type netwerk dat bereikbaar is via het toegangspunt.',
                                          owner=self)

    @property
    def kabelnetToegangId(self):
        """Uniek nummer uit de Kabelnet toepassing dat deze toegang identificeert."""
        return self._kabelnetToegangId.get_waarde()

    @kabelnetToegangId.setter
    def kabelnetToegangId(self, value):
        self._kabelnetToegangId.set_waarde(value, owner=self)

    @property
    def netwerkSoort(self):
        """Type netwerk dat bereikbaar is via het toegangspunt."""
        return self._netwerkSoort.get_waarde()

    @netwerkSoort.setter
    def netwerkSoort(self, value):
        self._netwerkSoort.set_waarde(value, owner=self)

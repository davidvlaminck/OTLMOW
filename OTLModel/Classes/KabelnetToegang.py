# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlKabelnettoegangNetwerksoort import KlKabelnettoegangNetwerksoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class KabelnetToegang(AIMNaamObject):
    """Knooppunt van Kabelnet dat toegang geeft tot de informatie die in Kabelnet bewaard wordt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.kabelnetToegangId = IntegerField(naam="kabelnetToegangId",
                                              label="kabelnettoegang ID",
                                              objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang.kabelnetToegangId",
                                              definition="Uniek nummer uit de Kabelnet toepassing dat deze toegang identificeert.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Uniek nummer uit de Kabelnet toepassing dat deze toegang identificeert."""

        netwerkSoortField = KeuzelijstField(naam="netwerkSoort",
                                            label="netwerk soort",
                                            lijst=KlKabelnettoegangNetwerksoort(),
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang.netwerkSoort",
                                            definition="Type netwerk dat bereikbaar is via het toegangspunt.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        self.netwerkSoort = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=netwerkSoortField)
        """Type netwerk dat bereikbaar is via het toegangspunt."""

from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Verkeersbord import Verkeersbord
from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRetroreflecterendVerkeersbordAfwerkingsgraad import KlRetroreflecterendVerkeersbordAfwerkingsgraad
from OTLModel.Datatypes.KlRetroreflecterendVerkeersbordGrootteorde import KlRetroreflecterendVerkeersbordGrootteorde
from OTLModel.Datatypes.KlRetroreflecterendVerkeersbordMerk import KlRetroreflecterendVerkeersbordMerk
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroreflecterendVerkeersbord(AIMObject, Verkeersbord):
    """Verkeersbord met op het beeldvlak een tekening en/of tekst die worden weergegeven met een geëigend bekledingsmateriaal."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Verkeersbord.__init__(self)

        self.afwerkingsgraad = KeuzelijstField(naam="afwerkingsgraad",
                                               label="afwerkingsgraad",
                                               lijst=KlRetroreflecterendVerkeersbordAfwerkingsgraad(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.afwerkingsgraad",
                                               definition="De afwerkingsgraad van het retroreflecterend verkeersbord, volgens een keuzelijst op basis van SB250.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """De afwerkingsgraad van het retroreflecterend verkeersbord, volgens een keuzelijst op basis van SB250."""

        self.grootteorde = KeuzelijstField(naam="grootteorde",
                                           label="grootteorde",
                                           lijst=KlRetroreflecterendVerkeersbordGrootteorde(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.grootteorde",
                                           definition="De classificatie naar grootteorde van het verkeersbord, zoals gedefinieerd in SB250 hoofdstuk 10.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """De classificatie naar grootteorde van het verkeersbord, zoals gedefinieerd in SB250 hoofdstuk 10."""

        self.kleurAchterkant = DteKleurRAL()
        """De kleur van de achterkant van het retroreflecterend verkeersbord."""
        self.kleurAchterkant.naam = "kleurAchterkant"
        self.kleurAchterkant.label = "kleur achterkant"
        self.kleurAchterkant.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.kleurAchterkant"
        self.kleurAchterkant.definition = "De kleur van de achterkant van het retroreflecterend verkeersbord."
        self.kleurAchterkant.constraints = ""
        self.kleurAchterkant.usagenote = ""
        self.kleurAchterkant.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlRetroreflecterendVerkeersbordMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.merk",
                                    definition="De merknaam van het verkeersbord; duidt op de leverancier of producent van het verkeersbord.",
                                    constraints="",
                                    usagenote="Te selecteren uit een keuzelijst.",
                                    deprecated_version="")
        """De merknaam van het verkeersbord; duidt op de leverancier of producent van het verkeersbord."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van het beeldvlak van een verkeersbord."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van het beeldvlak van een verkeersbord."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

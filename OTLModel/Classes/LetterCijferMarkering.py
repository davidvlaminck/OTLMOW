from OTLModel.Classes.FiguratieMarkeringToegang import FiguratieMarkeringToegang
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLetterCijfer import KlLetterCijfer
from OTLModel.Datatypes.KlLetterCijferType import KlLetterCijferType
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class LetterCijferMarkering(FiguratieMarkeringToegang):
    """Een markering bestaande uit individuele letters en/of cijfers."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.letterCijfer = KeuzelijstField(naam="letterCijfer",
                                            label="letter-cijfer",
                                            lijst=KlLetterCijfer(),
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering.letterCijfer",
                                            definition="De individuele letter of cijfer gebruikt bij de wegmarkering.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """De individuele letter of cijfer gebruikt bij de wegmarkering."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van de individuele letter- of cijfermarkering zoals beschreven in de algemene omzendbrief."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "basisoppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van de individuele letter- of cijfermarkering zoals beschreven in de algemene omzendbrief."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlLetterCijferType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LetterCijferMarkering.type",
                                    definition="Het type van de individuele letter- of cijfermarkering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de individuele letter- of cijfermarkering."""

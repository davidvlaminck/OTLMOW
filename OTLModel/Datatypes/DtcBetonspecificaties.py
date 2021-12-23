from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBetonmilieuklasse import KlBetonmilieuklasse
from OTLModel.Datatypes.KlBetonomgevingsklasse import KlBetonomgevingsklasse
from OTLModel.Datatypes.KlBetonsterkteklasse import KlBetonsterkteklasse
from OTLModel.Datatypes.KlGebruiksdomein import KlGebruiksdomein
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator
class DtcBetonspecificaties(ComplexField):
    """Complex datatype om de eigenschappen van beton te bundelen."""

    def __init__(self):
        super().__init__(naam="DtcBetonspecificaties",
                         label="Betonspecificaties",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties",
                         definition="Complex datatype om de eigenschappen van beton te bundelen.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.betondekking = KwantWrdInMillimeter()
        """De afstand in millimeter tussen de buitenkant van het beton (het oppervlak van het beton) tot het dichtstbijzijnde wapeningsstaal."""
        self.waarde.betondekking.naam = "betondekking"
        self.waarde.betondekking.label = "betondekking"
        self.waarde.betondekking.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betondekking"
        self.waarde.betondekking.definition = "De afstand in millimeter tussen de buitenkant van het beton (het oppervlak van het beton) tot het dichtstbijzijnde wapeningsstaal."
        self.waarde.betondekking.constraints = ""
        self.waarde.betondekking.usagenote = ""
        self.waarde.betondekking.deprecated_version = ""
        self.betondekking = self.waarde.betondekking

        betonmilieuklassenField = KeuzelijstField(naam="betonmilieuklassen",
                                                  label="betonmilieuklassen",
                                                  lijst=KlBetonmilieuklasse(),
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonmilieuklassen",
                                                  definition="Milieuklassen (X-klassen) leggen rechtstreeks de link met bepaalde aantastingsmechanismen, waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere milieuklassen van toepassing zijn.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        self.waarde.betonmilieuklassen = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=betonmilieuklassenField)
        self.betonmilieuklassen = self.waarde.betonmilieuklassen
        """Milieuklassen (X-klassen) leggen rechtstreeks de link met bepaalde aantastingsmechanismen, waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere milieuklassen van toepassing zijn."""

        betonomgevingsklassenField = KeuzelijstField(naam="betonomgevingsklassen",
                                                     label="betonomgevingsklassen",
                                                     lijst=KlBetonomgevingsklasse(),
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonomgevingsklassen",
                                                     definition="De omgeving waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere omgevingsklassen van toepassing zijn.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        self.waarde.betonomgevingsklassen = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=betonomgevingsklassenField)
        self.betonomgevingsklassen = self.waarde.betonomgevingsklassen
        """De omgeving waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere omgevingsklassen van toepassing zijn."""

        self.waarde.betonsterkteklasse = KeuzelijstField(naam="betonsterkteklasse",
                                                         label="betonsterkteklasse",
                                                         lijst=KlBetonsterkteklasse(),
                                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonsterkteklasse",
                                                         definition="De sterkteklasse is een maat voor de druksterkte van beton.",
                                                         constraints="",
                                                         usagenote="",
                                                         deprecated_version="")
        self.betonsterkteklasse = self.waarde.betonsterkteklasse
        """De sterkteklasse is een maat voor de druksterkte van beton."""

        self.waarde.gebruiksdomein = KeuzelijstField(naam="gebruiksdomein",
                                                     label="gebruiksdomein",
                                                     lijst=KlGebruiksdomein(),
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.gebruiksdomein",
                                                     definition="De gebruiksomstandigheden van het beton. Dit bepaalt tevens het maximum chloridegehalte.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        self.gebruiksdomein = self.waarde.gebruiksdomein
        """De gebruiksomstandigheden van het beton. Dit bepaalt tevens het maximum chloridegehalte."""

        self.waarde.grootsteKorrelafmetingDmax = KwantWrdInMillimeter()
        """De nominale grootste korrelafmeting (Dmax)."""
        self.waarde.grootsteKorrelafmetingDmax.naam = "grootsteKorrelafmetingDmax"
        self.waarde.grootsteKorrelafmetingDmax.label = "grootste korrelafmeting (Dmax)"
        self.waarde.grootsteKorrelafmetingDmax.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.grootsteKorrelafmetingDmax"
        self.waarde.grootsteKorrelafmetingDmax.definition = "De nominale grootste korrelafmeting (Dmax)."
        self.waarde.grootsteKorrelafmetingDmax.constraints = ""
        self.waarde.grootsteKorrelafmetingDmax.usagenote = ""
        self.waarde.grootsteKorrelafmetingDmax.deprecated_version = ""
        self.grootsteKorrelafmetingDmax = self.waarde.grootsteKorrelafmetingDmax

        self.waarde.isCementMetBeperktAlkaligehalte = BooleanField(naam="isCementMetBeperktAlkaligehalte",
                                                                   label="is cement met beperkt alkaligehalte",
                                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetBeperktAlkaligehalte",
                                                                   definition="Aanduiding of het cement een beperkt alkaligehalte heeft (LA).",
                                                                   constraints="",
                                                                   usagenote="",
                                                                   deprecated_version="")
        self.isCementMetBeperktAlkaligehalte = self.waarde.isCementMetBeperktAlkaligehalte
        """Aanduiding of het cement een beperkt alkaligehalte heeft (LA)."""

        self.waarde.isCementMetHogeAanvangssterkte = BooleanField(naam="isCementMetHogeAanvangssterkte",
                                                                  label="is cement met hoge aanvangssterkte",
                                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetHogeAanvangssterkte",
                                                                  definition="Geeft aan of het cement gebruikt wordt voor een snelle binding (bijvoorbeeld in de winter) (HES).",
                                                                  constraints="",
                                                                  usagenote="",
                                                                  deprecated_version="")
        self.isCementMetHogeAanvangssterkte = self.waarde.isCementMetHogeAanvangssterkte
        """Geeft aan of het cement gebruikt wordt voor een snelle binding (bijvoorbeeld in de winter) (HES)."""

        self.waarde.isCementMetHogeBestandheidTegenSulfaten = BooleanField(naam="isCementMetHogeBestandheidTegenSulfaten",
                                                                           label="is cement met hoge bestandheid tegen sulfaten",
                                                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetHogeBestandheidTegenSulfaten",
                                                                           definition="Geeft aan of het cement een hoge bestandheid heeft tegen sulfaten (SR).",
                                                                           constraints="",
                                                                           usagenote="",
                                                                           deprecated_version="")
        self.isCementMetHogeBestandheidTegenSulfaten = self.waarde.isCementMetHogeBestandheidTegenSulfaten
        """Geeft aan of het cement een hoge bestandheid heeft tegen sulfaten (SR)."""

        self.waarde.isCementMetLageHydratatiewarmte = BooleanField(naam="isCementMetLageHydratatiewarmte",
                                                                   label="is cement met lage hydratatiewarmte",
                                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetLageHydratatiewarmte",
                                                                   definition="Geeft aan of het cement gebruikt wordt voor een tragere sterkteontwikkeling (LH).",
                                                                   constraints="",
                                                                   usagenote="",
                                                                   deprecated_version="")
        self.isCementMetLageHydratatiewarmte = self.waarde.isCementMetLageHydratatiewarmte
        """Geeft aan of het cement gebruikt wordt voor een tragere sterkteontwikkeling (LH)."""

        self.waarde.isColloidaalbeton = BooleanField(naam="isColloidaalbeton",
                                                     label="is colloïdaalbeton",
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isColloidaalbeton",
                                                     definition="Geeft aan of het beton zich niet ontmengt onder of in water.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        self.isColloidaalbeton = self.waarde.isColloidaalbeton
        """Geeft aan of het beton zich niet ontmengt onder of in water."""

        self.waarde.technischeFiche = DtcDocument()
        """De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,..."""
        self.waarde.technischeFiche.naam = "technischeFiche"
        self.waarde.technischeFiche.label = "technische fiche"
        self.waarde.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.technischeFiche"
        self.waarde.technischeFiche.definition = "De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,..."
        self.waarde.technischeFiche.constraints = ""
        self.waarde.technischeFiche.usagenote = ""
        self.waarde.technischeFiche.deprecated_version = ""
        self.technischeFiche = self.waarde.technischeFiche

from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlMaaiFrequentie import KlMaaiFrequentie
from OTLModel.Datatypes.KlMaaiPeriode import KlMaaiPeriode


# Generated with OTLComplexDatatypeCreator
class DtcMaaien(ComplexField):
    """Complex datatype voor de eigenschappen van maaien."""

    def __init__(self):
        super().__init__(naam="DtcMaaien",
                         label="Maaien",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien",
                         definition="Complex datatype voor de eigenschappen van maaien.",
                         usagenote="",
                         deprecated_version="")

        frequentieField = KeuzelijstField(naam="frequentie",
                                          label="frequentie",
                                          lijst=KlMaaiFrequentie(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.frequentie",
                                          definition="Het aantal keer dat er gemaaid wordt per jaar.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        self.waarde.frequentie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=frequentieField)
        self.frequentie = self.waarde.frequentie
        """Het aantal keer dat er gemaaid wordt per jaar."""

        self.waarde.isGazonbeheer = BooleanField(naam="isGazonbeheer",
                                                 label="is gazonbeheer",
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.isGazonbeheer",
                                                 definition="Aanduiding of de grazige vegetatie meer dan 3x per jaar gemaaid wordt.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        self.isGazonbeheer = self.waarde.isGazonbeheer
        """Aanduiding of de grazige vegetatie meer dan 3x per jaar gemaaid wordt."""

        self.waarde.isMachinaal = BooleanField(naam="isMachinaal",
                                               label="is machinaal",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.isMachinaal",
                                               definition="Aanduiding of het maaien machinaal of handmatig wordt uitgevoerd.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        self.isMachinaal = self.waarde.isMachinaal
        """Aanduiding of het maaien machinaal of handmatig wordt uitgevoerd."""

        self.waarde.isRuigtebeheer = BooleanField(naam="isRuigtebeheer",
                                                  label="is ruigtebeheer",
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.isRuigtebeheer",
                                                  definition="Aanduiding of de grazige vegetatie minder dan 1x per jaar gemaaid wordt.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        self.isRuigtebeheer = self.waarde.isRuigtebeheer
        """Aanduiding of de grazige vegetatie minder dan 1x per jaar gemaaid wordt."""

        self.waarde.isVeiligheidsmaaien = BooleanField(naam="isVeiligheidsmaaien",
                                                       label="is veiligheidsmaaien",
                                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.isVeiligheidsmaaien",
                                                       definition="Aanduiding of er een maaistrook aanwezig is voor het vrijwaren van de zichtbaarheid en voor het vrijhouden van de bebakening en signalisatie.",
                                                       constraints="",
                                                       usagenote="",
                                                       deprecated_version="")
        self.isVeiligheidsmaaien = self.waarde.isVeiligheidsmaaien
        """Aanduiding of er een maaistrook aanwezig is voor het vrijwaren van de zichtbaarheid en voor het vrijhouden van de bebakening en signalisatie."""

        self.waarde.klepelmaaierToegelaten = BooleanField(naam="klepelmaaierToegelaten",
                                                          label="klepelmaaier toegelaten",
                                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.klepelmaaierToegelaten",
                                                          definition="Aanduiding of er gemaaid mag worden met een klepelmaaier.",
                                                          constraints="",
                                                          usagenote="",
                                                          deprecated_version="")
        self.klepelmaaierToegelaten = self.waarde.klepelmaaierToegelaten
        """Aanduiding of er gemaaid mag worden met een klepelmaaier."""

        periodeField = KeuzelijstField(naam="periode",
                                       label="periode",
                                       lijst=KlMaaiPeriode(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.periode",
                                       definition="De maand waarin het maaien wordt uitgevoerd.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        self.waarde.periode = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=periodeField)
        self.periode = self.waarde.periode
        """De maand waarin het maaien wordt uitgevoerd."""

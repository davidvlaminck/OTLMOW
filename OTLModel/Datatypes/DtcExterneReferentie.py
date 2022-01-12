# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcExterneReferentie(ComplexField):
    """Complex datatype waarmee een referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ... kan toegevoegd worden aan object."""

    def __init__(self):
        super().__init__(naam="DtcExterneReferentie",
                         label="Externe referentie",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcExterneReferentie",
                         definition="Complex datatype waarmee een referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ... kan toegevoegd worden aan object.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.externReferentienummer = StringField(naam="externReferentienummer",
                                                         label="extern referentienummer",
                                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcExterneReferentie.externReferentienummer",
                                                         definition="Referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ...",
                                                         constraints="",
                                                         usagenote="",
                                                         deprecated_version="")
        self.externReferentienummer = self.waarde.externReferentienummer
        """Referentienummer zoals gekend bij de externe partij bv. aannemer, VLCC, ..."""

        self.waarde.externePartij = StringField(naam="externePartij",
                                                label="externe partij",
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcExterneReferentie.externePartij",
                                                definition="De naam van de externe partij waarvoor de referentie geldt. Dit kan een organisatie zijn maar ook een softwaretoepassing zoals bv. ABBA of VLCC.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.externePartij = self.waarde.externePartij
        """De naam van de externe partij waarvoor de referentie geldt. Dit kan een organisatie zijn maar ook een softwaretoepassing zoals bv. ABBA of VLCC."""

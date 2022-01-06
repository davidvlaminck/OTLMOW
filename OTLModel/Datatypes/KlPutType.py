# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPutType(Keuzelijst):
    """Types van put."""

    def __init__(self):
        super().__init__(naam="KlPutType",
                         label="Put type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutType",
                         definition="Types van put.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutType")

        self.add_option("doorlooptoegangs--of-verbindingsput-(DTP-of-DVP)", "doorlooptoegangs- of verbindingsput (DTP of DVP)", "Doorlooptoegangs- of verbindingsput (= DTP of DVP)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/doorlooptoegangs--of-verbindingsput-(DTP-of-DVP)")
        self.add_option("begintoegangs--of-verbindingsput-(BIP-of-DVP)", "begintoegangs- of verbindingsput (BIP of DVP)", "Begintoegangs- of verbindingsput (= BIP of DVP)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/begintoegangs--of-verbindingsput-(BIP-of-DVP)")
        self.add_option("putbuis-of-schachttoegangsput-(STP)", "putbuis of schachttoegangsput (STP)", "Putbuis of schachttoegangsput (= STP)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/putbuis-of-schachttoegangsput-(STP)")
        self.add_option("hoektoegangsput-(HTP)", "hoektoegangsput (HTP)", "Hoektoegangsput (= HTP)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/hoektoegangsput-(HTP)")
        self.add_option("aansluitingstoegangsput-(ATP)", "aansluitingstoegangsput (ATP)", "Knijpopening", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/aansluitingstoegangsput-(ATP)")
        self.add_option("vervaltoegangsput-(VTP)", "vervaltoegangsput (VTP)", "Vervaltoegangsput (= VTP)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/vervaltoegangsput-(VTP)")

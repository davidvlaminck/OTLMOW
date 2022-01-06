# coding=utf-8
from OTLModel.Classes.DwarseMarkeringToegang import DwarseMarkeringToegang
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDwarseMarkeringVerschuindCode import KlDwarseMarkeringVerschuindCode
from OTLModel.Datatypes.KlDwarseMarkeringVerschuindSoort import KlDwarseMarkeringVerschuindSoort
from OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class DwarseMarkeringVerschuind(DwarseMarkeringToegang):
    """Een schuine markering dwars op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.basisoppervlakte = KwantWrdInVierkanteMeter()
        """De basisoppervlakte van de dwarse markering in vierkante meter."""
        self.basisoppervlakte.naam = "basisoppervlakte"
        self.basisoppervlakte.label = "oppervlakte"
        self.basisoppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.basisoppervlakte"
        self.basisoppervlakte.definition = "De basisoppervlakte van de dwarse markering in vierkante meter."
        self.basisoppervlakte.constraints = ""
        self.basisoppervlakte.usagenote = ""
        self.basisoppervlakte.deprecated_version = ""

        self.code = KeuzelijstField(naam="code",
                                    label="code",
                                    lijst=KlDwarseMarkeringVerschuindCode(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.code",
                                    definition="De (COPRO/BENOR)  code van dwarse markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De (COPRO/BENOR)  code van dwarse markering."""

        self.hoek = KwantWrdInDecimaleGraden()
        """De hoek van de verschuinde dwarsmarkering in decimale graden."""
        self.hoek.naam = "hoek"
        self.hoek.label = "hoek"
        self.hoek.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.hoek"
        self.hoek.definition = "De hoek van de verschuinde dwarsmarkering in decimale graden."
        self.hoek.constraints = ""
        self.hoek.usagenote = ""
        self.hoek.deprecated_version = ""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van een dwarsmarkering na verschuining."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van een dwarsmarkering na verschuining."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.soortOmschrijving = KeuzelijstField(naam="soortOmschrijving",
                                                 label="soort omschrijving",
                                                 lijst=KlDwarseMarkeringVerschuindSoort(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkeringVerschuind.soortOmschrijving",
                                                 definition="De soort en tevens de omschrijving van dwarse markering.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De soort en tevens de omschrijving van dwarse markering."""

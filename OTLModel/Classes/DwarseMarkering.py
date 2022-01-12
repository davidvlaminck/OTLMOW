# coding=utf-8
from OTLModel.Classes.DwarseMarkeringToegang import DwarseMarkeringToegang
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDwarseMarkeringCode import KlDwarseMarkeringCode
from OTLModel.Datatypes.KlDwarseMarkeringSoort import KlDwarseMarkeringSoort
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class DwarseMarkering(DwarseMarkeringToegang):
    """Een markering dwars op de weg aangebracht om het verkeer te waarschuwen, informeren of regelen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.code = KeuzelijstField(naam="code",
                                    label="code",
                                    lijst=KlDwarseMarkeringCode(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkering.code",
                                    definition="De (COPRO/BENOR)  code van dwarse markering.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De (COPRO/BENOR)  code van dwarse markering."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van de dwarse markering in vierkante meter."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkering.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van de dwarse markering in vierkante meter."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.soortOmschrijving = KeuzelijstField(naam="soortOmschrijving",
                                                 label="soort omschrijving",
                                                 lijst=KlDwarseMarkeringSoort(),
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DwarseMarkering.soortOmschrijving",
                                                 definition="De soort en tevens de omschrijving van dwarse markering.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De soort en tevens de omschrijving van dwarse markering."""

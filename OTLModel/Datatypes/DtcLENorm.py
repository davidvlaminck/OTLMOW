# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEKantopsluitingBijkomendeParameter import KlLEKantopsluitingBijkomendeParameter
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcLENorm(ComplexField):
    """Complex datatype voor de norm van het lijnvormig element."""

    def __init__(self):
        super().__init__(naam="DtcLENorm",
                         label="Norm van het lijnvormig element",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm",
                         definition="Complex datatype voor de norm van het lijnvormig element.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.bijkomendeParameter = KeuzelijstField(naam="bijkomendeParameter",
                                                          label="bijkomende parameter",
                                                          lijst=KlLEKantopsluitingBijkomendeParameter(),
                                                          objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm.bijkomendeParameter",
                                                          definition="Het gedetailleerder typeren van de kantopsluiting.",
                                                          constraints="",
                                                          usagenote="",
                                                          deprecated_version="")
        self.bijkomendeParameter = self.waarde.bijkomendeParameter
        """Het gedetailleerder typeren van de kantopsluiting."""

        self.waarde.norm = StringField(naam="norm",
                                       label="norm",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm.norm",
                                       definition="De opgelegde en beschreven standaard van de kantopsluiting.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        self.norm = self.waarde.norm
        """De opgelegde en beschreven standaard van de kantopsluiting."""

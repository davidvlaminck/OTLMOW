from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEKantopsluitingBijkomendeParameter import KlLEKantopsluitingBijkomendeParameter
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator
class DtcLENorm(ComplexField):
    """Complex datatype voor de norm van het lijnvormig element."""

    def __init__(self):
        super().__init__(naam="DtcLENorm",
                         label="Norm van het lijnvormig element",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm",
                         definition="Complex datatype voor de norm van het lijnvormig element.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.bijkomendeParameter = KeuzelijstField(naam="bijkomendeParameter",
                                                          lijst=KlLEKantopsluitingBijkomendeParameter(),
                                                          overerving=0,
                                                          label="bijkomende parameter",
                                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm.bijkomendeParameter",
                                                          definition="Het gedetailleerder typeren van de kantopsluiting.",
                                                          constraints="",
                                                          usagenote="",
                                                          deprecated_version="")
        self.bijkomendeParameter = self.waarde.bijkomendeParameter
        """Het gedetailleerder typeren van de kantopsluiting."""

        self.waarde.norm = StringField(naam="norm",
                                       label="norm",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcLENorm.norm",
                                       definition="De opgelegde en beschreven standaard van de kantopsluiting.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        self.norm = self.waarde.norm
        """De opgelegde en beschreven standaard van de kantopsluiting."""

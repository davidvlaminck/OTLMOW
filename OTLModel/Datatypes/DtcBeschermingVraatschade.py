from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlMateriaalBeschermingVraatschade import KlMateriaalBeschermingVraatschade


# Generated with OTLComplexDatatypeCreator
class DtcBeschermingVraatschade(ComplexField):
    """Complex datatype voor bescherming van de stam tegen knaagdieren."""

    def __init__(self):
        super().__init__(naam="DtcBeschermingVraatschade",
                         label="Bescherming vraatschade",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBeschermingVraatschade",
                         definition="Complex datatype voor bescherming van de stam tegen knaagdieren.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.materiaal = KeuzelijstField(naam="materiaal",
                                                label="materiaal",
                                                lijst=KlMateriaalBeschermingVraatschade(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBeschermingVraatschade.materiaal",
                                                definition="De middelen als bescherming tegen vraatschade.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.materiaal = self.waarde.materiaal
        """De middelen als bescherming tegen vraatschade."""

        self.waarde.tegenMaaischade = BooleanField(naam="tegenMaaischade",
                                                   label="tegen maaischade",
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcBeschermingVraatschade.tegenMaaischade",
                                                   definition="Aanduiding of er bescherming tegen maaischade aanwezig is.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        self.tegenMaaischade = self.waarde.tegenMaaischade
        """Aanduiding of er bescherming tegen maaischade aanwezig is."""

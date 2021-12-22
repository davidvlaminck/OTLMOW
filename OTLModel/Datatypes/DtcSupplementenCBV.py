from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlKleurSupp import KlKleurSupp
from OTLModel.Datatypes.KlTypeSuppCBV import KlTypeSuppCBV


# Generated with OTLComplexDatatypeCreator
class DtcSupplementenCBV(ComplexField):
    """Complex datatype voor de supplementen van de CBV."""

    def __init__(self):
        super().__init__(naam="DtcSupplementenCBV",
                         label="Supplementen CBV",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV",
                         definition="Complex datatype voor de supplementen van de CBV.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.kleur = KeuzelijstField(naam="kleur",
                                            lijst=KlKleurSupp(),
                                            overerving=0,
                                            label="kleur",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV.kleur",
                                            definition="De kleur van de supplementen toegevoegd aan de verharding.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        self.kleur = self.waarde.kleur
        """De kleur van de supplementen toegevoegd aan de verharding."""

        self.waarde.type = KeuzelijstField(naam="type",
                                           lijst=KlTypeSuppCBV(),
                                           overerving=0,
                                           label="type",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSupplementenCBV.type",
                                           definition="Het type van de supplementen toegevoegd aan de verharding.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.type = self.waarde.type
        """Het type van de supplementen toegevoegd aan de verharding."""

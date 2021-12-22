from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlConstructiestaalsoort import KlConstructiestaalsoort
from OTLModel.Datatypes.KlWalsmethode import KlWalsmethode


# Generated with OTLComplexDatatypeCreator
class DtcConstructiestaalspecificaties(ComplexField):
    """Complex datatype om de eigenschappen van constructiestaal te bundelen."""

    def __init__(self):
        super().__init__(naam="DtcConstructiestaalspecificaties",
                         label="Constructiestaalspecificaties",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcConstructiestaalspecificaties",
                         definition="Complex datatype om de eigenschappen van constructiestaal te bundelen.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.staalsoort = KeuzelijstField(naam="staalsoort",
                                                 lijst=KlConstructiestaalsoort(),
                                                 overerving=0,
                                                 label="staalsoort",
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcConstructiestaalspecificaties.staalsoort",
                                                 definition="Staalkwaliteit die wordt gebruikt volgens Europese normen.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        self.staalsoort = self.waarde.staalsoort
        """Staalkwaliteit die wordt gebruikt volgens Europese normen."""

        self.waarde.walsmethode = KeuzelijstField(naam="walsmethode",
                                                  lijst=KlWalsmethode(),
                                                  overerving=0,
                                                  label="walsmethode",
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcConstructiestaalspecificaties.walsmethode",
                                                  definition="Op welke manier het staal gewalst is.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        self.walsmethode = self.waarde.walsmethode
        """Op welke manier het staal gewalst is."""

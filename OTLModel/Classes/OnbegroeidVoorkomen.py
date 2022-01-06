from OTLModel.Classes.AndereVerharding import AndereVerharding
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOnbegroeidVoorkomenType import KlOnbegroeidVoorkomenType


# Generated with OTLClassCreator. To modify: extend, do not edit
class OnbegroeidVoorkomen(AndereVerharding):
    """Een ander fysiek voorkomen van het aardoppervlak dat niet vegetatief is."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OnbegroeidVoorkomen"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlOnbegroeidVoorkomenType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OnbegroeidVoorkomen.type",
                                    definition="Type van onbegroeid voorkomen.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Type van onbegroeid voorkomen."""

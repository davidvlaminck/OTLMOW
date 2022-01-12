# coding=utf-8
from OTLModel.Classes.Verkeerslicht import Verkeerslicht
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVriBewaking import KlVriBewaking


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeerslichtRood(Verkeerslicht):
    """Een lichtbron met rode kleur om de weggebruikers aan te geven dat het verboden is de stopstreep of, zo er geen stopstreep is, het verkeerslicht zelf, voorbij te rijden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtRood"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.typeBewaking = KeuzelijstField(naam="typeBewaking",
                                            label="type bewaking",
                                            lijst=KlVriBewaking(),
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtRood.typeBewaking",
                                            definition="Type bewaking van het rode verkeerslicht.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Type bewaking van het rode verkeerslicht."""

from OTLModel.Classes.Verkeerslicht import Verkeerslicht


# Generated with OTLClassCreator
class VerkeerslichtWit(Verkeerslicht):
    """Een witte lichtbron om het verkeer te regelen van voertuigen van personentransport."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtWit"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

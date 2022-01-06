# coding=utf-8
from OTLModel.Classes.Verkeerslicht import Verkeerslicht


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerkeerslichtOranjegeel(Verkeerslicht):
    """Een lichtbron met oranje-gele kleur om de weggebruikers aan te geven dat het verboden is de stopstreep of, zo er geen stopstreep is, het verkeerslicht zelf, voorbij te rijden, tenzij de bestuurder bij het aangaan van dat licht zo dicht genaderd is, dat hij niet meer op voldoende veilige wijze kan stoppen. Als dit licht bij een kruispunt geplaatst is, mag de bestuurder, die de stopstreep of het licht in dergelijke omstandigheden voorbijgereden is, het kruispunt evenwel slechts oversteken op voorwaarde de andere weggebruikers niet in gevaar te brengen"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtOranjegeel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

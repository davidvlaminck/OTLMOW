from OTLModel.Classes.NaampadObject import NaampadObject
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlNetwerklinkMediumtype import KlNetwerklinkMediumtype
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Link(NaampadObject):
    """Het (glasvezel) traject tussen twee toestellen (NetwerkElementen) die rechtstreeks met mekaar communiceren."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.geleidingsgroepTnummer = IntegerField(naam="geleidingsgroepTnummer",
                                                   label="geleidingsgroep T-nummer",
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link.geleidingsgroepTnummer",
                                                   definition="T-nummer van de geleidingsgroep in de kabelnet toepassing.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """T-nummer van de geleidingsgroep in de kabelnet toepassing."""

        self.mediumtype = KeuzelijstField(naam="mediumtype",
                                          label="mediumtype",
                                          lijst=KlNetwerklinkMediumtype(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link.mediumtype",
                                          definition="Geeft aan hoe de verbinding tussen Netwerkelementen fysiek gerealiseerd wordt",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Geeft aan hoe de verbinding tussen Netwerkelementen fysiek gerealiseerd wordt"""

        self.ring = StringField(naam="ring",
                                label="ring",
                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link.ring",
                                definition="Naam van de ringstructuur in het transport netwerk.",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
        """Naam van de ringstructuur in het transport netwerk."""

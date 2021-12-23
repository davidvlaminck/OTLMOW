from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DtcBeschermingVraatschade import DtcBeschermingVraatschade
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAantalBoompalen import KlAantalBoompalen
from OTLModel.Datatypes.KlBeschermingMaaischade import KlBeschermingMaaischade
from OTLModel.Datatypes.KlBoomVerankering import KlBoomVerankering
from OTLModel.Datatypes.KlBoomVerankeringtype import KlBoomVerankeringtype
from OTLModel.Datatypes.KlGroeiplaatsverbetering import KlGroeiplaatsverbetering
from OTLModel.Datatypes.KlMateriaalBeschermingVraatschade import KlMateriaalBeschermingVraatschade
from OTLModel.Datatypes.KlPlantmaatHoogte import KlPlantmaatHoogte
from OTLModel.Datatypes.KlPlantmaatOmtrek import KlPlantmaatOmtrek
from OTLModel.Datatypes.KlVegetatieWortel import KlVegetatieWortel
from OTLModel.Datatypes.KlVormAanleveringHoutigeVegetatie import KlVormAanleveringHoutigeVegetatie


# Generated with OTLComplexDatatypeCreator
class DtcAanlegBoomvorm(ComplexField):
    """Complex datatype om alle eigenschappen van de aanleg van een opgaande boom onder 1 noemer te houden."""

    def __init__(self):
        super().__init__(naam="DtcAanlegBoomvorm",
                         label="aanleg boomvorm",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm",
                         definition="Complex datatype om alle eigenschappen van de aanleg van een opgaande boom onder 1 noemer te houden.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.boompaalconstructie = KeuzelijstField(naam="boompaalconstructie",
                                                          label="boompaalconstructie",
                                                          lijst=KlAantalBoompalen(),
                                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.boompaalconstructie",
                                                          definition="Een constructie om de wortels van de aangeplante boom vast te zetten of te fixeren met oa. palen.",
                                                          constraints="",
                                                          usagenote="",
                                                          deprecated_version="")
        self.boompaalconstructie = self.waarde.boompaalconstructie
        """Een constructie om de wortels van de aangeplante boom vast te zetten of te fixeren met oa. palen."""

        self.waarde.groeiplaatsverbetering = KeuzelijstField(naam="groeiplaatsverbetering",
                                                             label="groeiplaatsverbetering",
                                                             lijst=KlGroeiplaatsverbetering(),
                                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.groeiplaatsverbetering",
                                                             definition="De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren.",
                                                             constraints="",
                                                             usagenote="",
                                                             deprecated_version="")
        self.groeiplaatsverbetering = self.waarde.groeiplaatsverbetering
        """De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren."""

        self.waarde.heeftBoomplaat = BooleanField(naam="heeftBoomplaat",
                                                  label="heeft boomplaat",
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.heeftBoomplaat",
                                                  definition="Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        self.heeftBoomplaat = self.waarde.heeftBoomplaat
        """Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden."""

        self.waarde.heeftWortelgeleidingwortelwering = BooleanField(naam="heeftWortelgeleidingwortelwering",
                                                                    label="heeft wortelgeleiding wortelwering",
                                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.heeftWortelgeleidingwortelwering",
                                                                    definition="Aanduiding of de boom wortelwering heeft. Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen.",
                                                                    constraints="",
                                                                    usagenote="",
                                                                    deprecated_version="")
        self.heeftWortelgeleidingwortelwering = self.waarde.heeftWortelgeleidingwortelwering
        """Aanduiding of de boom wortelwering heeft. Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen."""

        self.waarde.maaischadeBescherming = KeuzelijstField(naam="maaischadeBescherming",
                                                            label="maaischade bescherming",
                                                            lijst=KlBeschermingMaaischade(),
                                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.maaischadeBescherming",
                                                            definition="Bescherming van de stam tegen maaimachines.",
                                                            constraints="",
                                                            usagenote="",
                                                            deprecated_version="")
        self.maaischadeBescherming = self.waarde.maaischadeBescherming
        """Bescherming van de stam tegen maaimachines."""

        self.waarde.plantmaatHoogte = KeuzelijstField(naam="plantmaatHoogte",
                                                      label="plantmaat hoogte",
                                                      lijst=KlPlantmaatHoogte(),
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.plantmaatHoogte",
                                                      definition="De hoogte in meter gemeten van de stamvoet tot de top met een minimum en maximum waarde.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.plantmaatHoogte = self.waarde.plantmaatHoogte
        """De hoogte in meter gemeten van de stamvoet tot de top met een minimum en maximum waarde."""

        self.waarde.plantmaatOmtrek = KeuzelijstField(naam="plantmaatOmtrek",
                                                      label="plantmaat omtrek",
                                                      lijst=KlPlantmaatOmtrek(),
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.plantmaatOmtrek",
                                                      definition="De stamomtrek in centimeter  (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.plantmaatOmtrek = self.waarde.plantmaatOmtrek
        """De stamomtrek in centimeter  (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde."""

        self.waarde.verankering = KeuzelijstField(naam="verankering",
                                                  label="verankering",
                                                  lijst=KlBoomVerankering(),
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.verankering",
                                                  definition="Aanduiding of de boom onder- of bovengronds gefixeerd wordt.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        self.verankering = self.waarde.verankering
        """Aanduiding of de boom onder- of bovengronds gefixeerd wordt."""

        self.waarde.verankeringstype = KeuzelijstField(naam="verankeringstype",
                                                       label="verankeringstype",
                                                       lijst=KlBoomVerankeringtype(),
                                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.verankeringstype",
                                                       definition="Het materiaal van de fixering of verankering.",
                                                       constraints="",
                                                       usagenote="",
                                                       deprecated_version="")
        self.verankeringstype = self.waarde.verankeringstype
        """Het materiaal van de fixering of verankering."""

        self.waarde.vormAanlevering = KeuzelijstField(naam="vormAanlevering",
                                                      label="vorm aanlevering",
                                                      lijst=KlVormAanleveringHoutigeVegetatie(),
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.vormAanlevering",
                                                      definition="De wijze waarop het plantgoed wordt aangeleverd.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.vormAanlevering = self.waarde.vormAanlevering
        """De wijze waarop het plantgoed wordt aangeleverd."""

        self.waarde.vraatschadeBescherming = KeuzelijstField(naam="vraatschadeBescherming",
                                                             label="vraatschade bescherming",
                                                             lijst=KlMateriaalBeschermingVraatschade(),
                                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.vraatschadeBescherming",
                                                             definition="Bescherming van de stam tegen knaagdieren.",
                                                             constraints="",
                                                             usagenote="",
                                                             deprecated_version="")
        self.vraatschadeBescherming = self.waarde.vraatschadeBescherming
        """Bescherming van de stam tegen knaagdieren."""

        self.waarde.wortelAanplant = KeuzelijstField(naam="wortelAanplant",
                                                     label="wortel aanplant",
                                                     lijst=KlVegetatieWortel(),
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcAanlegBoomvorm.wortelAanplant",
                                                     definition="De manier van levering en aanplanting van het wortelgestel van de boom of plant.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        self.wortelAanplant = self.waarde.wortelAanplant
        """De manier van levering en aanplanting van het wortelgestel van de boom of plant."""

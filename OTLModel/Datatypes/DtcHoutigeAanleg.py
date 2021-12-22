from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcBeschermingVraatschade import DtcBeschermingVraatschade
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBeschermingMaaischade import KlBeschermingMaaischade
from OTLModel.Datatypes.KlMateriaalBeschermingVraatschade import KlMateriaalBeschermingVraatschade
from OTLModel.Datatypes.KlPlantmaatHoogte import KlPlantmaatHoogte
from OTLModel.Datatypes.KlPlantmaatOmtrek import KlPlantmaatOmtrek
from OTLModel.Datatypes.KlVegetatiePlantverband import KlVegetatiePlantverband
from OTLModel.Datatypes.KlVegetatieWortel import KlVegetatieWortel
from OTLModel.Datatypes.KlVormAanleveringHoutigeVegetatie import KlVormAanleveringHoutigeVegetatie
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


# Generated with OTLComplexDatatypeCreator
class DtcHoutigeAanleg(ComplexField):
    """Complex datatype dat de aanleg van houtige vegetatie beschrijft."""

    def __init__(self):
        super().__init__(naam="DtcHoutigeAanleg",
                         label="Houtige aanleg",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg",
                         definition="Complex datatype dat de aanleg van houtige vegetatie beschrijft.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.beschermingVraatschade = DtcBeschermingVraatschade()
        self.waarde.beschermingVraatschade.naam = "beschermingVraatschade"
        self.waarde.beschermingVraatschade.label = "bescherming vraatschade"
        self.waarde.beschermingVraatschade.definition = "Bescherming van de stam tegen knaagdieren."
        self.waarde.beschermingVraatschade.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.beschermingVraatschade"
        self.waarde.beschermingVraatschade.overerving = 0
        self.waarde.beschermingVraatschade.constraints = ""
        self.waarde.beschermingVraatschade.readonly = 0
        self.waarde.beschermingVraatschade.usagenote = "Attribuut uit gebruik sinds versie 2.0.0"
        self.waarde.beschermingVraatschade.deprecated_version = "2.0.0"
        self.beschermingVraatschade = self.waarde.beschermingVraatschade
        """Bescherming van de stam tegen knaagdieren."""

        self.waarde.heeftBoomplaat = BooleanField(naam="heeftBoomplaat",
                                                  label="heeft boomplaat",
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.heeftBoomplaat",
                                                  definition="Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        self.heeftBoomplaat = self.waarde.heeftBoomplaat
        """Boomplaten worden aangebracht rond de stam van bomen, bosgoed en heesters en eventueel vastgezet met piketten. Ze hebben een centrale opening en een rechte snede, zodat ze op eenvoudige wijze rond de planten kunnen aangebracht worden."""

        self.waarde.heeftHaagsteun = BooleanField(naam="heeftHaagsteun",
                                                  label="heeft haagsteun",
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.heeftHaagsteun",
                                                  definition="Duidt op de aanezigheid van een constructie van palen en bedrading die haagbeplanting ondersteunt.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        self.heeftHaagsteun = self.waarde.heeftHaagsteun
        """Duidt op de aanezigheid van een constructie van palen en bedrading die haagbeplanting ondersteunt."""

        self.waarde.heeftWortelgeleidingwortelwering = BooleanField(naam="heeftWortelgeleidingwortelwering",
                                                                    label="heeft wortelgeleiding-wortelwering",
                                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.heeftWortelgeleidingwortelwering",
                                                                    definition="Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen. Het heeft als doel om boomwortels naar beneden te leiden, waar ze onder een obstakel verder kunnen groeien.",
                                                                    constraints="",
                                                                    usagenote="",
                                                                    deprecated_version="")
        self.heeftWortelgeleidingwortelwering = self.waarde.heeftWortelgeleidingwortelwering
        """Wortelgeleiding en –wering moet voorkomen dat boomwortels het trottoir, de middenberm, het fietspad, de rijweg, andere wegverhardingen en leidingstelsels beschadigen. Het heeft als doel om boomwortels naar beneden te leiden, waar ze onder een obstakel verder kunnen groeien."""

        self.waarde.maaischadeBescherming = KeuzelijstField(naam="maaischadeBescherming",
                                                            lijst=KlBeschermingMaaischade(),
                                                            overerving=0,
                                                            label="maaischade bescherming",
                                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.maaischadeBescherming",
                                                            definition="Bescherming van de stam tegen maaimachines.",
                                                            constraints="",
                                                            usagenote="",
                                                            deprecated_version="")
        self.maaischadeBescherming = self.waarde.maaischadeBescherming
        """Bescherming van de stam tegen maaimachines."""

        self.waarde.plantafstand = NonNegIntegerField(naam="plantafstand",
                                                      label="plantafstand",
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantafstand",
                                                      definition="Aantal planten per lopende meter.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.plantafstand = self.waarde.plantafstand
        """Aantal planten per lopende meter."""

        self.waarde.plantdichtheid = NonNegIntegerField(naam="plantdichtheid",
                                                        label="plantdichtheid",
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantdichtheid",
                                                        definition="Aantal planten per vierkante meter.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        self.plantdichtheid = self.waarde.plantdichtheid
        """Aantal planten per vierkante meter."""

        self.waarde.plantmaatHoogte = KeuzelijstField(naam="plantmaatHoogte",
                                                      lijst=KlPlantmaatHoogte(),
                                                      overerving=0,
                                                      label="plantmaat hoogte",
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantmaatHoogte",
                                                      definition="De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.plantmaatHoogte = self.waarde.plantmaatHoogte
        """De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde."""

        self.waarde.plantmaatOmtrek = KeuzelijstField(naam="plantmaatOmtrek",
                                                      lijst=KlPlantmaatOmtrek(),
                                                      overerving=0,
                                                      label="plantmaat omtrek",
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantmaatOmtrek",
                                                      definition="De stamomtrek in centimeter  (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.plantmaatOmtrek = self.waarde.plantmaatOmtrek
        """De stamomtrek in centimeter  (gemeten op 1 m boven het maaiveld) met een minimum en maximum waarde."""

        self.waarde.plantverband = KeuzelijstField(naam="plantverband",
                                                   lijst=KlVegetatiePlantverband(),
                                                   overerving=0,
                                                   label="plantverband",
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.plantverband",
                                                   definition="De wijze waarop de planten zijn geschikt.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        self.plantverband = self.waarde.plantverband
        """De wijze waarop de planten zijn geschikt."""

        self.waarde.vormAanlevering = KeuzelijstField(naam="vormAanlevering",
                                                      lijst=KlVormAanleveringHoutigeVegetatie(),
                                                      overerving=0,
                                                      label="vorm aanlevering",
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.vormAanlevering",
                                                      definition="De wijze waarop het plantgoed wordt aangeleverd.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        self.vormAanlevering = self.waarde.vormAanlevering
        """De wijze waarop het plantgoed wordt aangeleverd."""

        self.waarde.vraatschadeBescherming = KeuzelijstField(naam="vraatschadeBescherming",
                                                             lijst=KlMateriaalBeschermingVraatschade(),
                                                             overerving=0,
                                                             label="vraatschade bescherming",
                                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.vraatschadeBescherming",
                                                             definition="Bescherming van de stam tegen knaagdieren.",
                                                             constraints="",
                                                             usagenote="",
                                                             deprecated_version="")
        self.vraatschadeBescherming = self.waarde.vraatschadeBescherming
        """Bescherming van de stam tegen knaagdieren."""

        self.waarde.wortel = KeuzelijstField(naam="wortel",
                                             lijst=KlVegetatieWortel(),
                                             overerving=0,
                                             label="wortel",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcHoutigeAanleg.wortel",
                                             definition="De manier van levering en aanplanting van het wortelgestel van de boom of plant.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        self.wortel = self.waarde.wortel
        """De manier van levering en aanplanting van het wortelgestel van de boom of plant."""

from OTLModel.Classes.VegetatieElement import VegetatieElement
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator
class Klimvorm(VegetatieElement):
    """Plant met buigzame stengels die zich aan muren,bomen,enz. hecht en zodoende omhoog klimt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.begroeidOppervlak = KwantWrdInVierkanteMeter()
        """Verticale oppervlakte dat begroeid is in vierkante meter."""
        self.begroeidOppervlak.naam = "begroeidOppervlak"
        self.begroeidOppervlak.label = "begroeid oppervlak"
        self.begroeidOppervlak.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.begroeidOppervlak"
        self.begroeidOppervlak.definition = "Verticale oppervlakte dat begroeid is in vierkante meter."
        self.begroeidOppervlak.constraints = ""
        self.begroeidOppervlak.usagenote = ""
        self.begroeidOppervlak.deprecated_version = ""

        self.heeftBeheerScheren = BooleanField(naam="heeftBeheerScheren",
                                               label="heeft beheer scheren",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.heeftBeheerScheren",
                                               definition="Duidt aan of de klimvorm al dan niet geschoren wordt.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Duidt aan of de klimvorm al dan niet geschoren wordt."""

        self.heeftBevestigingconstructie = BooleanField(naam="heeftBevestigingconstructie",
                                                        label="Heeft bevestigingsconstructie",
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.heeftBevestigingconstructie",
                                                        definition="Aanduiding of de klimvorm een bevestigingsconstructie heeft om aan bv een geluidswerende constructie vastgemaakt te worden.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        """Aanduiding of de klimvorm een bevestigingsconstructie heeft om aan bv een geluidswerende constructie vastgemaakt te worden."""

        self.isGrondgebonden = BooleanField(naam="isGrondgebonden",
                                            label="is grondgebonden",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.isGrondgebonden",
                                            definition="Duidt aan of de klimvorm al dan niet in volle grond staat.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Duidt aan of de klimvorm al dan niet in volle grond staat."""

        self.isZelfhechtend = BooleanField(naam="isZelfhechtend",
                                           label="is zelfhechtend",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.isZelfhechtend",
                                           definition="Geeft aan of de klimplant (zoals klimop of wingerd) rechtstreeks op de muur kan groeien zonder nood aan een draagstructuur.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Geeft aan of de klimplant (zoals klimop of wingerd) rechtstreeks op de muur kan groeien zonder nood aan een draagstructuur."""

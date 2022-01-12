# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDekselKaderType import KlDekselKaderType
from OTLModel.Datatypes.KlDekselKlasse import KlDekselKlasse
from OTLModel.Datatypes.KlDekselMateriaal import KlDekselMateriaal
from OTLModel.Datatypes.KlDekselRegeling import KlDekselRegeling
from OTLModel.Datatypes.KlDekselVergrendeling import KlDekselVergrendeling
from OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class PutBovenbouw(AIMObject):
    """Een combinatie van het riooldeksel met de kader en de regeling."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInCentimeter()
        """Breedte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de hoogte."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.breedte"
        self.breedte.definition = "Breedte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de hoogte."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.dekselklasse = KeuzelijstField(naam="dekselklasse",
                                            label="dekselklasse",
                                            lijst=KlDekselKlasse(),
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.dekselklasse",
                                            definition="Bepaalt de mate waarin het deksel van de bovenbouw belast kan worden door voertuigen.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Bepaalt de mate waarin het deksel van de bovenbouw belast kan worden door voertuigen."""

        self.dekselvorm = KeuzelijstField(naam="dekselvorm",
                                          label="dekselvorm",
                                          lijst=KlRioleringVorm(),
                                          objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.dekselvorm",
                                          definition="Bepaalt de vorm van het deksel.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Bepaalt de vorm van het deksel."""

        self.hoogte = KwantWrdInCentimeter()
        """Hoogte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de breedte."""
        self.hoogte.naam = "hoogte"
        self.hoogte.label = "hoogte"
        self.hoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.hoogte"
        self.hoogte.definition = "Hoogte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de breedte."
        self.hoogte.constraints = ""
        self.hoogte.usagenote = ""
        self.hoogte.deprecated_version = ""

        self.isAfgesloten = BooleanField(naam="isAfgesloten",
                                         label="is afgesloten",
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.isAfgesloten",
                                         definition="Bepaling of de afsluitinrichting vergrendeld is of niet.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaling of de afsluitinrichting vergrendeld is of niet."""

        self.isScharnierend = BooleanField(naam="isScharnierend",
                                           label="is scharnierend",
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.isScharnierend",
                                           definition="Het deksel is al of niet bevestigd met een scharnier.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Het deksel is al of niet bevestigd met een scharnier."""

        self.isWaterdichtVergrendeld = BooleanField(naam="isWaterdichtVergrendeld",
                                                    label="Is waterdicht vergrendeld",
                                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.isWaterdichtVergrendeld",
                                                    definition="Geeft aan of de bovenbouw al dan niet waterdicht vergrendeld is zodat het water zich niet boven de bovenbouw kan begeven.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """Geeft aan of de bovenbouw al dan niet waterdicht vergrendeld is zodat het water zich niet boven de bovenbouw kan begeven."""

        self.kader = KeuzelijstField(naam="kader",
                                     label="kader",
                                     lijst=KlDekselKaderType(),
                                     objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.kader",
                                     definition="Bepaalt het type van het dekselkader.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Bepaalt het type van het dekselkader."""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlDekselMateriaal(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.materiaal",
                                         definition="Het materiaal waaruit het deksel van de bovenbouw is vervaardigd.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Het materiaal waaruit het deksel van de bovenbouw is vervaardigd."""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van het zichtbare deel van de bovenbouw in vierkante meter."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van het zichtbare deel van de bovenbouw in vierkante meter."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        self.regeling = KeuzelijstField(naam="regeling",
                                        label="regeling",
                                        lijst=KlDekselRegeling(),
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.regeling",
                                        definition="De wijze hoe de regeling van het deksel is uitgevoerd.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """De wijze hoe de regeling van het deksel is uitgevoerd."""

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.technischeFiche"
        technischeFicheField.definition = "De technische fiche van de bovenbouw."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = "Bestanden van het type xlsx of pdf."
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """De technische fiche van de bovenbouw."""

        self.vergrendeling = KeuzelijstField(naam="vergrendeling",
                                             label="vergrendeling",
                                             lijst=KlDekselVergrendeling(),
                                             objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.vergrendeling",
                                             definition="Bepaalt het type sleutel voor het ontgrendelen van het deksel.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Bepaalt het type sleutel voor het ontgrendelen van het deksel."""

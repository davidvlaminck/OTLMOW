# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KlAIMToestand(KeuzelijstField):
    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""
    naam = "KlAIMToestand"
    label = "AIM toestand"
    objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand"
    definition = "Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."
    codelist = "https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand"
    options = {
        'geannuleerd': KeuzelijstWaarde(invulwaarde="geannuleerd",
                                        label="geannuleerd",
                                        definitie="",
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/geannuleerd"),
        'gepland': KeuzelijstWaarde(invulwaarde="gepland",
                                    label="gepland",
                                    definitie="",
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/gepland"),
        'in-gebruik': KeuzelijstWaarde(invulwaarde="in-gebruik",
                                       label="in gebruik",
                                       definitie="",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik"),
        'in-ontwerp': KeuzelijstWaarde(invulwaarde="in-ontwerp",
                                       label="in ontwerp",
                                       definitie="",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp"),
        'in-opbouw': KeuzelijstWaarde(invulwaarde="in-opbouw",
                                      label="in opbouw",
                                      definitie="",
                                      objectUri="https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-opbouw"),
        'overgedragen': KeuzelijstWaarde(invulwaarde="overgedragen",
                                         label="overgedragen",
                                         definitie="",
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/overgedragen"),
        "uit-gebruik": KeuzelijstWaarde(invulwaarde="overgedragen",
                                        label="overgedragen",
                                        definitie="",
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/overgedragen"),
        "verwijderd": KeuzelijstWaarde(invulwaarde="verwijderd",
                                       label="verwijderd",
                                       definitie="",
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd"),
    }

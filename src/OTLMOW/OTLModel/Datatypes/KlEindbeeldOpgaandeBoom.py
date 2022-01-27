# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEindbeeldOpgaandeBoom(KeuzelijstField):
    """Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats."""
    naam = 'KlEindbeeldOpgaandeBoom'
    label = 'Eindbeeld opgaande boom'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEindbeeldOpgaandeBoom'
    definition = 'Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEindbeeldOpgaandeBoom'
    options = {
        'gekandelaarde-boom': KeuzelijstWaarde(invulwaarde='gekandelaarde-boom',
                                               label='gekandelaarde boom',
                                               definitie='Het eindbeeld is een gekandelaarde boom. Een gekandelaarde boom is een boom waarvan alle gesteltakken periodiek op een bepaalde lengte worden afgezet en die hierop opnieuw uitlopen.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/gekandelaarde-boom'),
        'geschoren-boom': KeuzelijstWaarde(invulwaarde='geschoren-boom',
                                           label='geschoren boom',
                                           definitie='Het eindbeeld is een geschoren boom.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/geschoren-boom'),
        'knotboom': KeuzelijstWaarde(invulwaarde='knotboom',
                                     label='knotboom',
                                     definitie='Het eindbeeld is een knotboom. Dit is een snoeivorm waarbij periodiek alle takken afgezaagd worden tot op een verdikte knot bovenaan de stam.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/knotboom'),
        'leiboom': KeuzelijstWaarde(invulwaarde='leiboom',
                                    label='leiboom',
                                    definitie='Het eindbeeld is een leiboom. Een leiboom is een boom waarvan alle gesteltakken gedwongen worden in één (verticaal) vlak te groeien door geleiding. Soms worden de geleide bomen tegen een muur geleid of wordt er in een leidconstructie voorzien.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/leiboom'),
        'niet-vrij-uitgroeiend': KeuzelijstWaarde(invulwaarde='niet-vrij-uitgroeiend',
                                                  label='niet vrij uitgroeiend',
                                                  definitie='Het eindbeeld is een boom die niet vrij kan uitgroeien.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/niet-vrij-uitgroeiend'),
        'vrij-uitgroeiend': KeuzelijstWaarde(invulwaarde='vrij-uitgroeiend',
                                             label='vrij uitgroeiend',
                                             definitie='Het eindbeeld is een boom die vrij kan uitgroeien.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/vrij-uitgroeiend')
    }


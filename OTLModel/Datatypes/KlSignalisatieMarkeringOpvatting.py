# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignalisatieMarkeringOpvatting(KeuzelijstField):
    """De markeringsopvattingen van de markering."""
    naam = 'KlSignalisatieMarkeringOpvatting'
    label = 'Signalisatie markering opvatting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignalisatieMarkeringOpvatting'
    definition = 'De markeringsopvattingen van de markering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignalisatieMarkeringOpvatting'
    options = {
        'middelenverbintenis': KeuzelijstWaarde(invulwaarde='middelenverbintenis',
                                                label='middelenverbintenis',
                                                definitie='Legt de nadruk op de wijze van aanbrengen en doseringen.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieMarkeringOpvatting/middelenverbintenis'),
        'resultaatsverbintenis': KeuzelijstWaarde(invulwaarde='resultaatsverbintenis',
                                                  label='resultaatsverbintenis',
                                                  definitie='Houdt in dat de doseringen niet worden vastgelegd in het bijzonder bestek maar dat de markeringen, in nieuwe toestand en gedurende de waarborgperiode voor de markering, moeten voldoen aan resultaatseisen. ',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieMarkeringOpvatting/resultaatsverbintenis')
    }


# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCameraBeeldverwerkingstype(KeuzelijstField):
    """Lijst met mogelijke types van beeldverwerking eigen aan een camera (in tegenstelling tot beeldverwerking door andere assets)."""
    naam = 'KlCameraBeeldverwerkingstype'
    label = 'Camera beeldverwerkingstypes'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraBeeldverwerkingstype'
    definition = 'Lijst met mogelijke types van beeldverwerking eigen aan een camera (in tegenstelling tot beeldverwerking door andere assets).'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraBeeldverwerkingstype'
    options = {
        'adr': KeuzelijstWaarde(invulwaarde='adr',
                                label='ADR',
                                definitie='Interne beeldverwerking van het type ADR (detectie van symbolen op vrachtvervoer die gevaarlijke ladingen aangeven volgens het ADR-verdrag).',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraBeeldverwerkingstype/adr'),
        'aid': KeuzelijstWaarde(invulwaarde='aid',
                                label='AID',
                                definitie='Interne beeldverwerking van het type automatische incident detectie (AID).',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraBeeldverwerkingstype/aid')
    }


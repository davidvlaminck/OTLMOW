# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeSuppCBV(KeuzelijstField):
    """Keuzelijst om het type van de toegevoegde supplementen van de CBV te bepalen."""
    naam = 'KlTypeSuppCBV'
    label = 'Type supplementen CBV'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeSuppCBV'
    definition = 'Keuzelijst om het type van de toegevoegde supplementen van de CBV te bepalen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeSuppCBV'
    options = {
        'figureren-betonoppervlak-in-de-massa-gekleurd': KeuzelijstWaarde(invulwaarde='figureren-betonoppervlak-in-de-massa-gekleurd',
                                                                          label='figureren betonoppervlak in de massa gekleurd',
                                                                          definitie='Supplementen voor het bekomen van een in de massa gekleurde CBV.',
                                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSuppCBV/figureren-betonoppervlak-in-de-massa-gekleurd'),
        'figureren-betonoppervlak-met-kleurverharder': KeuzelijstWaarde(invulwaarde='figureren-betonoppervlak-met-kleurverharder',
                                                                        label='figureren betonoppervlak met kleurverharder',
                                                                        definitie='Supplementen voor het bekomen van een gekleurde 2 laagse deklaag van CBV.',
                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSuppCBV/figureren-betonoppervlak-met-kleurverharder')
    }


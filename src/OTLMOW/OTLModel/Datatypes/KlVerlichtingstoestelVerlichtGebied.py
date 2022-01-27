# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelVerlichtGebied(KeuzelijstField):
    """Het gebied op de wegbaan of het object dat verlicht wordt door het verlichtingstoestel."""
    naam = 'KlVerlichtingstoestelVerlichtGebied'
    label = 'Verlichtingstoestel verlicht gebied.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelVerlichtGebied'
    definition = 'Het gebied op de wegbaan of het object dat verlicht wordt door het verlichtingstoestel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelVerlichtGebied'
    options = {
        'afrit': KeuzelijstWaarde(invulwaarde='afrit',
                                  label='afrit',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/afrit'),
        'bebakening': KeuzelijstWaarde(invulwaarde='bebakening',
                                       label='bebakening',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/bebakening'),
        'doorlopende-straatverlichting': KeuzelijstWaarde(invulwaarde='doorlopende-straatverlichting',
                                                          label='doorlopende straatverlichting',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/doorlopende-straatverlichting'),
        'fietspad': KeuzelijstWaarde(invulwaarde='fietspad',
                                     label='fietspad',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/fietspad'),
        'hoofdweg': KeuzelijstWaarde(invulwaarde='hoofdweg',
                                     label='hoofdweg',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/hoofdweg'),
        'kruispunt': KeuzelijstWaarde(invulwaarde='kruispunt',
                                      label='kruispunt',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/kruispunt'),
        'monument': KeuzelijstWaarde(invulwaarde='monument',
                                     label='monument',
                                     definitie='Alle niet-functie verlichting, dus alle verlichting die nodig is om je weg te vinden.Verlichting voor artistieke creaties op (bv. rotonde) of rond de openbare weg (bv. ecoduct dat onderaan een schilderij heeft) of voor artistieke belichting (niet verlichting) te geven, bv een hangbrug waarbij de kabels aangelicht worden. Somskan dit ook zijn voor het aanlichten of belichten van gebouwen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/monument'),
        'onderdoorgang': KeuzelijstWaarde(invulwaarde='onderdoorgang',
                                          label='onderdoorgang',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/onderdoorgang'),
        'oprit': KeuzelijstWaarde(invulwaarde='oprit',
                                  label='oprit',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/oprit'),
        'parking': KeuzelijstWaarde(invulwaarde='parking',
                                    label='parking',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/parking'),
        'projector': KeuzelijstWaarde(invulwaarde='projector',
                                      label='projector',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/projector'),
        'punctuele-verlichting': KeuzelijstWaarde(invulwaarde='punctuele-verlichting',
                                                  label='punctuele verlichting',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/punctuele-verlichting'),
        'rotonde': KeuzelijstWaarde(invulwaarde='rotonde',
                                    label='rotonde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/rotonde'),
        'tunnelverlichting': KeuzelijstWaarde(invulwaarde='tunnelverlichting',
                                              label='tunnelverlichting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/tunnelverlichting'),
        'wisselaar': KeuzelijstWaarde(invulwaarde='wisselaar',
                                      label='wisselaar',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelVerlichtGebied/wisselaar')
    }


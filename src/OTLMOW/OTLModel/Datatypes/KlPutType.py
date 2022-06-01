# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPutType(KeuzelijstField):
    """Types van put."""
    naam = 'KlPutType'
    label = 'Put type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutType'
    definition = 'Types van put.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutType'
    options = {
        'aansluitingstoegangsput-(ATP)': KeuzelijstWaarde(invulwaarde='aansluitingstoegangsput-(ATP)',
                                                          label='aansluitingstoegangsput (ATP)',
                                                          definitie='Knijpopening',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/aansluitingstoegangsput-(ATP)'),
        'begintoegangs--of-verbindingsput-(BIP-of-DVP)': KeuzelijstWaarde(invulwaarde='begintoegangs--of-verbindingsput-(BIP-of-DVP)',
                                                                          label='begintoegangs- of verbindingsput (BIP of DVP)',
                                                                          definitie='Begintoegangs- of verbindingsput (= BIP of DVP)',
                                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/begintoegangs--of-verbindingsput-(BIP-of-DVP)'),
        'doorlooptoegangs--of-verbindingsput-(DTP-of-DVP)': KeuzelijstWaarde(invulwaarde='doorlooptoegangs--of-verbindingsput-(DTP-of-DVP)',
                                                                             label='doorlooptoegangs- of verbindingsput (DTP of DVP)',
                                                                             definitie='Doorlooptoegangs- of verbindingsput (= DTP of DVP)',
                                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/doorlooptoegangs--of-verbindingsput-(DTP-of-DVP)'),
        'hoektoegangsput-(HTP)': KeuzelijstWaarde(invulwaarde='hoektoegangsput-(HTP)',
                                                  label='hoektoegangsput (HTP)',
                                                  definitie='Hoektoegangsput (= HTP)',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/hoektoegangsput-(HTP)'),
        'putbuis-of-schachttoegangsput-(STP)': KeuzelijstWaarde(invulwaarde='putbuis-of-schachttoegangsput-(STP)',
                                                                label='putbuis of schachttoegangsput (STP)',
                                                                definitie='Putbuis of schachttoegangsput (= STP)',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/putbuis-of-schachttoegangsput-(STP)'),
        'vervaltoegangsput-(VTP)': KeuzelijstWaarde(invulwaarde='vervaltoegangsput-(VTP)',
                                                    label='vervaltoegangsput (VTP)',
                                                    definitie='Vervaltoegangsput (= VTP)',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutType/vervaltoegangsput-(VTP)')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlPutType.get_dummy_data()


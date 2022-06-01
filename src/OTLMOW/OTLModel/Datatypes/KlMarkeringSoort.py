# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMarkeringSoort(KeuzelijstField):
    """De soorten van markingsproduct. Afgeleid van de COPRO_code."""
    naam = 'KlMarkeringSoort'
    label = 'Soort markeringsproduct'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMarkeringSoort'
    definition = 'De soorten van markingsproduct. Afgeleid van de COPRO_code.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMarkeringSoort'
    options = {
        'geprefabriceerd': KeuzelijstWaarde(invulwaarde='geprefabriceerd',
                                            label='geprefabriceerd',
                                            definitie='Voorgevormde wegmarkering.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/geprefabriceerd'),
        'koudplastisch': KeuzelijstWaarde(invulwaarde='koudplastisch',
                                          label='koudplastisch',
                                          definitie='Een koudplast is een markeringssubstantie gevormd door de chemische reactie van 2 of meerdere componenten (minstens 1 verharder en 1 hoofdcomponent), waarvan geen oplosmiddelen.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/koudplastisch'),
        'thermoplastisch-vlak': KeuzelijstWaarde(invulwaarde='thermoplastisch-vlak',
                                                 label='thermoplastisch vlak',
                                                 definitie='Een thermoplast is een wegmarkeringsproduct zonder oplosmiddel. De substantie wordt door verwarming vloeibaar gemaakt en wordt manueel of mechanisch aangebracht met een geëigend apparaat of toestel. Door afkoeling wordt een geheel gevormd. Een vlak systeem is een film met constante dosering.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/thermoplastisch-vlak'),
        'thermoplastische-multi-dot': KeuzelijstWaarde(invulwaarde='thermoplastische-multi-dot',
                                                       label='thermoplastische multi-dot',
                                                       definitie='Een thermoplast is een wegmarkeringsproduct zonder oplosmiddel. De substantie wordt door verwarming vloeibaar gemaakt en wordt manueel of mechanisch aangebracht met een geëigend apparaat of toestel. Door afkoeling wordt een geheel gevormd. Geprofileerde systemen hebben in dwars- en of lengterichting veranderlijke filmdikte. Hierdoor ontstaat een reliëf met een wisselende hoogte.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/thermoplastische-multi-dot'),
        'thermoplastische-ribbelmarkering': KeuzelijstWaarde(invulwaarde='thermoplastische-ribbelmarkering',
                                                             label='thermoplastische ribbelmarkering',
                                                             definitie='Een thermoplast is een wegmarkeringsproduct zonder oplosmiddel. De substantie wordt door verwarming vloeibaar gemaakt en wordt manueel of mechanisch aangebracht met een geëigend apparaat of toestel. Door afkoeling wordt een geheel gevormd. Geprofileerde systemen hebben in dwars- en of lengterichting veranderlijke filmdikte. Hierdoor ontstaat een reliëf met een wisselende hoogte.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/thermoplastische-ribbelmarkering'),
        'verf': KeuzelijstWaarde(invulwaarde='verf',
                                 label='verf',
                                 definitie='Wegenverf die zich uitstekend leent tot de markering van openbare wegen. Wegenverf is een vloeibaar product dat vaste stoffen zoals bindmiddel, stoffen die kleuren reflecteren, vulstoffen en additieven bevat.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringSoort/verf')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlMarkeringSoort.get_dummy_data()


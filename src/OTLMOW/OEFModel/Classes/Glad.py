# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class Glad(EMObject):
    """Specifiek meldingstype wegen winterdienst : gladheidsmelding, vraag strooiactie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Glad'
    label = 'Gladheidsmelding'

    def __init__(self):
        super().__init__()


# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class Calam(EMObject):
    """Specifiek meldingstype wegen : calamiteitsmelding, vraag interventie district"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Calam'
    label = 'Calamiteit wegen'

    def __init__(self):
        super().__init__()


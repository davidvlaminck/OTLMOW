# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class Wilddet(EMObject):
    """Een wilddetectiesysteem zal de weggebruikers waarschuwen bij de aanwezigheid van eventueel overstekend wild"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Wilddet'
    label = 'Wilddetectiesysteem'

    def __init__(self):
        super().__init__()


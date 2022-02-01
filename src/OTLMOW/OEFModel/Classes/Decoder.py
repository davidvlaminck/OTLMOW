# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class Decoder(EMObject):
    """Camera-uitrusting : Het betreft hier een video-decoder. Deze vormt eendigitale datastroom om tot een analoog videosignaal"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Decoder'
    label = 'Decoder camerabeelden'

    def __init__(self):
        super().__init__()


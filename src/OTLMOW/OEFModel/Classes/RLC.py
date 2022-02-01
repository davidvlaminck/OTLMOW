# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class RLC(EMObject):
    """VHS flitspalen : Installatie Roodlichtcamera - Dit type flitspaal registreert zowel roodlichtnegaties als snelheidsovertredingen. Zij worden opgesteld op kruispunten met verkeerslichten."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#RLC'
    label = 'Roodlichtcamera installatie'

    def __init__(self):
        super().__init__()


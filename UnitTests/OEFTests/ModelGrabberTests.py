import unittest

from OTLMOW.OEFModel.ModelGrabber import ModelGrabber


class ModelGrabberTests(unittest.TestCase):
    def test_grab_model(self):
        grabber = ModelGrabber()
        grabber.decode_json()
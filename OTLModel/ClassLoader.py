import importlib
import importlib.util
import os


class ClassLoader:
    @staticmethod
    def dynamic_create_instance_from_name(class_name):
        py_mod = __import__(name=f'OTLModel.Classes.{class_name}', fromlist=f'Classes.{class_name}')
        class_ = getattr(py_mod, class_name)
        instance = class_()

        return instance



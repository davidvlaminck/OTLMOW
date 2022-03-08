from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject


class ClassLoader:
    """This class attempts to load an OTL class from the corresponding module and instantiate it."""
    @staticmethod
    def dynamic_create_instance_from_name(class_name: str) -> OTLObject | None:
        """Loads the OTL class module and attempts to instantiate the class using the name of the class

        :param class_name: class name to instantiate
        :type: str
        :rtype: OTLObject or None
        :return: returns an instance of class_name, that inherits from OTLObject
        """
        try:
            py_mod = __import__(name=f'OTLMOW.OTLModel.Classes.{class_name}', fromlist=f'Classes.{class_name}')
        except ModuleNotFoundError:
            return None
        class_ = getattr(py_mod, class_name)
        instance = class_()

        return instance

    def dynamic_create_instance_from_uri(self, class_uri: str) -> OTLObject | None:
        class_name = class_uri.split('#')[-1]
        return self.dynamic_create_instance_from_name(class_name)

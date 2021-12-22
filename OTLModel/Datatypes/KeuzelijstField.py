from OTLModel.Datatypes.Keuzelijst import Keuzelijst
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde
from OTLModel.Datatypes.OTLField import OTLField


class KeuzelijstField(OTLField):
    def __init__(self, lijst: Keuzelijst, naam, label, uri, definition, overerving, constraints, usagenote, deprecated_version,
                 readonly=False, readonlyValue=None):
        super().__init__(naam, label, uri, definition, constraints, usagenote, deprecated_version, readonly, readonlyValue)
        self.lijst = lijst
        self.overerving = overerving
        self.waarde = None

    def __setattr__(self, name, value):
        if name == "waarde" and self.readonly and value is not None:
            raise AttributeError(f"can't set the value of a readonly attribute")
        if name == "waarde":
            if value is not None and (not isinstance(value, KeuzelijstWaarde)):
                raise ValueError(f'expecting {self.lijst.__name__} in {self.naam}')
            if value is not None and not value in self.lijst.options:
                raise ValueError(
                    f'{value.invulwaarde} is not a valid option for {self.naam}, find the valid options in {self.lijst}')
        self.__dict__[name] = value

    def default(self):
        if self.waarde is None:
            return None
        return self.waarde.invulwaarde

    def set_value_by_invulwaarde(self, invulwaarde):
        self.waarde = self.lijst.get_value_by_invulwaarde(invulwaarde)

    def set_value_by_label(self, label):
        self.waarde = self.lijst.get_value_by_label(label)


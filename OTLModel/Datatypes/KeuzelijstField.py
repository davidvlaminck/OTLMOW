from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde
from OTLModel.Datatypes.OTLField import OTLField


# alleen keuzelijst waardes + get methods. set methods in keuzelijstField. keuzelijst.waarde -> keuzelijstwaarde
class Keuzelijst:
    def __init__(self, naam, label, uri, definition, usagenote, deprecated_version, codelist):
        self.options = []
        self.codelist = codelist
        self.naam = naam
        self.label = label
        self.uri = uri
        self.definition = definition
        self.usagenote = usagenote
        self.deprecated_version = deprecated_version

    def add_option(self, invulwaarde, label, definitie, uri):
        self.options.append(KeuzelijstWaarde(invulwaarde, label, definitie, uri))

    def get_value_by_invulwaarde(self, invulwaarde):
        try:
            return next(o for o in self.options if o.invulwaarde == invulwaarde)
        except StopIteration:
            raise ValueError(f"There is no option with waarde '{invulwaarde}' in {self.naam}.")

    def get_value_by_label(self, label):
        try:
            return next(o for o in self.options if o.label == label)
        except StopIteration:
            raise ValueError(f"There is no option with label '{label}' in {self.naam}.")


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


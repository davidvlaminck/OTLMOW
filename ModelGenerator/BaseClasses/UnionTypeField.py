from ModelGenerator.BaseClasses.OTLField import OTLField


class UnionTypeField(OTLField):
    def __init__(self, naam, label, uri, definition, usagenote, deprecated_version, fieldsTuple, readonly=False,
                 readonlyValue=None):
        super().__init__(naam=naam, label=label, uri=uri, definition=definition, constraints=None, usagenote=usagenote,
                         deprecated_version=deprecated_version, readonly=readonly, readonlyValue=readonlyValue)
        self.fieldsTuple = fieldsTuple

    def __setattr__(self, name, value):
        if name == "waarde" and self.readonly and value is not None:
            raise AttributeError(f"can't set the value of a readonly attribute")
        if name == "waarde":
            if value is None:
                self.__dict__["waarde"] = value
                return
            correcttype = self.check_if_field_in_list(value)
            if not correcttype:
                raise TypeError(f'expecting correct type in {self.naam}. Correct types are of type {self.fieldsTuple}')
            self.__dict__["waarde"] = value
            return
        self.__dict__[name] = value

    def check_if_field_in_list(self, value):
        for field in self.fieldsTuple:
            if isinstance(value, field):
                return True
        return False

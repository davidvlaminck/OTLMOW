from OTLModel.Datatypes.OTLField import OTLField


class UnionTypeField(OTLField):
    def __init__(self, naam, label, uri, definition, usagenote, deprecated_version, fieldsTuple, readonly=False,
                 readonlyValue=None):
        super().__init__(naam=naam, label=label, uri=uri, definition=definition, constraints=None, usagenote=usagenote,
                         deprecated_version=deprecated_version, readonly=readonly, readonlyValue=readonlyValue)
        self.fieldsTuple = fieldsTuple
        self.actiefVeld = None

    def __getattribute__(self, name):
        if name == "waarde":
            return self.actiefVeld.waarde
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "waarde" and self.readonly and value is not None:
            raise AttributeError(f"can't set the value of a readonly attribute")
        if name == "waarde":
            if value is None:
                self.__dict__["waarde"] = value
                return
            if self.actiefVeld is None:
                raise RuntimeError('Use the method use_field() first to notify what field of the union type you want to use.')
            if not isinstance(value, type(self.actiefVeld)):
                raise ValueError(f'{value} is not of the correct type, expecting type of {type(self.actiefVeld)})')
            self.actiefVeld = value
            return
        self.__dict__[name] = value

    def use_field(self, fieldName):
        try:
            self.actiefVeld = next(f for f in self.fieldsTuple if f.naam == fieldName)
            self.waarde = self.actiefVeld.waarde
        except StopIteration:
            msg = f'{fieldName} is not a valid field name for this field. Use of the of the following instead: '
            for field in self.fieldsTuple:
                msg += field.naam + ', '
            msg = msg[:-1]
            raise ValueError(msg)

    def default(self):
        if self.actiefVeld is not None:
            return self.actiefVeld.waarde
        return None

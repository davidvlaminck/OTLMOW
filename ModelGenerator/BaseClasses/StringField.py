class StringField:
    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.name]
        except KeyError:
            return None

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'expecting string in {self.name}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

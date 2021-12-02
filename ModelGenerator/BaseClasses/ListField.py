class ListField:
    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.name]
        except KeyError:
            return None

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError(f'expecting list in {self.name}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
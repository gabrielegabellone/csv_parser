class FloatField:
    """
    `DescriptorClass` for handling `float` attributes with advanced features such as default and minimum values.
    """
    def __init__(self, default=None, min_value=None):
        """
        :param default: the default value that the field will have if one is not provided, default to `None`
        :param min_value: the minimum value that the field must have if provided, default to `None`
        """
        self._name = None
        self.default = default
        self.min_value = min_value

    def __get__(self, instance, owner) -> object:
        return instance.__dict__.get(self._name, self.default)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value: float) -> None:
        self.validate(value)
        instance.__dict__[self._name] = value

    def validate(self, value: float):
        if self.min_value and value < self.min_value:
            raise AttributeError(f'Value must be at least {self.min_value}')


class IntegerField(FloatField):
    """
    `DescriptorClass` for handling `int` attributes with advanced features such as default and minimum values.
    """
    def validate(self, value: float):
        super().__init__(value)
        if not value.is_integer():
            raise AttributeError('Value must be an integer')

from decimal import Decimal


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
        if instance is None:
            return f'{self.__class__.__name__}.{owner.__name__}'
        return instance.__dict__.get(self._name, self.default)

    def __set_name__(self, owner, name):
        """Dynamically sets the name of the attribute we use to store the value.

        :param owner: the ClientClass that uses the descriptor, in our case the `Product` class
        :param name: The name of the attribute corresponding to the instance of this DescriptorClass, in our case `price`
        """
        self._name = name

    def __set__(self, instance, value: float) -> None:
        self.validate(value)
        instance.__dict__[self._name] = value

    def validate(self, value: float):
        if self.min_value is not None and value < self.min_value:
            raise AttributeError(f'Value must be at least {self.min_value}')


class IntegerField(FloatField):
    """
    `DescriptorClass` for handling `int` attributes with advanced features such as default and minimum values.
    """
    def validate(self, value: int):
        super().validate(value)
        if not Decimal(value) % 1 == 0:
            raise AttributeError('Value must be an integer')

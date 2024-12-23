from .fields import FloatField, IntegerField


class Product:
    """
    Represents the abstraction of a product having a name, a description, a price and a quantity.
    """
    price = FloatField(min_value=0.05)
    quantity = IntegerField(min_value=0)

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @staticmethod
    def choose_name() -> str:
        """It takes care of receiving the product name as input.

        :return: The name of the product given in input
        """
        name = input('Enter the product name: ')
        return name

    @staticmethod
    def choose_description() -> str:
        """It takes care of receiving the product description as input.

        :return: The description of the product given in input
        """
        description = input('Enter a description: ')
        return description

    def choose_price(self):
        """
        It takes care of receiving the product price as input. Until an exception is raised in case of invalid value, an error message will be printed and an input value will be requested again.
        """
        while self.price is None:
            try:
                price = float(input('Insert a price: '))
                self.price = price
            except ValueError:
                print('You must enter a numeric value!')
            except AttributeError as a:
                print(a)

    def choose_quantity(self):
        """
        It takes care of receiving the product quantity as input. Until an exception is raised in case of invalid value, an error message will be printed and an input value will be requested again.
        """
        while self.quantity is None:
            try:
                quantity = float(input('Insert a quantity: '))
                self.quantity = quantity
            except ValueError:
                print('You must enter a numeric value!')
            except AttributeError as a:
                print(a)

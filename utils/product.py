from .fields import FloatField, IntegerField, StringField


class Product:
    """
    Represents the abstraction of a product having a name, a description, a price and a quantity.
    """
    name = StringField()
    description = StringField(blank=True)
    price = FloatField(min_value=0.05)
    quantity = IntegerField(min_value=0)

    # def __init__(self, description: str):
    #     self.description = description
    #
    # @staticmethod
    # def choose_description() -> str:
    #     """It takes care of receiving the product description as input.
    #
    #     :return: The description of the product given in input
    #     """
    #     description = input('Enter a description: ')
    #     return description

    def choose_name(self):
        while self.name is None:
            try:
                name = input('Enter the product name: ')
                self.name = name
            except AttributeError as a:
                print(a)

    def choose_description(self):
        while self.description is None:
            try:
                description = input('Enter a description: ')
                self.description = description
            except AttributeError as a:
                print(a)

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

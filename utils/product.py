from .fields import FloatField, IntegerField, StringField


class Product:
    """
    Represents the abstraction of a product having a name, a description, a price and a quantity.
    """
    name = StringField()
    description = StringField(blank=True)
    price = FloatField(min_value=0.05)
    quantity = IntegerField(min_value=0)

    def choose_name(self):
        """
        It takes care of receiving the product name as input. Until an exception is raised in case of invalid value,
        an error message will be printed and an input value will be requested again.
        Once a correct value is entered, it is set to the `name` attribute.
        """
        while self.name is None:
            try:
                name = input('Enter the product name: ')
                self.name = name
            except AttributeError as a:
                print(a)

    def choose_description(self):
        """
        It takes care of receiving the product description as input. Until an exception is raised in case of invalid value,
        an error message will be printed and an input value will be requested again.
        Once a correct value is entered, it is set to the `description` attribute.
        """
        while self.description is None:
            try:
                description = input('Enter a description: ')
                self.description = description
            except AttributeError as a:
                print(a)

    def choose_price(self):
        """
        It takes care of receiving the product price as input. Until an exception is raised in case of invalid value, an error message will be printed and an input value will be requested again.
        Once a correct value is entered, it is set to the `price` attribute.
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
        Once a correct value is entered, it is set to the `quantity` attribute.
        """
        while self.quantity is None:
            try:
                quantity = float(input('Insert a quantity: '))
                self.quantity = quantity
            except ValueError:
                print('You must enter a numeric value!')
            except AttributeError as a:
                print(a)

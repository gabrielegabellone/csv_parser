class InputProductNumber:
    minimum = 0
    initial_value = 0

    def is_a_valid_input(self, value) -> bool:
        return value >= self.minimum

    def enter_product_number(self) -> int:
        """
        It takes care of receiving a number of products as input, if the number is an integer it will be validated and
        returned. The input will be requested until a valid number is entered.
        :return: the entered number
        """
        product_number = self.initial_value
        validated_input = False

        while not validated_input:
            try:
                product_number = int(input('How many products do you want to insert in the csv? (0 to exit) '))
                if self.is_a_valid_input(product_number):
                    validated_input = True
                else:
                    print(f'{product_number} is not a valid input, you must enter a value greater than {self.minimum}')
            except ValueError:
                print('Invalid input! You must enter an integer.')

        return product_number

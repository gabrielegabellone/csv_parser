class InputProductNumber:
    @staticmethod
    def enter_product_number() -> int:
        """
        It takes care of receiving a number of products as input, if the number is an integer it will be validated and
        returned. The input will be requested until a valid number is entered.
        :return: the entered number
        """
        is_a_validated_input = False

        while not is_a_validated_input:
            try:
                product_number = int(input('How many products do you want to insert in the csv? '))
                is_a_validated_input = True
            except ValueError:
                print('Invalid input! Enter a numeric value.')

        return product_number

import csv
import datetime

from utils.input_product_number import InputProductNumber
from utils.product import Product


def get_filename() -> str:
    """
    Generate csv file name.

    :return: the filename
    """
    now = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
    filename = f'products_{now}.csv'
    return filename


def write_csv(products: list):
    """Takes care of writing a csv file containing the list of products passed as a parameter.
    The file is saved in the root.

    :param products: a list of `Product` instances
    """
    filename = get_filename()

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['name', 'description', 'price', 'quantity']

        writer.writerow(field)

        for product in products:
            writer.writerow([product.name, product.description, product.price, product.quantity])


def enter_products(number_of_products: int) -> list:
    """
    Receives user data as input for product insertion.

    :param number_of_products: the number of products to insert
    :return: a list of `Product` instances
    """
    products = []

    while len(products) < number_of_products:
        print(f'\nEnter product {len(products)+1}/{number_of_products}')

        p = Product()
        p.choose_name()
        p.choose_description()
        p.choose_price()
        p.choose_quantity()

        products.append(p)

    return products


def main():
    number_of_products = InputProductNumber().enter_product_number()
    if number_of_products == 0:
        quit()
    products = enter_products(number_of_products)
    write_csv(products)


if __name__ == '__main__':
    main()

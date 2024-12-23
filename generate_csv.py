import csv
import datetime
from utils.product import Product


def write_csv(products: list):
    """Takes care of writing a csv file containing the list of products passed as a parameter. A file `products_<timestamp>.csv` is saved in the root.

    :param products: a list of `Product` instances
    """
    now = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
    filename = f'products_{now}.csv'

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['name', 'description', 'price', 'quantity']

        writer.writerow(field)

        for product in products:
            writer.writerow([product.name, product.description, product.price, product.quantity])


if __name__ == '__main__':
    products_number = int(input('How many products do you want to insert in the csv? '))
    products = []

    while len(products) < products_number:
        print(f'\nEnter product {len(products)+1}/{products_number}')
        name = Product.choose_name()
        description = Product.choose_description()

        p = Product(name, description)
        p.choose_price()
        p.choose_quantity()

        products.append(p)

    write_csv(products)

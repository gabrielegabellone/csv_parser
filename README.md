# CSV Parser
Project with the aim of putting into practice an in-depth study I have done on the use of descriptors and generators in Python.  
I organized the project in two parts:
- a CSV parser, even if it actually deals with iterating and printing line by line, here I had the opportunity to put the generators into practice
- a CSV generator that instead allows you to manually generate the CSV by giving input information on products such as name, description, price and quantity, here instead I had the opportunity to experiment with the descriptors in order to be able to manage any input validations.

## How to run
### Install requirements
```
pip install -r requirements.txt
```

### CSV generation
First of all if you don't already have a CSV file or if you want to generate one you need to run the command:
```
python generate_csv.py
```

Once you run this command, you will be asked for the number of products you want to insert into the CSV and for each 
product you will be asked for the name, description, quantity and price:
```
How many products do you want to insert in the csv? 2

Enter product 1/2
Enter the product name: Mouse
Enter a description: a mouse for test purposes
Insert a price: 10
Insert a quantity: 1

Enter product 2/2
Enter the product name:
```
At the end you will find in the root of the project a csv file called `products` and followed by the date and time at the 
time of generation.

### CSV reading
To read a csv you will need to run the following command, where the `<path>` argument is the path to the csv file:
```
python main.py <path>
```

Each line of the csv will be printed in the terminal in **dict** format and preceded by the string `Processing`:
```
Processing {'name': 'Mouse', 'description': 'a mouse for test purposes', 'price': '10.0', 'quantity': '1.0'}
Processing {'name': 'PC', 'description': 'a PC', 'price': '300.0', 'quantity': '1.0'}

```

## What is a Descriptor?
Is an object whose attributes can be accessed through the methods of its protocol(`__get__()`, `__set__()`, `__delete__()`). 
The class that uses the features implemented by the descriptor is called **ClientClass**, while the class that implements 
the methods of the descriptor is called **DescriptorClass**. Therefore, in order to use the features of the DescriptorClass, 
the ClientClass must have a class attribute inside it, which will be an instance of the DescriptorClass.

### Practical Example
In the project I implemented a Product class and to manage those fields that would have advanced controls such as a minimum value I implemented the DescriptorClass **IntegerField** and **FloatField**.

```python
# utils/fields.py

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
        print('__get__ method call')
        return instance.__dict__.get(self._name, self.default)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value: float) -> None:
        print('__set__ method call')
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
```
```python
# utils/product.py

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
```

So to sum up:
- FloatField's `__get__` method will be called when we get the `price` attribute of a `Product` instance, while `__set__` when we assign them a value: 
  ```
  >>> p = Product(name='PC', description='')
  >>> p.price = 300
  __set__ method call
  >>> p.price
  __get__ method call
  300
  ```
- `__set_name__()` is another method of the protocol that takes care of dynamically setting the name of the attribute that we 
use to store the value. In our case it will set the `price` and `quantity` keys of the dict for instances of the `Product` class respectively.
- Descriptors are really useful when we want to have multiple attributes that share the same properties in different classes, 
in our example we could reuse an `IntegerField` or `FloatField` attribute multiple times in different classes without having 
to rewrite the same code multiple times.

## What is a Generator?
A `Generator` is a type of object that is returned by functions that return their value using the `yield` keyword. 
This allows you to instantiate `Generator` objects that produce a value when iterated. 
The advantage is that you can iterate and produce values when needed rather than having them all stored in memory.

### Practical Example
In the project I implemented the `csv_reader()` function which takes care of returning the lines of the csv file one at a time.

```python
import csv


def csv_reader(file_path: str):
    """It takes care of yielding the rows of a csv file.

    :param file_path: the path of the csv file to read
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row        
```

This allows you to instantiate a `Generator` object that will return the lines of the file when it is iterated.
````
>>> rows = csv_reader(file_path='example.csv')
>>> for r in rows:
...     print(r)
{'name': 'Mouse', 'description': 'a mouse for test purposes', 'price': '10.0', 'quantity': '1.0'}
{'name': 'PC', 'description': 'a PC', 'price': '300.0', 'quantity': '1.0'}
{'name': 'Desk', 'description': '', 'price': '80.0', 'quantity': '1.0'}
{'name': 'Pen', 'description': 'black pen', 'price': '1.5', 'quantity': '1.0'}
````

The advantage is that if for example, it is a file with many lines these will not be stored in memory in the variable 
`rows`, but will all be produced at the moment. 
It should be noted that the generator, by its nature, stops producing the values once the iteration has finished, 
so if we try to call the for loop on the variable rows again no value will be produced, in the same way if we call the 
function `next()` (a built-in function of iterators that returns the next value in an iteration we will get a `StopIteration` exception.

```
>>> for r in rows:
...     print(r)

>>> next(rows)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
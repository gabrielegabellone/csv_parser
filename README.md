# CSV Parser
Project with the aim of putting into practice an in-depth study I have done on the use of descriptors and generators in Python.  
I organized the project in two parts:
- a CSV parser, even if it actually deals with iterating and printing line by line, here I had the opportunity to put the generators into practice
- a CSV generator that instead allows you to manually generate the CSV by giving input information on products such as name, description, price and quantity, here instead I had the opportunity to experiment with the descriptors in order to be able to manage any input validations.

## What is a Descriptor?
Is an object whose attributes can be accessed through the methods of its protocol(`__get__()`, `__set__()`, `__delete()`). 
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
  p = Product(name='PC', description='')
  p.price = 300
  >> __set__ method call
  p.price
  >> __get__ method call
  >> 300
  ```
- `__set_name__()` is another method of the protocol that takes care of dynamically setting the name of the attribute that we 
use to store the value. In our case it will set the `price` and `quantity` keys of the dict for instances of the `Product` class respectively.
- Descriptors are really useful when we want to have multiple attributes that share the same properties in different classes, 
in our example we could reuse an `IntegerField` or `FloatField` attribute multiple times in different classes without having 
to rewrite the same code multiple times.
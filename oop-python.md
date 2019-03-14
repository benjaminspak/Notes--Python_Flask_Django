# Object Oriented Python

#### Key Terms
+ Classes - are the blueprints of objects.
+ Method - a function defined within a class.
+ Instance - the result of using, or calling, a class.
+ Attribute - the name for a variable that belongs to a class.

#### Reminders
+ Instances are responsible for their own attribute values.
+ 

#### Instanciation

```python
class Student:
    name = 'Benjamin'

me = Student()  # New instance of the Student class
print(me.name)  # You can call the class attributes against the new instance.
```

+ Methods in classes, are the actions that the instances of your class can do.
+ Methods are functions that belong to a class.
    + Whenever methods are used, they are used by an instance of a class, rather than the actual class itself.
    + Because of this, methods take at least, one parameter - which represents the instance that's using the method.
    + By convention, that parameter is always called 'self'.

#### Simple Method Example

```python
class Student:
    name = 'Your name'

    def praise(self):
        return 'Hello ' + self.name


```

#### Int Example - With Arg

```python
class Student:
    name = 'Your name'

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        if grade <= 50:
            return self.reassurance()

```

#### Accepting KWargs as for Attributes

```python
"""
Accept keyword arguments and assign them as attributes to predefined attribute variables.
"""
class Animal:
    def __init__(self, **kwargs):
        self.species = kwargs.get("species")
        self.age = kwargs.get("age")
        self.sound = kwargs.get("sound")
```


#### Automatically Executed Class Example

```python
"""
setattr(object, name, value)
This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value.
# The string may name an existing attribute or a new attribute.
# The function assigns the value to the attribute, provided the object allows it.
# For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
"""

import random

class Thief:
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        self.name = sneaky
        self.sneaky = sneaky

        for key, value in kwargs.items():
            setattr(self, key, value)

    def pickpocket(self):
        if self.sneaky:
            return self.sneaky and bool(random.randint(0, 1))
        return False

    def hide(self, light_level):
        return self.sneaky and light_level < 10

```

#### Allowing users to assign more attributes

```python
"""
Defining args allows you to set attributes. However, it does not allow you to pass kwargs in the future unless the attribute is already defined.
"""

class Animal:
    def __init__(self, **kwargs):
        self.species = kwargs.get("species")
        self.age = kwargs.get("age")
        self.sound = kwargs.get("sound")

>>> wolf = Animal(species="Canus Lupus", age=5, sound="howl", color="grey")
>>> wolf.species
"Canus Lupus"

>>> wolf.color
AttributeError
```

```python

"""
Using the setattr() method we can avoid kwarg issues with attributes that are not set prior to passed via and instance.
"""

class Animal:
    def __init__(self, name, **kwargs):
        self.name = name
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)

```

#### Overriding what happens when a new class is instantiated
+ Create an  __init__ method

#### Subclasses & inheritance

```python

class Inventory:
    def __init__(self):
        self.slots = []
    
    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
    pass
```

#### Superperlative functions / super

```python

"""
When you user super, you have to call the method name, and it's required arguments too.
"""

class Theif(Character):
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        # Sub classes can take different arguments than their parent classes.
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

```

### Special Methods (@property method)

```python
"""
With @property you can access the property, but not set an attribute.
For example: (small.radius) will return a value. But, you can't set a value like small.radius = 10. You will get an attribute error.
"""

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

small = Circle(10)
print(small.diameter)  # 10
print(small.radius)  # 5
```
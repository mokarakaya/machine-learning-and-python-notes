# `__call__` Function

```
class A:
  def __call__(self):
    return 10

a = A()
a()
```

- `__call__` allows objects to be called just like functions.

# `@classmethod` Annotation

```
class InputData:

    def __init__(self, value):
        self.value = value

    def read(self):
        raise NotImplementedError

class DayInputData(InputData):
    def __init__(self, value):
        super().__init__(value)

    def read(self):
        return self.value

    @classmethod
    def from_day(cls, day):
        value = 7
        if day == 'Monday':
            value = 1
        elif day == 'Tuesday':
            value = 2
        return cls(value)


a = DayInputData.from_day('Tuesday')
print(a.read())
a = DayInputData(2)
print(a.read())
```

- `@classmethod` allows us to overload the constructor. We can either crate `DayInputData` object by using the `__init__` function for `from_day` function.


# `super()` Method Resolution Order (MRO)

```
class Base:
    def __init__(self, value):
        self.value = value

class TimesTwo(Base):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 2

class PlusFive(Base):
    def __init__(self, value):
        super().__init__(value)
        self.value += 5

class Math(TimesTwo, PlusFive):
    def __init__(self, value):
        super().__init__(value)

class Math2(PlusFive, TimesTwo):
    def __init__(self, value):
        super().__init__(value)

a = Math(3)
print(a.value)
b = Math2(3)
print(b.value)

16
11
```

- Parent classes executed from right to left. So `Math` calls `PlusFive` first, and `Math2` class `TimesTwo` first.

# `mix-in` Classes

```
class PrintMe:
    def print_me(self):
        print('printing:', self.value)


class Math(PrintMe):
    def __init__(self, value):
        self.value = value

    def calc(self):
        self.print_me()

a = Math(3)
a.calc()
```

- `mix-in` classes do not define their own `__init__` functions or attributes.
- We can use `mix-in` classes instead of multiple inheritance. It is especially useful when we need to inherit several classes.


# Private Attributes

- `self.__private_field = 10`
- We can not reach private field from outside of the class by calling dot (`.`). Child classes can not also reach these variables.
- `@classmethod` can reach the private variable. We can also reach the private variable by using `__dict__` or the key of the attribute in `__dict__`.


# `collections.abc` for Custom Container Types

- `collections.abc` has a set of abstract base classes and it provides many typical methods. As an example `from collections.abc import Sequence`  has methods for sequences (e.g. `list`) such as `index`, `count` etc. We can use `Sequence` when we create a new class which inherits a sequence e.g. `list`.

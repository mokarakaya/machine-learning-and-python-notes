# Integer Division
- `Python2`: `3 / 2` -> 1
- `Python3`: `3 / 2` -> 1.5

# Xrange
- Lazy evaluation range function xrange in Python2 does not exist in Python3.

# Raising Exceptions

- `Python2`: `raise IOError, "file error"`
- `Python2 and Python3`:`raise IOError("file error")`

# Handling exceptions
- `Python2`: `except NameError, err:`
- `Python3`: `except NameError as err:`

# The next() function and .next() method

- `Python2`: `my_generator.next()`
- `Python2 and Python3`: `next(my_generator)`

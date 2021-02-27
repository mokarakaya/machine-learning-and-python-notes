# Ternary Operators

- `'hello' if True else 'world'`

# `*args` and `**kwargs`

- `*args` to get list of attributes by an order.
- `**kwargs` to get list of attribute tuples with key and value. `for key, value in kwargs.items(): `

# `re` module for Regular Expressions

```
re.search('o', 'worldo')
<_sre.SRE_Match object; span=(1, 2), match='o'>


re.findall('o', 'worldo')
['o', 'o']

list(re.finditer('o', 'worldo'))
[<_sre.SRE_Match object; span=(1, 2), match='o'>, <_sre.SRE_Match object; span=(5, 6), match='o'>]

```

- Returns None if there is no  match.

- `split()`: This method is used to split a given string into a list.
- `sub()`: This method is used to find a substring where a regex pattern matches, and then it replaces the matched substring with a different string.
- `subn()`: This method is similar to the sub() method, but it returns the new string, along with the number of replacements.

# Built-in

- `Built-in modules`: os, sys, math, random etc.
- `Built-in types`: Integers, floating-point, complex numbers, strings, boolean, built-in functions.

# Data Structures
- dictonaries, lists, sets, tuples, strings. Strings and tuples are immutable.

# Access specifier
- Python uses `_` and `__`
- According to PEP-8 `_` means variable of function is intended to be used internally, but there is no restriction applied.
- `__` means private and we can not access.

# `try:` `except` `else:`
- Else block is executed if there is no error.

# `is` and `==`

- `is` checks identity and `==` check equality.
- `[1,2] == [1,2]` -> True
- `[1,2] is [1,2]` -> False


# Python is Call by Reference

```
a = [1,2,3]
s = 'test'
def test(b, c):
    b.append(4)
    print(a is b)
    print(c is s)
    c = 'k'
    print(c is s)


test(a, s)
print(a, s)

prints:
True
True
False
[1, 2, 3, 4] test

```

- When you pass an immutable object as an argument - for instance a number, a string, a tuple; it appears to be similar to ‘Call by value’ - in that the function can change the parameter name that was passed, but the actual value wont change in the function caller.; but it doesn’t change because it is immutable, and any attempt to change the object will actually create a new object with the new value.

# List Operations

- `'cat' * 3` -> 'catcatcat'
- `[1,2,3] * 2` -> [1, 2, 3, 1, 2, 3]
- `np.array([1,2,3]) * 2` -> array([2, 4, 6])
- `a = [1,2], b = [3,4]` then `a + b` -> [1, 2, 3, 4]  
- `a = np.array([1,2]), b = np.array([3,4])` then `a + b` -> [4, 6]  
- `a = np.array([1,2]), b = np.array([3,4])` then `np.concatenate([a,b])` -> [1, 2, 3, 4]


# Module vs Package

- While a module is a single Python file, a package is a directory of Python modules containing an additional `__init__.py` file, to distinguish a package from a directory that just happens to contain a bunch of Python scripts.


# .append vs .extend

```
a = [1,2,3]
b = [1,2,3]
a.append(6)
print(a)
#=> [1, 2, 3, 6]
b.extend([4,5])
print(b)
#=> [1, 2, 3, 4, 5]

```

# Stack and Queue

- Use list and `pop()` for stack (FILO)  behavior
- Use list and `pop(0)` for queue (FIFO)  behavior

```
a = [2,4,6]
a.pop() -> 6
a = [2,4,6]
a.pop(0) -> 2
```

## Deque

- We can also use `deque` for the same behavior.
- `pop()` is for stack, and `popleft()` is for queue.

```
from collections import deque
a = deque()
a.extend([2,4,6])
a.pop() -> 6

a = deque()
a.extend([2,4,6])
a.popleft() -> 2

```

# Check numbers and letters in a string

- `'123a'.isnumeric()`: Check if a string only contains numbers.
- `'123a'.isalpha()`: Check if a string only contains letters.
- `'123abc...'.isalnum()`:  Check if a string only contains numbers and letters.


# Delete from array

- `x = ['a', 'b']`
  - `x.remove('b')` -> ['a']
  - `del(x[1])` -> ['a']
  - `x.pop(1)` -> ['a'], and returns 'b'
- `x = np.array(['a', 'b'])`
  - `np.delete(x, [1])` -> returns ['a'] np array and does not change x
  - `np.delete(x, np.where(x == 'b'))` -> returns ['a'] np array and does not change x.


# Pickle

```
import pickle

example_dict = {1:"6",2:"2",3:"f"}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()


pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)

```

# Dynamically and Strongly typed
- Python is strongly typed and `"1" + 2 ` will throw `TypeError`. Javascript is weakly typed.
- Python is dynamically typed, and data types are checked during execution.

# Pyc files
- These are created by the Python interpreter when a .py file is imported, and they contain the "compiled bytecode" of the imported module/program, the idea being that the "translation" from source code to bytecode (which only needs to be done once) can be skipped on subsequent imports if the .pyc is newer than the corresponding .py file, thus speeding startup a little. But it's still interpreted.
- The default implementation of the Python programming language is CPython which is written in the C programming language. CPython compiles the python source code into the bytecode, and this bytecode is then executed by the CPython virtual machine.

# Memory Management
- Memory management in Python is handled by the Python Memory Manager. The memory allocated by the manager is in form of a private heap space dedicated for Python. All Python objects are stored in this heap and being private, it is inaccessible to the programmer. Additionally, Python has an in-built garbage collection to recycle the unused memory for the private heap space.

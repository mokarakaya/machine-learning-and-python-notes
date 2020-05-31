# Slicing

```
a[:]      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:5]     # ['a', 'b', 'c', 'd', 'e']
a[:-1]    # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
a[4:]     #                     ['e', 'f', 'g', 'h']
a[-3:]    #                          ['f', 'g', 'h']
a[2:5]    #           ['c', 'd', 'e']
a[2:-1]   #           ['c', 'd', 'e', 'f', 'g']
a[-3:-1]  #                          ['f', 'g']
```
- Slicing does not return index out of range error.

# Stride

```
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

>>>
['red', 'yellow', 'blue']
['orange', 'green', 'purple']
```

```
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x[::2]   # ['a', 'c', 'e', 'g']
x[::-2]  # ['h', 'f', 'd', 'b']
```

- Avoid using slicing and striding in a single line.

# Catch-all unpacking

```
first, *middle, last = [1, 2, 3, 4]
```

- We can use * anywhere, but we can not use it twice.

# Sort

```
power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

power_tools.sort(key=lambda x: (x.weight, x.name))
```

- First sorts by weight, and then name.
- To sort in reverse order, we can either use `reverse=True` or `-x.weight`.


# Insertion Ordering

- In Python 3.5 and before, iterating over a dict would return keys in arbitrary order

- `OrderedDict` has similar behavior as `dict` (since Python 3.7), but `OrderedDict`.

```
a = {'x':1}
b = OrderedDict(sorted(a.items(), key=lambda t: t[0]))
b.popitem(last=True)

```

# Handle Missing Directory keys

- `counters.get(key, 0)` returns default value `0` if the key is missing.
- `counters.setdefault(key, 0)` behaves similar to `get`, but it also sets the default value to use later.
- `setdefault` always returns the same object. `get` returns a new object if the object is created in the expression.
- We can also check first with `in` but it requires two times access.

# `__missing__` for Default Values

```
class MyDict(dict):
    def __missing__(self, key):
        return set()
```
- The class above will create a new `set()` for each missing value.

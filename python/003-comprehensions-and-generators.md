# Assignment Expressions in Comprehensions

```
found = {name: batches for name in order
         if (batches := get_batches(stock.get(name, 0), 8))}
```
- In Python 3.8 and later, it is possible to use assignment expression in if-condition (`:=`). We do not need to calculate `batches` twice.

# Generators

- We can create generator functions by using `yield`. The generator function does not immediately run, but it returns an iterator to calculate result when we call `next` on the iterator.

- We can choose to use generators when we have large inputs, and generator functions are sometimes easier to read.

# Iterating over Arguments

- An iterator produces its results only a single time.
- Expressions which needs loops (e.g. for, sum etc.) calls `iter` built-in function, and `iter` calls `__iter__` function of the object. The function should return an iterator. We can implement `__iter__` function by using generators.

```
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
```

- Whenever we iterate over an object of `ReadVisits`, a new iterator will be created. So, iterator will not be exhausted when it is called for the second time. The disadvantage is that the function needs to read the file twice.

# Generator Expressions for List Comprehensions

```
it = (len(x) for x in open('my_file.txt'))
```

- `it` is a generator object that we can iterate. It helps to alleviate memory issues when the file is large.

```
roots = ((x, x**0.5) for x in it)
```
- We can combine two generators.


# Multiple Generators with `yield from`

```
def child():    
  for i in range(1_000_000):
    yield i

def slow():
  for i in child():
    yield i

def fast():
  yield from child()
```

- `yield from` expression allows you to compose multiple nested generators.
- `yield from` has better performance than manually iterating in the generator function.

```
  def double_inputs():
    while True:
      x = yield
      x * 2
```

# Generators with `send`, and `throw`

- We can inject data to the generator function by using `send`, but injecting an iterator input to the composed generator is better, and we should avoid using `send` function.

- We can also send exceptions to the generator function by using `throw`.

# `itertools` for Iterators and Generators

- We use `itertools` functions for linking, filtering, and producing combinations.

- `chain`: combine multiple iterators into one.
  - `it = itertools.chain([1, 2, 3], [4, 5, 6])`
- `repeat`: repeats a single value in an iterator `n` times.
  - `it = itertools.repeat('hello', 3)`
- `cycle`: cycles the iterator forever.
  - `it = itertools.cycle([1, 2])`
- `tee`: creates multiple parallel iterators.
  - `it1, it2, it3 = itertools.tee(['first', 'second'], 3)`
- `zip_longest`: a version of `zip`, but it uses all elements in the longest list.
  - `it = itertools.zip_longest(keys, values, fillvalue='nope')`. `keys`, and `values` have different sizes.
- `islice`: filters an iterator by using standard slicing, and striding.    
  - `first_five = itertools.islice(values, 5)`.
- `takewhile`: returns items until the predicate is false.
  - `it = itertools.takewhile(lambda x: x <= 3, [1,2,3,4,5])` (returns first 3)
- `dropwhile`: skips items until the predicate returns `False` for the first time. Opposite of `takewhile`.
  - `it = itertools.dropwhile(lambda x: x <= 3, [1,2,3,4,5])` (returns 4,5)
- `filterfalse`: Opposite of `filter`. Returns items where the predicate returns `False`.
  - `itertools.filterfalse(lambda x: x <= 3, [1,2,3,4,1])`  (returns 4)
- `accumulate`: similar to `reduce` but return a iterator for each step.  
  - `itertools.accumulate( [1,2,3,4], lambda x,y: x* y )` (returns [1, 2, 6, 24])
- `product`: returns a Cartesian product of items.
  - `itertools.product([1, 2], repeat=2)` returns `[(1, 1), (1, 2), (2, 1), (2, 2)]`
  - `itertools.product([1, 2], ['a', 'b'])` returns `[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]`
- `permutations`: Returns permutations of the input.
  - `itertools.permutations([1, 2, 3, 4], 2)` length is 12.
- `combinations`: Returns combinations the input.
  - `itertools.combinations([1, 2, 3, 4], 2)` length is 6.
- `combinations_with_replacement`: Similar to `combinations` but repeated values are allowed.
  - `itertools.combinations_with_replacement([1, 2, 3, 4], 2)` length is 10.

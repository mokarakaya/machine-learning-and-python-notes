-  Unlike Python lists, NumPy is constrained to arrays that all contain the same type. It is also possible to force to create a Python array with the same type `array.array('i', L)`

# Creating Arrays from Scratch
- `zeros`
- `ones`:  np.ones((3, 5), dtype=float)
- `full`:
- `arange`: np.arange(0, 20, 2) -> array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
- `linspace`: np.linspace(0, 1, 5) -> array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
- `random.random`
- `random.normal`: np.random.normal(0, 1, (3, 3)) -> Create a 3x3 array of normally distributed random values with mean 0 and standard deviation 1.
- `random.randint`
- `eye`:  np.eye(3) ->  Create a 3x3 identity matrix.

# Numpy Datatypes
- `bool_`: One byte
- `int_`: Default integer type (same as C long; normally either int64 or int32.Depends on the platform. type is inherited from the C compiler of the platform. The inherited type in C is long.)
- `int8`: Byte (–128 to 127)
- `int16`: Integer (–32768 to 32767)
- `int32`: Integer (–2147483648 to 2147483647)
- `int64`: Integer (–9223372036854775808 to 9223372036854775807)
- `uint8`: Unsigned integer (0 to 255)
- `uint16`: Unsigned integer (0 to 65535)
- `uint64`: Unsigned integer (0 to 18446744073709551615)
- `float_`: Shorthand for float64
1101.234 -> 1101 is exponent and 234 is mantissa
- `float16`: Half-precision float: sign bit, 5 bits exponent, 10 bits mantissa
- `float32`: Single-precision float: sign bit, 8 bits exponent, 23 bits mantissa
- `float64`: Double-precision float: sign bit, 11 bits exponent, 52 bits mantissa
- `complex_`: Shorthand for complex128
- `complex64`: Complex number, represented by two 32-bit floats
- `complex128`: Complex number, represented by two 64-bit floats

# NumPy Array Attributes
- `x = np.random.randint(10, size=(3, 4, 5)) `
  -  `x.ndim`: 3
  - `x.shape`: (3, 4, 5)
  - `x.size`: 60
  - `x.dtype`: int64
  - `x.itemsize`: 8 bytes
  - `x.nbytes`: 480 bytes.

# Accessing Subarrays
- `x[start:stop:step]`
-  Numpy subarrays return views rather than copies of the array data. This is one area in which NumPy array slicing differs from Python list slicing: in lists, slices will be copies.

# Array Concatenation

- `x = np.array([1, 2, 3])`, `y = np.array([3, 2, 1])`
  -  `np.concatenate([x, y])`: array([1, 2, 3, 3, 2, 1])
- `grid = np.array([[1, 2, 3], [4, 5, 6]])`
  - `np.concatenate([grid, grid])`: array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]) `vstack` also returns the same output.
  -  `np.concatenate([grid, grid], axis=1)`:  array([[1, 2, 3, 1, 2, 3], [4, 5, 6, 4, 5, 6]]), `hstack` also returns the same output.
  - `np.dstack` will stack arrays along the third axis.

# Array Splitting

- `x = [1, 2, 3, 99, 99, 3, 2, 1]`
  - `np.split(x, [3, 5])`: [1 2 3] [99 99] [3 2 1]
- `grid = np.arange(16).reshape((4, 4))`
  - `np.split(grid, [2])` or `np.vsplit(grid, [2])`:[[0 1 2 3] [4 5 6 7]] [[ 8  9 10 11] [12 13 14 15]]
  - `np.split(grid, [2], axis=1)` or `np.hsplit(grid, [2])`:[[ 0  1] [ 4  5] [ 8  9] [12 13]] [[ 2  3] [ 6  7] [10 11] [14 15]]
- `np.dsplit` will split arrays along the third axis.

# UFuncs
- Python loops with default interpreter CPython is slow. There are other options such as PyPy (just-in-time compiler), Cython (converts Python code to compilable C code), Numba (converts snippets of Python code to fast LLVM bytecode)
- Vectorized operations in NumPy are implemented via ufuncs, whose main purpose is to quickly execute repeated operations on values in NumPy arrays

## Aggregate UFuncs
- `x = np.arange(1, 6)`
  - `np.add.reduce(x)`: 15
  - `np.add.accumulate(x)`: array([ 1,  3,  6, 10, 15]) Keeps outputs of the intermediate operations
  - multiply, subtract, divide are also available

## Outer UFunc
- Outputs all pairs of two inputs
- `x = np.arange(1, 4)`
  - `np.multiply.outer(x,x)`: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# Aggregations

- np.sum is faster than Python sum() on Numpy objects. Python sum is faster on python objects. Also applicable to min, and max.
- np.sum, np.min, and np.max have axis (0,1,..) attribute to calculate on axises.
- These functions also have nan versions e.g. `nansum`, and they are nan-safe.
- Other aggregation functions: `prod` (multiply all elements), `mean`, `std`, `var`, `argmin`, `argmax`, `median`, `percentile`, `any`, `all`.
- `np.any(x < 3)`:  x is an np array, and `x<3` return a list of boolean for each element in the array.

# Broadcasting Rules
- Numpy applies three rules to determine the interaction between two arrays.
  - Rule 1: If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side.
  - Rule 2: If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
  - Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

- Example 1: original: `M.shape = (2, 3), a.shape = (3,)`
  - converted to: `M.shape -> (2, 3), a.shape -> (1, 3)`
  - converted to: `M.shape -> (2, 3) a.shape -> (2, 3)`
  - output for `M + a` will have shape `(2,3)`

- Example 1: original: `a.shape = (3, 1) b.shape = (3,)`
  - converted to: `a.shape -> (3, 1), b.shape -> (1, 3)`
  - converted to: `a.shape -> (3, 3), b.shape -> (3, 3)`
  - output for `a + b` will have shape `(3,3)`

- Example 3: original: `M.shape = (3, 2), a.shape = (3,)`
  - converted to: `M.shape -> (3, 2), a.shape -> (1, 3)`
  - converted to: `M.shape -> (3, 2), a.shape -> (3, 3)`
  - Will rise ValueError since shapes are compatible to broadcast.

# Axis
- We can think axis as the collapsed dimension:
  - `a.shape -> (10,3)` then `a.sum(axis=0)` will return an array with 3 values
  - `a.shape -> (10,3)` then `a.sum(axis=1)` will return an array with 10 values

#  Binning Data
- `x = np.random.randn(100)`:  “standard normal” distribution.
- `bins = np.linspace(-5, 5, 20)` 20 bins between -5 and 5.
- `counts = np.zeros_like(bins)` arrays with zeros with shape of bins.
- `i = np.searchsorted(bins, x)` returns the bin ids.
- `np.add.at(counts, i, 1)` return the size of each bin.

# Sorting
- `np.sort`, `np.argsort`
- `a.sort()` sorts in-place.
- `np.sort(X, axis=0)`: sort each column
- `np.sort(X, axis=1)`: sort each row

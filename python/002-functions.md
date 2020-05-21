# Scope order
- Interpreter looks for a variable in following scope;


1. Current function
2. Any enclosing scopes (such as other containing functions).
3. The scope of the module that contains the code (also called the global scope).
4. The built-in scope (that contains functions like len and str).

```
found =1
def call_closure():
    found = 2
    def helper():
        #nonlocal found # Added
        # global found
        found = 3
    helper()
    print(found)
print(found)
```
- By default -> prints 2, 1
- When `nonlocal` enabled ->  prints 3,1. `nonlocal` reaches enclosing scopes. `nonlocal` does not reach global scope, if there is no attribute in enclosing scope.
- When `global` enabled ->  prints 2,3. `global` reaches global scope.

# Positional Arguments and Keyword Arguments

- \*  used for positional arguments.
- \** used for keyword arguments.
- Name of the argument is the keyword. `def a(b)`
- We can also give a default value if `b` is optional `def a(b=None)`

# Keyword-only and Position-only Arguments

```
def a(b, *, c=False):
 pass
```
- `c` is still optional but it is keyword-only.


```
def a(b, /, *, c=False):
 pass
```
- `b` is a positional-only argument.
- Python 3.8 and higher has positional-only arguments.


# Function Decorators

```

def trace(func):
 def wrap(*args, **kwargs):
    print('calling with', args, kwargs)
    result = func(*args, **kwargs)
    print('returns', result)
    return result
 return wrap


@trace
def next_me(i):
    return i + 1

b = next_me(1)
print(b)

```

- will print;
```
calling with (1,) {}
returns 2
2
```

# Counting Methods

- `Factorial`: `n! = n x (n -1) x (n — 2) x … x 2 x 1`

Use when the number of items is equal to the number of places available.

Eg. Find the total number of ways 5 people can sit in 5 empty seats.
= 5 x 4 x 3 x 2 x 1 = 120

- `Fundamental Counting Principle` (multiplication)

This method should be used when repetitions are allowed and the number 
of ways to fill an open place is not affected by previous fills.

Eg. There are 3 types of breakfasts, 4 types of lunches, and 5 types of desserts. 
The total number of combinations is = 5 x 4 x 3 = 60

- `Permutations`: `P(n,r)= n! / (n−r)!`

This method is used when replacements are not allowed and order of item ranking matters.

Eg. A code has 4 digits in a particular order and the digits range from 0 to 9. How many permutations are there if one digit can only be used once?
P(n,r) = 10!/(10–4)! = (10x9x8x7x6x5x4x3x2x1)/(6x5x4x3x2x1) = 5040

- `Combinations Formula`: `C(n,r)=(n!)/[(n−r)!r!]`

This is used when replacements are not allowed and the order in which items are ranked does not mater.

Eg. To win the lottery, you must select the 5 correct numbers in any order from 1 to 52. What is the number of possible combinations?
C(n,r) = 52! / (52–5)!5! = 2,598,960
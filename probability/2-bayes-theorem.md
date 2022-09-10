- There are three types of players in a tournament (A, B, C) and the percentage of each type is:
```
A = 50%
B = 25%
C = 25%
```
- Your probability to win a match against each type is:
```
0.3 against A
0.4 against B
0.5 against C
```

- Q1: If you play a match in this tournament, what is the probability of your winning the match?

```
P[A] = 0.5
P[B] = 0.25
P[C] = 0.25

P[W|A] = 0.3
P[W|B] = 0.4
P[W|C] = 0.5

P[W] = P[W|A] P[A] + P[W|B] P[B] + P[W|C] P[C]
P[W] = (0.3)(0.5) + (0.4)(0.25) + (0.5)(0.25) = 0.375
```
- Q2: Supposing that you have won a match, what is the probability that you played against an A player?
```
P[A|W] = (P[W|A] P[A]) / P[W]
P[A|W] = (0.3 0.5) / 0.375 = 0.4
```
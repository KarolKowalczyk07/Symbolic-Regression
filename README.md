# Symbolic-Regression
Symbolic Regression searches different mathematical expressions in order to best fit a set of data.
To do this, a binary tree with a depth of 9 was used to store all parts of the expression.
The following operators were used: +, -, *, /, sin, cos, x (variable).
A Random Search, Random Mutational Hill Climber (adding a small float), and Genetic Algorithm (swapping tree branches among individual solutions) were used to best fit the data.
Expressions were saved as strings (for evaluation) and arrays (to allow swapping tree branches between individuals for GA).

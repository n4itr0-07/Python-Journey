import math
import latexify

@latexify.with_latex

def solve(a, b, c):
    return(-b + math.sqrt(b**2 - 4*a*c)) / (2*(a+b))

solve(1, 2, 1) # This Module is only for python 3.11

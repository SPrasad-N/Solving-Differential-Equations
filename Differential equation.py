import sympy as sy
from sympy import *
from sympy.interactive import printing

x = sy.Symbol("x")
y = sy.Function("y")(x)
f = Eq(y.diff(x,x)+2*y.diff(x)-9,sy.sin(x))
pprint(f)
pprint(dsolve(f),y)
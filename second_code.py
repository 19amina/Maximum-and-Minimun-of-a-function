from sympy import *
x = Symbol('x', real = True)
f = 2*x**3 + 3*x**2 - 36*x - 10
first_der = f.diff(x)
l = solve(first_der, x)
x1 = l[0]
x2 = l[1]
second_der = f.diff(x).diff(x)
second_der_for_x1 = second_der.subs(x, x1)
second_der_for_x2 = second_der.subs(x, x2)

maximum_for_x = 0
minimum_for_x = 0
if second_der_for_x1 < 0:
  maximum_for_x = x1
  minimum_for_x = x2
elif second_der_for_x1 > 0:
  maximum_for_x = x2
  minimum_for_x = x1
elif second_der_for_x2 < 0:
  maximum_for_x = x2
  minimum_for_x = x1
elif second_der_for_x2 > 0:
  maximum_for_x = x1
  minimum_for_x = x2

first_der_for_y1 = f.subs(x, minimum)
first_der_for_y2 = f.subs(x, maximum)
	 
minimum_dot = [minimum, first_der_for_y1]
maximum_dot = [maximum, first_der_for_y2]
	 
print(minimum_dot)
print(maximum_dot)

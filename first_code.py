import math
from math import e
number1 = (math.sqrt(5) – 1) / 2
number2 = (3 - math.sqrt(5)) / 2
	 
def golden_section (f, a, b, tol = 1e-5, h = None, c = None, d = None, fc = None, fd = None):
  print(a, b, c, d, fc, fd)
  (a, b) = (min(a, b), max(a, b))
  if h is None: h = b – a
  if h <= tol:
    return (a, b)
  if c is None:  c = a + number2 * h
  if d is None:  d = a + number1 * h
  if fc is None:  fc = f(c)
  if fd is None: fd = f(d)
  if fc < fd:
    return golden_section(f, a, d, tol, h*number1, c = None, fc = None, d = c, fd = fc)
  else:
    return golden_section(f, c, b, tol, h*number1, c = d, fc = fd, d = None, fd = None)
    
f = lambda x: e**((x-2)**2)
a = -5
b = 5
(c, d) = golden_section(f, a, b)
print(f((c + d)/2))

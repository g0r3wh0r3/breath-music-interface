from math import pi
c = 3.3E-6
period = 12.2E-9
f = 1/period 
print(f)
sqrt_lc = 1/(2*pi*f)
print(sqrt_lc)
lc = sqrt_lc**2 
print(lc)
l = lc/c

print(l)
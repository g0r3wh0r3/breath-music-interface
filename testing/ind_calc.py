from math import pi
# calculates the inductance from the frequency 
freq = float(input())
#period = float(input())
#freq = 1/period
C = 3.3E-6 # capacitor val 
L = 1/((2*pi*freq)**2**C)
print(L)
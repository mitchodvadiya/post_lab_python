
# ------------------------------------------------------------------------------------------------------------
# Post Lab Exercise:

# 1. Using Python, compute the Z-transform of the sequence x[n]=3^n u[n].
import sympy as sp 
# Define symbols
n, z, a = sp.symbols('n z a')
# Define the signal x[n] = a^n * u[n]
x_n = 3**n
# Compute the Z-transform
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# Print the result
print("Z-transform of x[n] = a^n u[n]:")
sp.pprint(X_z, use_unicode=True)


# 2 : Using Python, compute the Z-transform of the sequence x[n]=cos⁡(wn)u[n]. 
import sympy as sp
# Define symbols
n, z, omega = sp.symbols('n z omega')
# Define the sinusoidal sequence x[n] = cos(omega * n) * u[n]
x_n = sp.cos(omega * n)
# Compute the Z-transform
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# Print the result
print("Z-transform of x[n] = cos(omega * n) u[n]:")
sp.pprint(X_z, use_unicode=True)

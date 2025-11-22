# post lab 19
# -------------------------------------------------------------------------------------------------------------------
# 1 code :
import numpy as np
def z_transform_unit_step(N=20):
 
    z = 0.8  # example test value inside ROC
    U = 0

    for n in range(N):
        U += z**(-n)

    return U

def check_stability(poles):

    for p in poles:
        if abs(p) >= 1:
            return "System is Unstable"
    return "System is Stable"

print("Z-transform (approx) of unit step:", z_transform_unit_step())

unit_step_poles = [1]
print("Unit step system stability:", check_stability(unit_step_poles))


# 2 code :
# import numpy as np
def system_stability_Hz():
    # Given poles and zeros
    zeros = [0.7, 0.9]
    poles = [0.6, 0.4]

    # Print them
    print("Zeros of H(z):", zeros)
    print("Poles of H(z):", poles)

    # Stability check
    for p in poles:
        if abs(p) >= 1:
            return "The system is Unstable"

    return "The system is Stable"


# Run program
print(system_stability_Hz())
  
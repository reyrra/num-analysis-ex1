import numpy as np

def f(x):
    return 1 / np.sqrt(-np.log(x))

h = 0.01

n = int(1/h)

integral_midpoint = 0
for i in range(n):
    x_mid = (i + 0.5) * h  
    midpoint_value = f(x_mid)  
    integral_midpoint += midpoint_value * h
    print(f"Step {i+1}: x_mid = {x_mid}, f(x_mid) = {midpoint_value}, Partial Integral = {integral_midpoint}")

exact_integral = np.sqrt(np.pi)

error = abs(integral_midpoint - exact_integral)


print(f"\nApproximated Integral using Midpoint Method: {integral_midpoint}")
print(f"Exact Integral Value: {exact_integral}")
print(f"Error: {error}")

def f(x):
    return x**2 - (1 - x)**5

def f_prime(x):
    return 2*x + 5*(1 - x)**4

def f_double_prime(x):
    return 18*x**2 - 80*x + 80

def newton_raphson_method(f, f_prime, f_double_prime, x_0, epsilon):
    x = x_0
    while abs(f(x)) > epsilon:
        u = f(x) / f_prime(x)
        v = u * f_prime(x) / f_double_prime(x)
        x = x - u / (1 - 0.5 * v)
    return x

root = newton_raphson_method(f, f_prime, f_double_prime, 0.5, 0.5e-5)
print(f"The root of the equation x^2 - (1 - x)^5 = 0 in the interval (0, 1) with an accuracy of 1/2 * 10^-5 is approximately {root:.6f}.")

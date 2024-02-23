import numpy as np

def f(x):
    return np.log(x + 1)

h = 0.01

# به روش ذوزنقه ای مرکب
def trapezoidal_compound(f, a, b, n):
     #طول هر زیربازه
    h = (b - a) / n
    #ایجاد آرایه ای از n+1 نقطه در بازه ی (a,b) که هر دو نقطه مجاور فاصله h دارند
    x = np.linspace(a, b, n+1)
    #محاسبه مقدار تابع در هر نقطه از آرایه
    y = f(x)
    #محاسبه مساحت زیر نمودار با فرمول روش ذوزنقه 
    integral = h * (0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1]))
    return integral

#روش سیمپسون
def simpson_compound(f, a, b, n):
    #روش سیمپسون نیاز دارد n زوج باشد
    if n % 2:
        n += 1  
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    # محاسبه ی مساحت زیر نمودار با روش سیمپسون
    integral = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))
    return integral

#  محاسبه مقدار انتگرال در بازه ی [0,1]
integral_trapezoidal = trapezoidal_compound(f, 0, 1, int(1/h))
integral_simpson = simpson_compound(f, 0, 1, int(1/h))

# جواب دقیق
exact_integral = np.log(2)

# چاپ نتایج
print(f"Trapezoidal Method: {integral_trapezoidal}")
print(f"Simpson Method: {integral_simpson}")
print(f"Exact Integral: {exact_integral}")

# مقایسه نتایج
error_trapezoidal = abs(integral_trapezoidal - exact_integral)
error_simpson = abs(integral_simpson - exact_integral)

print(f"\nError in Trapezoidal Method: {error_trapezoidal}")
print(f"Error in Simpson Method: {error_simpson}")

#حل به روش تنصیف

import math


def f(x):
    return math.exp(x) - 3 * x**2

# تعریف یک بازه اولیه برای x
a = 3
b = 4


epsilon = 0.5 * 10**-5

# تعریف یک متغیر برای ذخیره مقدار قبلی x
prev_x = 0


while True:
    # محاسبه نقطه وسط بازه
    x = (a + b) / 2

    
    print("x = ", x)

    # بررسی شرط خروج از حلقه
    if abs(x - prev_x) < epsilon:
        break

    # بررسی علامت تابع در نقطه وسط
    if f(x) > 0:
        # اگر مثبت بود، بازه را به سمت چپ کوچک کن
        b = x
    else:
        # اگر منفی بود، بازه را به سمت راست کوچک کن
        a = x

    # به روز رسانی مقدار قبلی x
    prev_x = x


print(" an approximate root for f(x) = 0 :")
print(x)

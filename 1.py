0
#نمایش تابع جدولی
x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 8, 11, 32, 68, 128]

#مقدار تابع با استفاده از فرمول لاگرانژ
def lagrange(x, y, x0):
    n = len(x)
    y0 = 0
    for i in range(n):
        p = y[i]
        for j in range(n):
            if i != j:
                p = p * (x0 - x[j]) / (x[i] - x[j])
        y0 = y0 + p
    return y0

# تولید یک رشته حاوی چندجمله ای تقریبی با استفاده از فرمول لاگرانژ
def poly(x, y):
    #تعداد نقاط چند جمله ای
    n = len(x)
    s = ""
    #برای محاسبه هر جمله
    for i in range(n):
        p = y[i]
        #برای محاسبه ی ضریب هر جمله با استفاده از فرمول لاگرانژ
        for j in range(n):
            if i != j:
                p = p / (x[i] - x[j])
        #جملات مثبت
        if p > 0 and i > 0:
            s = s + " + "
        #جملات منفی
        elif p < 0:
            s = s + " - "
            p = -p
        #نمایش ضریب هر جمله
        if p != 1 or i == n - 1:
            s = s + str(p)
        if i < n - 1:
            s = s + "x"
         #نمایش توان هر جمله
            if i < n - 2:
                s = s + "^" + str(n - i - 1)
    return s

print("f(x) = " + poly(x, y))

print("f(2.3) = " + str(lagrange(x, y, 2.3)))
print("f(6.7) = " + str(lagrange(x, y, 6.7)))

x_approx = float(input("Please enter x_approx value: "))

print("f(" + str(x_approx) + ") = " + str(lagrange(x, y, x_approx)))

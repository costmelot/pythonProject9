# Даны две функции:
# f(x) = x^3 - 50x и g(x) = -x^4 + 88x^2 - 241
# Требуется:
# 1. Найти координаты точек пересечения

import numpy as np
import matplotlib.pyplot as plt

# f(x) = x^3 - 50x
fx = (0, 1, 0, -50, 0)

# g(x) = -x^4 + 88x^2 - 241
gx = (-1, 0, 88, 0, -241)

rx = np.polynomial.polynomial.polysub(fx, gx)

# print(rx)
res = np.roots(rx)
# print(np.around(res, 2))
res_x = res.tolist()
# print(res_x)
y1 = np.polyval(fx, res_x)
# print(np.around(y1, 2))
res_y = y1.tolist()
# print(res_y)

for i in range(len(res_x)):
    xy = res_x[i], res_y[i]
    t2 = tuple(map(lambda x: isinstance(x, float) and round(x, 2) or x, xy))
    print('Координаты точки пересечения (x, y):', t2)

# 2. Построить графики функций в одной системе координат

x = np.arange(-10, 10, 0.05)
f = x ** 3 - 50 * x
g = - x ** 4 + 88 * x ** 2 - 241

plt.plot(x, f, label="f(x)", linestyle="-.")
plt.plot(x, g, label="g(x)", linestyle=":")
plt.legend()
plt.show()

#  3. Построить график функции пересечения
# Выводим значения точек пересечения на график.

plt.scatter(res_x, res_y)
plt.show()

# Строим модели регрессии с разными степенями полинома.

model = np.polyfit(res_x, res_y, 3)
print(model)

predict = np.poly1d(model)
x_value = 20
print(predict(x_value))

x_axis = range(-15, 15)
y_axis = predict(x_axis)

plt.scatter(res_x, res_y)
plt.plot(x_axis, y_axis, color='b', linestyle=':')
plt.show()

model = np.polyfit(res_x, res_y, 2)
print(model)

predict = np.poly1d(model)
x_value = 20
print(predict(x_value))

x_axis = range(-15, 15)
y_axis = predict(x_axis)

plt.scatter(res_x, res_y)
plt.plot(x_axis, y_axis, color='b', linestyle=':')
plt.show()

model = np.polyfit(res_x, res_y, 1)
print(model)

predict = np.poly1d(model)
x_value = 20
print(predict(x_value))

x_axis = range(-15, 15)
y_axis = predict(x_axis)

plt.scatter(res_x, res_y)
plt.plot(x_axis, y_axis, color='b', linestyle=':')
plt.show()

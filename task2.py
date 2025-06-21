import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції
def f(x):
    return x**2

# Параметри інтегрування
a, b = 0, 2  # Межі інтегрування
N = 100000  # Кількість випадкових точок для Монте-Карло
y_max = f(b)  # Максимальне значення функції на [0, 2]

# Метод Монте-Карло
np.random.seed(42)  # Для відтворюваності
x_random = np.random.uniform(a, b, N)  # Випадкові x
y_random = np.random.uniform(0, y_max, N)  # Випадкові y
under_curve = y_random <= f(x_random)  # Точки під кривою
integral_mc = (b - a) * y_max * np.sum(under_curve) / N

# Аналітичне обчислення інтеграла
# ∫(x^2)dx від 0 до 2 = [x^3/3] від 0 до 2 = 8/3 ≈ 2.66667
integral_analytic = (b**3) / 3 - (a**3) / 3

# Обчислення інтеграла за допомогою quad
integral_quad, error_quad = spi.quad(f, a, b)

# Виведення результатів
print(f"Інтеграл (Монте-Карло): {integral_mc:.6f}")
print(f"Інтеграл (Аналітичний): {integral_analytic:.6f}")
print(f"Інтеграл (quad): {integral_quad:.6f}, помилка: {error_quad:.6e}")

# Візуалізація
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)  # Графік функції
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)  # Область під кривою
ax.scatter(x_random[::100], y_random[::100], c=under_curve[::100], cmap='coolwarm', s=1, alpha=0.5)  # Точки Монте-Карло
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Інтеграл f(x) = x² від {a} до {b} (Монте-Карло)')
plt.grid()
plt.show()

from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Ініціалізація моделі
model = LpProblem(name="Production_Optimization", sense=LpMaximize)

# Змінні: кількість Лимонаду (x) та Фруктового соку (y)
x = LpVariable(name="Lemonade", lowBound=0)  # Лимонад
y = LpVariable(name="Fruit_Juice", lowBound=0)  # Фруктовий сік

# Цільова функція: максимізувати загальну кількість продуктів (x + y)
model += lpSum([x, y]), "Total_Products"

# Обмеження ресурсів
model += 2 * x + y <= 100, "Water_Constraint"  # Вода: 2 од. для Лимонаду, 1 од. для Соку
model += x <= 50, "Sugar_Constraint"  # Цукор: 1 од. для Лимонаду
model += x <= 30, "Lemon_Juice_Constraint"  # Лимонний сік: 1 од. для Лимонаду
model += 2 * y <= 40, "Fruit_Puree_Constraint"  # Фруктове пюре: 2 од. для Соку

# Розв'язання задачі
model.solve()

# Виведення результатів
lemonade = value(x)
fruit_juice = value(y)
total_products = value(model.objective)

print(f"Кількість Лимонаду: {lemonade}")
print(f"Кількість Фруктового соку: {fruit_juice}")
print(f"Загальна кількість продуктів: {total_products}")

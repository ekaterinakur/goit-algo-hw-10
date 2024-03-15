import pulp

problem = pulp.LpProblem("Maximise Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

problem += lemonade + fruit_juice, "Total_Products"

# Обмеження
problem += 2 * lemonade + fruit_juice <= 100, "Water"
problem += lemonade <= 50, "Sugar"
problem += lemonade <= 30, "Lemon juice"
problem += 2 * fruit_juice <= 40, "Fruit puree"

problem.solve()

print('\n')
print("Максимальна кількість продукту:", round(problem.objective.value(), 2))
print("Лемонаду:", round(lemonade.value(), 2))
print("Фруктового соку:", round(fruit_juice.value(), 2))
print('\n')

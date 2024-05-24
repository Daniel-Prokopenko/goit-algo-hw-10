import pulp

model = pulp.LpProblem("problem", pulp.LpMaximize)

L = pulp.LpVariable("L", lowBound=0, cat="Integer")
J = pulp.LpVariable("J", lowBound=0, cat="Integer")

model += L + J, "total"

model += 2 * L + J <= 100  # Вода
model += L <= 50  # Цукор
model += L <= 30  # Лимонний сік
model += 2 * J <= 40  # Фруктове пюре


model.solve()
print(f"Лимонаду: {L.varValue} літрів")
print(f"Фруктового соку: {J.varValue} літрів")

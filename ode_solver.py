import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

# -------------------------
# Input ODE
# -------------------------
x, y = symbols('x y')

func_input = input("Enter dy/dx = f(x,y) (e.g., x + y): ")
f_expr = sympify(func_input)
f = lambdify((x, y), f_expr, 'math')

# -------------------------
# Optional Exact Solution
# -------------------------
exact_input = input("Enter exact solution y(x) (or press Enter to skip): ")

if exact_input != "":
    exact_expr = sympify(exact_input)
    exact_func = lambdify(x, exact_expr, 'math')
else:
    exact_func = None

# -------------------------
# Initial Conditions
# -------------------------
x0 = float(input("Enter initial x0: "))
y0 = float(input("Enter initial y0: "))
h = float(input("Enter step size h: "))
n = int(input("Enter number of steps: "))

# -------------------------
# Euler Method
# -------------------------
x_euler = [x0]
y_euler = [y0]

for i in range(n):
    y_new = y_euler[-1] + h * f(x_euler[-1], y_euler[-1])
    x_new = x_euler[-1] + h

    x_euler.append(x_new)
    y_euler.append(y_new)

# -------------------------
# Runge-Kutta 4 Method
# -------------------------
x_rk = [x0]
y_rk = [y0]

for i in range(n):
    x_i = x_rk[-1]
    y_i = y_rk[-1]

    k1 = h * f(x_i, y_i)
    k2 = h * f(x_i + h/2, y_i + k1/2)
    k3 = h * f(x_i + h/2, y_i + k2/2)
    k4 = h * f(x_i + h, y_i + k3)

    y_new = y_i + (k1 + 2*k2 + 2*k3 + k4) / 6
    x_new = x_i + h

    x_rk.append(x_new)
    y_rk.append(y_new)

# -------------------------
# Output Results
# -------------------------
print("\n========== RESULTS ==========")
print(f"Final value at x = {x_euler[-1]:.6f}")

print(f"Euler Method: y = {y_euler[-1]:.6f}")
print(f"Runge-Kutta (RK4): y = {y_rk[-1]:.6f}")

# -------------------------
# Difference between methods
# -------------------------
diff = abs(y_rk[-1] - y_euler[-1])
print("\nDifference between methods:", diff)

# -------------------------
# Exact Error (if provided)
# -------------------------
if exact_func is not None:
    exact_value = exact_func(x_euler[-1])
    error_euler = abs(exact_value - y_euler[-1])
    error_rk = abs(exact_value - y_rk[-1])

    print("\n========== ERROR (vs Exact) ==========")
    print(f"Exact Value: {exact_value:.6f}")
    print(f"Euler Error: {error_euler:.6f}")
    print(f"RK4 Error: {error_rk:.6f}")

# -------------------------
# Plot
# -------------------------
plt.figure(figsize=(8,5))

# Numerical solutions
plt.plot(x_euler, y_euler, marker='o', label="Euler")
plt.plot(x_rk, y_rk, marker='s', label="Runge-Kutta (RK4)")

# Exact solution (if available)
if exact_func is not None:
    y_exact = [exact_func(xi) for xi in x_rk]
    plt.plot(x_rk, y_exact, linestyle="--", label="Exact Solution")

plt.xlabel("x")
plt.ylabel("y")
plt.title("ODE Solution: Euler vs Runge-Kutta")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

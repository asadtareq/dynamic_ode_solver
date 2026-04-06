# Dynamic ODE Solver (Euler vs Runge-Kutta)

## Description
This project implements numerical methods to solve ordinary differential equations (ODEs) using Python.

Users can input a differential equation dy/dx = f(x, y), initial conditions, and step size. The program computes numerical solutions using Euler and Runge–Kutta (RK4) methods and compares their accuracy.

## Motivation
This project is part of my research preparation in numerical analysis and computational mathematics. It focuses on analyzing the accuracy and efficiency of numerical methods for solving ODEs.

## Methods Implemented
- Euler Method
- Runge–Kutta Method (RK4)

## Features
- Dynamic input of differential equations
- Optional exact solution input
- Error comparison with exact solution
- Method comparison (Euler vs RK4)
- Graph visualization

## Results Summary
- Euler method shows larger numerical error
- Runge–Kutta (RK4) provides highly accurate results
- Error comparison demonstrates the superiority of higher-order methods

## Related Research
This project is related to my preprint:

**Accuracy–Efficiency Comparison of Fixed-Step and Adaptive Runge–Kutta Methods for Ordinary Differential Equations**

DOI: https://doi.org/10.21203/rs.3.rs-9312149/v1

## Technologies Used
- Python
- SymPy
- NumPy
- Matplotlib

## How to Run

1. Install required libraries:

2. Run the program:
 -python ode_solver.py

## Example 
input: 
- dy/dx = x+y
- Exact solution: 2*exp(x) - x - 1
- x0 = 0
- y0 = 1
- h = 0.1
- n = 10

Output:
- Euler result
- RK4 result
- Error comparison
- Graph visualization

## Visualization

- output.png
- plot_ode_solver

## Author
Md Asaduzzaman
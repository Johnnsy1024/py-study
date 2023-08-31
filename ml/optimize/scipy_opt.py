from scipy.optimize import minimize

def eqn(x):
    return x**2 + x + 2

my_min = minimize(eqn, 0, method='BFGS')

print(my_min)
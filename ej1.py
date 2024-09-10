import sympy as sp
#Se definen las variables, donde x = cantera1, y = cantera2, z = cantera3
x, y, z = sp.symbols('x y z')
#Se definen las ecuaciones
eq1 = sp.Eq(0.52*x + 0.20*y + 0.25*z, 4800)
eq2 = sp.Eq(0.30*x + 0.50*y + 0.20*z, 5810)
eq3 = sp.Eq(0.18*x + 0.30*y + 0.55*z, 5690)
#Se obtiene la solucion
sol = sp.solve((eq1, eq2, eq3), (x,y,z))
print(f"""Se debe transportar de la cantera 1: {sol[x]:.2f} metros cubicos
Se debe transportar de la cantera 2: {sol[y]:.2f} metros cubicos
Se debe transportar de la cantera 3: {sol[z]:.2f} metros cubicos
""")
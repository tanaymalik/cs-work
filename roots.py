'''
                                         CALCULATING THE ROOTS OF A QUADRATIC EQUATION

Objective:               the objective of this program is to calculate the roots of a quadratic equation using 
                                        the coefficients a,b,c provided by the user.                                         

'''

# Get coefficients from the user
a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient b: "))
c = float(input("Enter the value of coefficient c: "))


# Calculate the discriminant
discriminant = (b**2) - 4*a*c

# Two real and distinct roots
r1 = (- b - (discriminant)**0.5) / 2*a
r2 = (-b + (discriminant)**0.5) / 2*a

print(f"The two real and distinct roots are: {r1} and {r2}")    
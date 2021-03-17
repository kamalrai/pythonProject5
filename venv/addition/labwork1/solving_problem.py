#solve each of the following problems using python scripts.Make sure you use appropriate variable names and comments.
# When there is a final answer have python print it into the screen. A person's bmi is defined as : weight in kg/(height
# in meter )^2

length = float(input("enter your height ( in meter ): "))
weight = float(input("enter your weight (in kilogram ): "))
bmi = weight / length**2
print(f"your BODY MASS INDEX is {bmi} kg/m^2")

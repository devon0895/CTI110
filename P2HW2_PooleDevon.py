#Devon Poole
#3/13/2024
#P2HW2
#Understanding of Lists

mod1 = float(input("Enter grade for Modlue 1: "))
mod2 = int(input("Enter grade for Modlue 2: "))
mod3 = float(input("Enter grade for Modlue 3: "))
mod4 = int(input("Enter grade for Modlue 4: "))
mod5 = int(input("Enter grade for Modlue 5: "))
mod6 = int(input("Enter grade for Modlue 6: "))
avg = mod1 + mod2 + mod3 + mod4 + mod5 + mod6
#---------Results---------

print(f"\nLowest Grade: {mod5:.1f}")
print(f"Highest Grade: {mod6:.1f}")
print(f"Sum of Grades: {mod1 + mod2 + mod3 + mod4 + mod5 + mod6:.1f}")
print(f"Average: {avg / 6:.2f}")

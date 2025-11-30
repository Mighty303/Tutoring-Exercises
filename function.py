def my_sum(a, b):
    """Returns the sum of two numbers."""
    s = a + b
    return s

# num = my_sum(1, 4)
# print("Sum is " + num)

def calculate_damage(base_damage, multiplier):
    total = base_damage * multiplier
    return total

damage = calculate_damage(10, 2)  # damage is now 20
print(damage)  # Prints: 20
# This function calculates AND gives back the result

def calculate_xp(level):
    xp = level * 100
    return xp

def print_xp_message(level):
    xp = level * 100
    print("You need " + xp + " XP to reach level " + level)

print_xp_message(1)

xp = calculate_xp(1)
print(xp)  # Output: 100

xp = calculate_xp(5)
print(xp)  # Output: 500

xp = calculate_xp(10)
print(xp)  # Output: 1000
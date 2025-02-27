import random

value = random.randint(1, 10)

if value <= 5 and value >= 1:
    print("Heads!")
elif value >= 6 and value <= 10:
    print("Tails!")
else:
    print("Flip again")
"""Run me: python 01-basics/examples.py  (then change things and re-run!)"""

# Variables
player = "Alex"
score = 120
print(f"{player} has {score} points")

# Conditionals
if score >= 100:
    print("Level up!")
else:
    print("Keep going")

# Loops
print("Countdown:")
for i in range(3, 0, -1):
    print(i)
print("Go!")

# Even or odd with %
for n in range(1, 6):
    kind = "even" if n % 2 == 0 else "odd"
    print(n, "is", kind)

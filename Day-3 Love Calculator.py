print("Welcome to Love calculator")
n1 = input("Enter Your name\n")
n2 = input("Enter your boyfriend/girlfriend name\n")
combined = n1 + n2
lower = combined.lower()
t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")
true = t + r + u + e
l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
print(f"Your love score is {love_score}")


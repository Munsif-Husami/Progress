#1st Approach

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
who_picked = random.randint(1,1000)
print(who_picked)
if who_picked < 200:
    print(friends[0])
elif who_picked < 400:
    print(friends[1])
elif who_picked < 600:
    print(friends[2])
elif who_picked < 800:
    print(friends[3])
else:
    print("Emanuel")

#2nd Approach
who_picked = random.choice(friends)
print(f"{who_picked} will pay the bill")

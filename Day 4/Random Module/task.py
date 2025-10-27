import random
import my_module

#random_int = random.randint(1,10)
#print(random_int)

#print(my_module.my_fav_number)

#random_num = random.random() * 10
#print(random_num)

#random_float = random.uniform(1,10)
#print(random_float)

random_choice = random.randint(1,100)
print(random_choice)
if random_choice % 2 == 0:
    print('Heads')
else:
    print('Tails')
# import random

# side =random.randint(0,1)

# if side == 0:
#     print("Heads")
# else:
#     print("Tails")

import random

Person = str(input("Enter the name of the person seprated by commas: "))
Name = Person.split(",")
length=len(Name)
# print(length)
Bill = random.randint(0,length-1)
Cash=Name[Bill]
print(f"The person who will pay the bill is: {Cash}")
#.......................................Nested if statements...........................................
'''
a=input().lower()
b=input().lower()
if a=="sunny":
    if b=="morning":
        print("Go and play football")
    else:
        print("It's time to sleep.Good night")
elif a=="rainy":
     if b=="morning":
         print("Go and play with yourboat toy")
     else:
         print("It's time to sleep lock your doors")
else:
     print("Play with your video games")
print("Have a Nice Day")
'''
#............................................Nested if statements.............................................



for i in range(1,6):
    for j in range(1,11):
        print(f"{i} * {j} = {i * j} ")

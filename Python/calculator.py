a=input("Give me operater: ").lower()
b=int(input())
c=int(input())
if a=="addition" or a=="+":
    print(f"Addition:{b+c}")
elif a=="subtraction"or a=="-":
     print(f"Subtraction:{b-c}")
elif a=="division" or a=="/":
     print(f"Division:{b/c}")
elif a=="multiplication" or a=="*":
     print(f"Multiplication:{b*c}")
else: 
     print("Some went wrong: Try Again")
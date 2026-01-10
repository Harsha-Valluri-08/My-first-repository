'''
a="Harsha"
print(a[0:-2:3])
'''
#.........................................................
'''
s=input()
s2=s.lower()
a=s2.count('a')
e=s2.count('e')
i=s2.count('i')
o=s2.count('o')
u=s2.count('u')
print(f"Number of vowels: {a}+{e}+{i}+{o}+{u}")
'''
#..........................................................
'''
a=int(input("Marks in Math: "))
b=int(input("Marks in Science: "))
c=int(input("Marks in English: "))
T=a+b+c
print(f"Total Marks:{T}")
A=T/3*100
print(f"Average Marks:{A}")
if A>90:
    print('Grade:A')
elif A>80 and   A<90:
     print("Grade:B")
elif A<80 and A>70:
      print("Grade:c")
else:
     print("Better luck next time: Fail")
print("Education is the key to success")
'''
#...........................................................................................................................................
'''
a=input()
a1=a[::-1]
if a==a1 :
    print("It is a palindrome")
else:
    print("It is not a palindrome")
'''
#........................................................
'''
a,b,c=input().split(",")
n1=int(a)
n2=int(b)
n3=int(c)
if n1>n2 and n1>n3:
      print(f"The greatest Number is:{ n1}")
elif n2>n3 and n2>n1:
         print(f"The greatest Number is:{ n2}")
elif n3>n1 and n3>n2:
         print(f"The greatest NUmber is:{ n3}")
'''
'''
a=int(input())
if (a%4==0 and a%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")
'''
'''
a=int(input())
b=a+273
print("Kelvin:",b,end="k")
'''
'''
a = input()
b = a[-1:-6:-2]
print(b)
'''

a = " hARSHA".swapcase().lstrip()
print("My name is:",a)
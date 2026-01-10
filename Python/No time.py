'''
a=input("Enter your name: ")
print("Hello,",a)
'''
'''
x,y=input().split(",")
sum=int(x)+int(y)
print(sum)
'''
'''
a=input("Name of the student: ")
b=input("Marks alloted: ")
print(f"Name: {a} Marks: {b}")

'''
'''
x,y=input().split(",")
a=int(x)
b=int(y)
sum=a+b
print(sum)
'''
'''
num1=5
num2=10
sum=num1+num2
print("sum:",sum,sep="")
print(f"sum:{sum}")
'''
'''
#........................................................................................................................................
a=int(input("Give some value:"))
b=int(input("Give some value:"))
c=int(input("Give some value:"))
d=(b**2)-4*a*c
root1=(-b+(d**(0.5)))/2*a
root2=(-b-(d**(0.5)))/2*a
print(f"Roots: ({root1},{root2})")
#........................................................................................................................................
'''
'''
a=20
b=10
a+=b#(30)
b=a-b#(10)
a=a-b#(30-10)
print(f"value of a is:{a}")
print(f"value of a is:{b}")
'''

i,j = input().split(",")
a = int(i)
b = int(j)
print(f"Addition:{a+b}\nSubtraction:{a-b}\nDivision:{a/b}\nMultiplication:{a*b}")
# Questio NO;1
# expected input=John
# expected output= Hello,John
# THIS IN VARABLE FORM
'''
a="John"
print('Hello',a,sep=",")
# IN INPUT FORM
Name = input("Enter your name")
print("Hello",Name,sep=",")
'''

# Question NO;2
# expected input=5
# expected output=You entered:5

'''
a=int(input("give me some value;"))
b=int(input("give me some value;"))
c=a+b
print("final value",c)
a=input()
print("value of Pi:",a)
'''
'''
a=int(input())
b=int(input())
c=int(input())
sum=a+b+c
print(sum)
'''
'''
a=input()
b=a.split(" ")
print(b)
'''
'''
x,y=input().split()
print("x=",x,"y=",y,sep=" ")
'''
'''
x,y,z=input().split()
sum=int(x)+int(y)+int(z)
print(sum)
'''
'''
a=input()
b=input()
print("Name:",a,",Age:",b,sep="")
'''
'''
a=int(input())
print('Addition:',a,"Subtraction:",a,"Multiplication:",a,"Division:",a)
'''
'''
x,y=input().split(",")
sum=int(x)+int(y)
print(sum)
'''
'''
a="Harsha is a"
print(len(a))
'''
'''
a="Harsha     is a  "
a1=a.strip()
print(a1)
'''
'''
a=input("Marks in Math: ")
b=input("Marks in Science: ")
c=input("Marks in English: ")
total=int(a)+int(b)+int(c)
Average=total/3*100
print(f"Total Marks:{total} ")
print(f"Aveage Marks:{Average}")
print("Grade: A")
'''
'''
a=1
b=0
c=a and b
print(c)
'''
'''
a={1,2,3}
print(1 in a)
'''
'''
# it doesn't see weather the letter are capital are not  #
a="Harsha"
b="harsha"
print(a is not b)
'''
# This are used for sets #
'''
c = 10
while c>0:
# Give one c to a friend
 print("Giving a c to a friend!")
# Decrease the number of c
c-=1 
'''


n = int(input("Enter a number: "))

even_count = 0
odd_count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

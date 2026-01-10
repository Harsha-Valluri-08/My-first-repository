#........................one...............
'''
a = int(input())

while a>0:
    b=a%10
    print(b)
    a=a//10
'''
#....................one......................

#...I have to be the best of my self.........#
'''
name = input("What is your name:").title()
if name == "Hello Buddy":
    print("Hi sir, How can I help you it's your Buddy:")
else:
    print("May I know how you are:")
'''
'''
A = input("May I know your Good name:").lower()
i = 1
while A == "harsha" and i<=3:
    print("Hello sir:")
    i +=1
    if A != "harsha":
        print("I can't recognize you") # There is fault in this #
'''
'''
a = int(input("give me some value:"))
for i in range(1,a):
    if i%2 == 0:
     print
     '''
'''
n = int(input("Give me some value:"))

i = 0

while n>0:
    i+=1
    if i>5:
     break
    print(i)

for w in range(1,6):
   print(w)
'''
'''
n = int(input("Give me some value:"))

i = 0

while i<n:
    i += 1
    print(i)
'''
'''
n = int(input("Give me some value:"))

i = 0
sum = 0

while i<n:
    i += 1
    sum +=i
    print(sum)


for w in range(n+1):
    sum += w
    print(sum)
'''
'''
a = int(input("Give me some value:"))

i = 0

while i<a:
    i+=1
    if not (i%2==0):
     print(i)
     print("Even numbers")

for w in range(1,a+1):
    if w%2 == 0:
     print(w)

'''
'''
a = int(input("Give me some value:"))
b = int(input("Give me some value:"))

for i in range (1,a+1):
    for j in range(1,b+1):
        print(f"{i}x{j} = {i*j}")
'''
'''
a = int(input())

i = 0

while i<=10:
    print(f"{a} X {i} = {a*i}")
    i += 1
'''
'''
n = int(input("Give me some value:"))
factorial = 0
for w in range(1,n+1):
    factorial +=1
    total = factorial*w
    print(total)
'''
'''
a = int(input())

b = 1

for w in range(a+1):
    b *= a
    a-=1
    print(b)
'''
'''
a = int(input("Give me some value"))

f = 1
while a>0:
    f *= a
    a -= 1
    print(f)
    '''
'''
n = int(input())
i = 0
while i<n:
    i += 1
    print(i)

for w in range(1,n+1):
    print(w)
'''
'''
n = int(input())

for w in range(1,n+1):
    if w%2 == 0:
        print(w)
i = 0
while i<n:
    i += 1
    if i%2 == 0:
     print(i)
'''
'''
a = int(input())

i = 0
sum = 0

while i<a:
    i += 1
    sum += i
    print(sum)

for w in range(1,a+1):
    sum += w
    print(sum)
'''
'''
a = int(input())
b = int(input())
for i in range(1,a+1):
    for j in range(1,b+1):
        print(f"{i} x {j} = {i*j}")
'''
'''
a = 3
b = 0
while b<10:
    b += 1
    print(f"{a} x {b} = {a*b}")
'''   
'''
a = int(input())
i = 0
while i<a:
    i += 1
    if i%2 != 0:
        print(i)
for w in range(1,a+1):
    if w%2 != 0:
        print(w)
'''
'''
a = int(input())
b = int(input())
for i in range(1,a+1):
    for j in range(1,b+1):
        if i == 3:
            continue
        print(f"{i} x {j} = {i*j}")
'''
'''
a = int(input())
b = int(input())
def sum(a,b):
    print(a+b)
sum(a,b)
'''
'''
r = int(input("Give me some value:"))

def radi(a):
    print(3.14*r*r)
radi(r)
'''
'''
a = int(input("Give me some value:"))
b = int(input("Give me some value:"))
c = int(input("Give me some value:"))

def quadratic(a,b,c):
    d = (b**2)-(4*a*c)
    return (-b+(d**(0.5)))/2*a
c = quadratic(a,b,c)
print(c)
'''
'''
def swap(a,b):
    a += b
    b = a -b
    a -= b
    print(f"b = {a}")
    print(f"a = {b}")
swap(5,10)
swap(10,5)
swap(20,30)
'''
'''
def tem(x):
    a = 273 + x
    b = 9/5*x + 32
    print(a)
    print(b)
tem(30)
'''



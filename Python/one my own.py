'''
a = input("Name:").capitalize()
b = int(input("Age:"))
print("Hello!",a," your current age is:",b,sep="")
print(f"Hello!{ a} your current age is:{b}")
'''
'''
def sum(a,b):
    return a+b
a = sum(5,10)
print(a)
'''
'''
print(chr(68))
print(ord("A")
'''
'''
float= 'harsha'
print(float)
'''
'''
a = [1,2,3,1,1,1,22]
a.clear()
print(a)
'''
'''
x = int(input("Give me some value:"))

i = 0
while i<x:
    i += 1
    if i%2 != 0:
        print(i)


for z in range(x):
    if not z%2 == 0:
        print(z)

print("Hello")
'''
'''
a = {'name': "harsha",'age': 17,'house': 2-40,'Age': 17}
print(set(a.values()))

print(a)
'''
'''
a = {'Harsha','harsha','HARSHA'}
a = list(a)
print(a)
a.remove("HARSHA")
print(a)
a.extend([3,4])
print(a)
a.append([3,4])
print(a)
a.append("ab")
print(a)
a.extend([1])
print(a)
'''
'''
s = int(input("Values in your mind:"))
i = 0 
sum = 0
while i<s:
    i += 1
    sum += i
    print(sum)
'''
'''
a = int(input())

i = 0
while i<a:
    i += 1
    if i%2 == 0:
        print(i)

for w in range(1,a+1):
    if w%2 == 0:
        print(w)
'''
'''
def print_even(n):
    for i in range(0,n+1,2):
        print(i)

a = int(input("Enter a number: "))
print_even(a)
'''
'''
a = int(input("Enter the values:"))

i = 1
while i<a:
    i += 1
    if i == 2 or 1 == 3:
        print(i)
        continue
    if i%2 !=0 and i%3 !=0 and i %5 != 0 and i%7 != 0 and i%9 != 0 and i != 11:
      print(i)

for w in range(2,a+1):
    if w == 2:
        print(w)
        continue
    if w == 3:
       print(w)
       continue
    if w%2 !=0 and w%3 !=0:
      print(w)
'''
'''
a = int(input())

even_count = 0
odd_count = 0
for w in range(1,a+1):
    if w%2 == 0:
        even_count += 1
    else :
        odd_count +=1

print("Even_count:",even_count)
print("Odd_count:",odd_count)
'''
'''
a = ord('a')
print(a)

b = chr(99)
print(b)

c = 3//5
print(c)

print(4//5)

print(2**2)

v = 'Harsha'
print(len(v))
'''
'''
a = int(input())
b = int(input())
if a<b:
    def sum(a,b):
     print(a+b)

    sum(a,b)
'''
'''
def function(a,b):
    print(a+b)

function(1,2)
'''

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)
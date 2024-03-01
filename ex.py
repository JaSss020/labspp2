print("Hello, World")

if 5>2: 
    print("YES")

#This is a comment

"""
This is a comment
written in 
more than just one line
"""

carmane = "Volvo"

x = 50

x = 5
y = 10
print(x+y)

x = 5
y = 10
z = x + y
print(z)

x,y,z = "Banana" , "Orange" , "Cherry"

x=y=z="Orange"

def myfunc():
    global x
    x = "fantastic"

x = 5
print(type(x)) #it will be integer

x = "Hello, World"
print(type(x)) #it will be string

x = 10.5
print(type(x)) #it will be float

x = [" egwg", "rg wgwg" , "rgwgh"]
print(type(x)) #it will be list

x = ("egfgwg", " rwhwh", "rhwh")
print(type(x)) #it will be tuple

x = {"name": "John", "age": 15}
print(type(x)) #it will be

x = True
print(type(x)) #it will be boolean

x = 5
a = float(x)

x = 5.5
a = int(x)

a = complex(x)

x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


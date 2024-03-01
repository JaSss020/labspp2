import random

#ex1
def gramToOunces(grams):
    return grams*28.3495231

a = 2 #in grams
print(gramToOunces(a))

def FtoC(faren):
    return (faren-32)*(5/9)

b = 3 #in farenheit 
print (FtoC(b))

def primeSorter(list):
    result = []
    for i in list:
        if i > 1:
            flag = False
            for j in range(2, int(i**0.5) + 1):
                if i % j==0:
                    flag = True
                    break
            if not flag:
                result.append(i)
    return result

c = [1,4,6, 19, 17, 11]
print(primeSorter(c))

def permutator(str, empt = ""):
    if not str:
        print(empt)
    else:
        for i in range(len(str)):
            new_str = str[:i] + str[i+1:]
            permutator(new_str, empt + str[i])

# permutator("sultan")

def wordReversor(str1):
    b = str1.split(" ")
    str2 = ""
    for i in reversed(b):
        str2 += i
        str2 += " " 
    print(str2)

wordReversor("hello everyone")

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

list = [3,4,5,6,7,3]
print(has_33(list))

def spy_game(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i+2] == 7:
            return True
    return False

list = [0,0,4,0,0,7]
print(spy_game(list))


def findValue(radius):
    print((4/3)*3.14*radius**2)

findValue(3)


def ispalindrome(str):
    cleaned_str = ''.join(str.lower().split())
    return cleaned_str == cleaned_str[::-1]
word = "madam"
print(ispalindrome(word))


def uniqueElements(list):
    unique_list = []
    
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    
    return unique_list

list = [1,4,4,5,5,6,3,1]
result = uniqueElements(list)

print(result)

def histogram(list):
    for i in list:
        print("*" * i)

list = [1,2,3]
histogram(list)

def guessThenumber():
    print("Hello! What is your name? ")
    name = str(input())

    rand_num = random.randint(1, 20)
    print("Well, " + name + " I am thinking of a number between 1 and 20.")

    cnt = 0
    while(True):
        print("Take a guess")
        a = int(input())
        cnt += 1
        if(a == rand_num):
            print(cnt)
            print("Good job," +name+ " You guessed my number in " +  " guesses!")
            break

#guessThenumber()

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def morethan55(movie):
    for i in movies:
        if i["imdb"] > 5.5:
            print(i["name"])

morethan55(movies)

category1 = "Romance"

def category_sorting(movie):
    list = []
    for i in movies:
        if i["category"] == category1:
            list.append(i["name"])
    print(list)

category_sorting(movies)

def avarage_value(movie):
    a = 0
    for i in movies:
        a += i["imdb"]
    print(a/15)

avarage_value(movies)

#1
class string_methods:
    def _init_(self):
        self.str = ""
    
    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())
 
use = string_methods()
use.getString()
use.printString()

#2
class Shape:
    def area():
        print(0)

class inh(Shape):
    pass

class Square(Shape):
    def _init_(self,length):
        self.length = length
    
    def area(self):
        print(self.length*self.length)

sh = Shape()
sq = Square(6)
print(sh.area()," ",sq.area())

#3
class Rectangle(Shape):
    def _init_(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        print(self.length*self.width)

rec = Rectangle(4,6)
rec.area()

#4
import math
class Point():
    def _init_(self,x,y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)
    
    def move(self,x1,y1):
        self.x = x1
        self.y = y1
    
    def dist(self,x1,y1):
        print(math.sqrt((self.x-x1)*2+(self.y-y1)*2))

points = Point(4,5)
points.move(2,4)
points.dist(1,3)

#5
class bank_account():
    def _init_(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep):
        self.deposit =+ dep
    
    def withdraw(self,withd):
        if self.withdraw > withd:
            self.withdraw=-withd
        else:
            print("Sizdin balans molsheri zhetpeidi")

bank = bank_account("Aibar", 1000)
bank.deposit(600)
bank.withdraw(1500)

#6
def prime_filter(number):
    if number == 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        return True

num = [15,12,2,13,23]

prime = list(filter(lambda x: prime_filter(x), num))
print(prime) 
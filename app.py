from math import *
import util
from Student import Student

print("hello world")

print("   /")

print(" /")



a = 23
b = "hell";


print( len(b.upper()))
print( a)
print( a , b)

print(b[2])

print(b.index("ll"))

b = b.replace("ll","llo")

print( b)

print(-34343444343343434343433434343343 / 7878788788008808)

print(-333434343343 * (7878788788008808 /33))


print(str(10 % 3))
print (pow(3,3))


print(sqrt(36))

#name = input("whats your name ")
#age = input("whats your age ")


#print ("hello " + name , age)


ages = [98,8,0]
names = ['kapil','test','tom']

#start from back
print(names)
ages.extend(names)
print(ages.append(90))
print(ages.insert(2,'data'))


print(ages.remove('data'))

#remove last element
ages.pop()



print(ages.index("kapil"))

##error if not in list.

print(ages.count("kapil"))

names.sort()

print(names)

cords = [(4,5),(8,9)]


print(cords[0])

print(cords[0][1])



def add_num(data):
    print("input num" + data)

add_num("89")


is_male = True
isTall = False

if is_male and isTall:
    print("male is tall")
elif is_male and not(isTall):
    print("male not tall")


else:
    print("no male")

i = 1

"""while i <= 10:
    print(i)
    i += 1
"""
## map like data structure called dictonary in python
data = {

    "jan" : "january",
    "feb" : "februray",
}
x = 1

print(len(data.items()))
while x <= len(data.items()):
    print(x)
    print(data["jan"])
    x += 1



for letter in "hello kapil":
    print(letter)

friends = ["Kapil","tom","harry"]

for friend in friends: ## for list of friends
    print(friend)

for index in range(3,10): ## range from 3 to 10
    print(index)

for index in range(10):  ## from 0 to 9
    print(index)

for index in range(len(friends)):

    if index == 2:
        print("my second friend")

    print (friends[index])

try:
    print("hello")
except:
    print("never reach here")

#read file r , w write file , a append file , r+

##reading from file..
filedata = open("data.txt","r")
#print(filedata.readable()) ## true if file is readable.
#print(filedata.read()) ##write data to print stream
#print(filedata.readline()) ##write mutiple line

for datainfile in filedata.readlines():
    print(datainfile)

filedata.close()


# calling function from other file.
util.upper()



## using student class here


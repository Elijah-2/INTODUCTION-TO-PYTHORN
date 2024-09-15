"""this the introduction to python
#single quotes or double quotes are preferred

print("hello world")
#variable - is a container for values ..it behaves like the values it contains
#values include string,floats,boolean,integers and so on
first_name = 'elijah onyango'
print(first_name)
print(f"hello mr.{first_name}, Onyango")
#INTEGERS,BOOLEAN,FLOATS AND OTHER VALUES CAN BE USED THE SAME WAY
#the integers
age= 23
height=3
clothes = 40
name ="Elijah"
single = False
print(f"hello student my name is {name} , \ni am {age}, years old i have {clothes} clothes,\n "
      f"my height is {height}, \ntall and my marital status single={single}")

#TYPECASTING
#This the process of converting one data type to another
examples include;
str() ,int(),float(),bool()
we use type() to know the type of datatype we are dealling with for examples
name = "Elijah Ouma"
age = 25
gpa = 3.8
married = False
print(type(name))
print(type(age))
print(type(married))
print(type(gpa))
#integers can be type casted to string
#input = is a function that prompts the user to enter there questions or views and it return the side effects as a string.
name =input("What is your real name? ")
buy = input("what do you want to buy today ")
number=int(input("what quantity would you like to buy "))
cost =int(input("what is the price of each item bought? "))
total =number*cost
print(f"your name is {name},\n,you have bought {buy} ,"
      f"\n,each {buy} cost {cost}, \n, so you have to spent {total} shillings today\n"
      f" .thanks in advance")
#MADLIBS GAME
#WORD GAME WHERE ONE CREATS A STORY BY FILLING BLANKS WITH RANDOM WORDS
#Argumented sign operator (+=)
M = input("guess time of the day: ")
P= input("Guess anything that starts with letter p: ")
C = input("guess any letter that starts with letter C: ")
print(f"when i woke up in the   {M}, i found {P} ,: \n"
      f"Washing their teeth,the {C} "
      f"\nask me to bring my plate so that it can be served as sooon as possible")
friends = 154
#friends+=5 this adds 5 to friends
#friends -=2 this subtruct 2 from original number of friends
#friends *=3 this multiply the values of friends by 3
#friends /=4 this divides the value of friends to whole number
#friends **=2 this get the value in powered form
#friends %=3 this gives the remainder in division of calculation
print(friends)
x = 20
y=4.23333333333
z = -87
#result = round(y,4) # this rounded the value to the nearest 4 decimal places
#result= abs(z) # this determines the absolute values of the values given
#result = pow(2,10)  two is the bse and 10 is the power
#result= max(x,y,z)
result= min(x,y,z) this is how to get a minimum value and maximum value in a data set

print(result)"""

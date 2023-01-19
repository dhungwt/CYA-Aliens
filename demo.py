#Data types
print("hello world")#string 
print(5) #int
print(5.0) #float 

#Arithmetic Operators 
# reference - https://www.w3schools.com/python/python_operators.asp

#variables 
name = "beth"
print("Welcome " + name + "!")
#string methods reference https://www.w3schools.com/python/python_ref_string.asp 
print("Welcome" + name.upper() + "!")

#built in functions reference https://www.w3schools.com/python/python_ref_functions.asp
print("your name has " + str(len(name)) + " letters in it")  

#user input 
age = int(input("how old are you? "))
# print("you are " + age + " years old")

#conditionals (if/else)
if age >= 18:
	print("you are old enough to vote")
else:
	print("not old enough to vote")

#branching if statements & comparison operators 
username = input("please enter your username: ")
password = int(input("please enter your password: "))

if username == "Beyonce" and password == 1234:
	print("hello Queen B!")
elif password != 1234 and username == "Beyonce":
	print("wrong password")
else:
	print("hello regular person")
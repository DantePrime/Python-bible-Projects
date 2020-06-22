#Ask for user's info

name = input("What is your name?: ")
age = input("How old are you?: ")
city = input("What city do you live in?: ")
hobby = input("What do you love doing?: ")

#Output

string = "\n\nYour name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,hobby)

print(output)

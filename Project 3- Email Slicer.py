#Ask user's email address

email = input("What is your email address ?: ").strip()

#Slicing before @

user = email[:email.index("@")]

#Slicing after @

domain = email[(email.index("@")+1):]

#Output

output = "Your username is {} and your domain name is {}".format(user,domain)

print(output)

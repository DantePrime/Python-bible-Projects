import random

health = 50
print("Initial health is {}".format(health))
difficult = int(input("1.Easy\n2.Medium\n3.Hard\nEnter the difficulty level"))
potion_health = int(random.randint(25,50)/difficult)
health = health + potion_health
print("Health after taking health potion is {}".format(health))


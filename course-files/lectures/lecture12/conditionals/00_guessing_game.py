from random import randint

# First pick a secret number.
secret = randint(0, 100)

# for debugging...(cough cheating cough)
# print(secret)

# Then ask the person to input a number
my_num = input("Guess what number I'm thinking of? ")
# Don't forget to convert the string to an int!
my_num = int(my_num)

# Now check to see if the number is the secret one!
# If it is, tell them they win. Otherwise, tell them the secret.
if my_num == secret:
    print("Holy guacamole you won!")
else:
    print("Lol. Not even close.")
    # Here we use the variadic syntax of print for convenience!
    print("The secret was...", secret, "but you guessed", my_num)

print("Game over.")
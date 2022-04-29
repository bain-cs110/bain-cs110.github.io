import random

# Create a list of 100 wallets
wallets = [100] * 1000

counter = 0

while counter < 10000:
    for person in wallets:
        person_1 = random.randint(0, len(wallets)-1)
        person_2 = random.randint(0, len(wallets)-1)
        if wallets[person_1] > 0:
            wallets[person_1] -= 1
            wallets[person_2] += 1

    counter += 1


print(wallets)

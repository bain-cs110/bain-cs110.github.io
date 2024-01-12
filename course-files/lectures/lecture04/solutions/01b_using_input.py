# ----------------------------------------------------
# 1. say hello using an input
# ----------------------------------------------------

# Old method
print("Hello there, Obi-wan!")
print("Your name is", len("Obi-wan"), "letters long")
print("How are you this morning?")


# New method that takes any name as input!
name = input("Enter your name: ")
print("Hello there " + name)
print("Your name is", len(name), "letters long")
print("How are you this morning?")

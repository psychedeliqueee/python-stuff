print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

names = lowercase_name1 + lowercase_name2

true = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love = names.count("l") + names.count("o") + names.count("v") + names.count("e")

result = str(true) + str(love)
result_int = int(result)

if result_int < 10 or result_int > 90:
    print(f"Your score is {result_int}, you go together like coke and mentos.")
elif result_int > 40 and result_int < 50:
    print(f"Your score is {result_int}, you are alright together.")
else:
    print(f"Your score is {result_int}.")

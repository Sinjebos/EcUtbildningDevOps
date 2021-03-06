import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print('Invalid input')

print('*' * 40)
print(get_integer.__doc__)
print('*' * 40)
help(get_integer)
print('*' * 40)

min_value = 1
max_value = 10
answer = random.randint(min_value, max_value)

guess = -1
print('Enter "0" to end game early')
print("Guess a number between {} and {}: ".format(min_value, max_value))
while guess != answer:
    guess = get_integer(': ')

    if guess == 0:
        print("Quiting game")
        break

    if guess == answer:
        print("Correct guess")
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

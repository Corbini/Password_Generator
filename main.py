import string
import random


def get_letters(count=0, big_letters=True):
    letters_data = string.ascii_lowercase
    if big_letters:
        letters_data += string.ascii_uppercase

    picked_letters = []

    while count:
        picked_letters.append(
            letters_data[random.randint(0, len(letters_data)-1)])
        count -= 1

    print(picked_letters)
    return picked_letters


def get_numbers(count=0, specials=True):
    return ["1", "2", "!"]


def randomize_placement(letters=[], numbers=[]):
    return "password"


def password_dont_have_words(password=""):
    return True


def get_bool_input(text=""):
    while True:
        user_input = input(text + "(y for yes, n for no): ")

        if user_input == "y":
            return True

        if user_input == "n":
            return False

        print("Incorrect input")


def get_number_input(text=""):
    while True:
        user_input = input(text + ": ")
        if user_input.isdecimal():
            return int(user_input)

        print("incorrect input")


def main():
    print("Welcome to password generator",
          "Specify your password", sep="\n")

    amount_of_letters = get_number_input("How many letters do you want?")
    want_big_letters = get_bool_input("Do you want big letters?")
    letters = get_letters(amount_of_letters,want_big_letters)

    amount_of_numbers = get_number_input("How many numbers do you want")
    want_specials = get_bool_input("Do you want big letters")
    numbers = get_numbers(amount_of_numbers, want_specials)

    while True:
        password = randomize_placement(letters, numbers)
        if password_dont_have_words(password):
            break

    print("Your password is:", password)


random.seed()
main()

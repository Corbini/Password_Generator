import string
import random


def get_random_from_list(count=0, data_list=[]):
    if len(data_list) == 0:
        return []

    picked = []

    while count:
        picked.append(
            data_list[random.randint(0, len(data_list) - 1)])
        count -= 1

    print(picked)
    return picked


def get_letters(count=0, big_letters=True):
    letters_data = string.ascii_lowercase
    if big_letters:
        letters_data += string.ascii_uppercase

    return get_random_from_list(count, letters_data)


def get_numbers(count=0, punctuation=True):
    numbers_data = string.ascii_letters
    if punctuation:
        numbers_data += string.punctuation

    return get_random_from_list(count, numbers_data)


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
    want_punctuation = get_bool_input("Do you want punctuation")
    numbers = get_numbers(amount_of_numbers, want_punctuation)

    while True:
        password = randomize_placement(letters, numbers)
        if password_dont_have_words(password):
            break

    print("Your password is:", password)


random.seed()
main()

import string
import random


def get_letters(count=0, big_letters=True):
    if count < 0:
        return [];

    letters_data = string.ascii_lowercase
    if big_letters:
        letters_data += string.ascii_uppercase

    return random.choices(letters_data, k=count)


def get_numbers(count=0, punctuation=True):
    if count < 0:
        return [];

    numbers_data = string.digits
    if punctuation:
        numbers_data += string.punctuation

    return random.choices(numbers_data, k=count)


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

    data_list=[]

    amount_of_letters = get_number_input("How many letters do you want?")
    want_big_letters = get_bool_input("Do you want big letters?")
    data_list += get_letters(amount_of_letters,want_big_letters)
    print(data_list)

    amount_of_numbers = get_number_input("How many numbers do you want")
    want_punctuation = get_bool_input("Do you want punctuation")
    data_list += get_numbers(amount_of_numbers, want_punctuation)
    print(data_list)

    while True:
        password = random.sample(data_list, k=len(data_list))
        if password_dont_have_words(password):
            break

    print("Your password is:", "".join(password))


random.seed()
main()

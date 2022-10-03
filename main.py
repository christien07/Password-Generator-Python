import secrets
import string
import random

def main():
    print("Welcome to my Password Generator Tool built in Python.")
    security_measure = input("Does this password need to be reasonably secure? Y or N\n")
    if security_measure.upper() == 'Y':
        how_long = input("How long should the password be? Only enter an integer value here:\n")
        range_of_char = string.ascii_letters + string.digits + string.punctuation
        final_pass = ''.join(secrets.choice(range_of_char) for i in range(int(how_long)))
        print(f"Your password is:\n{final_pass}")

    elif security_measure.upper() == 'N':
        num_letters = input("How many letters would you like in your password?\n")
        num_symbols = input("How many symbols would you like in your password?\n")
        num_numbers = input("How many numbers would you like in your password?\n")

        population = ""
        if int(num_numbers) > 0:
            population += "0123456789"
        if int(num_symbols) > 0:
            population += "`~!@#$%^&*()-_+={[;:}]'<>,.?/\|"
        if int(num_letters) > 0:
            population += "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

        passwd = random.sample(population, k=(int(num_numbers) + int(num_letters) + int(num_symbols)))
        print(f"Your password is:\n" + "".join(passwd))


if __name__ == "__main__":
    main()

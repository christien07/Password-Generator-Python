import secrets
import string

def main():
    print("Welcome to my Password Generator Tool built in Python.")
    security_measure = input("Does this password need to be reasonably secure? Y or N\n")
    if security_measure.upper() == 'Y':
        how_long = input("How long should the password be? Only enter an integer value here:\n")
        range_of_char = string.ascii_letters + string.digits + string.punctuation
        final_pass = ''.join(secrets.choice(range_of_char) for i in range(int(how_long)))
        print(f"Your password is:\n{final_pass}")

    elif security_measure == 'N':
        num_letters = input("How many letters would you like in your password?\n")
        num_symbols = input("How many symbols would you like in your password?\n")
        num_numbers = input("How many numbers would you like in your password?\n")

        # Store gen. password in array
        passwd = []



if __name__ == "__main__":
    main()

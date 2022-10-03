import secrets
import string
import random

def main():
    # D.R.Y.
    # :)
    numbers = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]

    # Need to include both backslash, \, and quotes, ", implementation may need to change
    symbols = [
        "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", ";", ":", "}", "]", "'", "<", ">", ",", ".",
        "?", "/", "\n".strip("n"), "|", '"'
    ]

    letters = [
        "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", 
        "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"
    ]

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

        total_len = int(num_letters) + int(num_numbers) + int(num_symbols)

        """
        population = ""
        if int(num_numbers) > 0:
            population += "".join(numbers)
        if int(num_symbols) > 0:
            population += "".join(symbols)
        if int(num_letters) > 0:
            population += "".join(letters)
        """

        # Symbols: There are 32 symbols to choose from
        rando1 = random.randint(0, 31)
        # Numbers: There are 10 numbers to choose from
        rando2 = random.randint(0, 9)
        # Letters: There are 26*2 == 52 letters, including uppercase and lowercase
        rando3 = random.randint(0, 51)

        n = 1
        password = ""
        while n < total_len:
            if int(num_symbols) > 0:
                i = 0
                while i < int(num_symbols):
                    password += symbols[random.randint(0, 31)]
                    i += 1
                    n += 1
            if int(num_numbers) > 0:
                j = 0
                while j < int(num_numbers):
                    password += numbers[random.randint(0, 9)]
                    j += 1
                    n += 1
            if int(num_letters) > 0:
                k = 0
                while k < int(num_letters):
                    password += letters[random.randint(0, 51)]
                    k += 1
                    n += 1
        
        final_passwd = "".join(random.sample(password, total_len))
        print(f"Your generated password is:\n{final_passwd}")

        """
        passwd = random.sample(population, k=(int(num_numbers) + int(num_letters) + int(num_symbols)))
        print(f"Your password is:\n" + "".join(passwd))
        """


if __name__ == "__main__":
    main()

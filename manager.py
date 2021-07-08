import fire, string, random, pymongo, hashlib
import pyinputplus as pyip


def main(length):
    """ Main Script Function """

    str_passcode = Generate_password(length)
    

def Generate_password(password_length):
    """ Generating the password """

    letters = string.ascii_letters
    digits = string.digits
    extras = string.punctuation

    values = []
    values.extend(letters)
    values.extend(digits)
    values.extend(extras)

    secret_code = "".join(random.sample(values,password_length))

    print(secret_code)
    return secret_code



if __name__ == "__main__":

    fire.Fire(main)
    print("Code Completed 🚀")


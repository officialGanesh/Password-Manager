import fire, string, random, pymongo, hashlib
import pyinputplus as pyip


def main(length):
    """ Main Script Function """

    str_passcode = Generate_password(length)
    secret_hash(str_passcode)

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

def secret_hash(data):
    """ Making a hash of a secret code """

    passwords_hash = hashlib.md5(data.encode("UTF-8")).hexdigest()
    print(passwords_hash)


if __name__ == "__main__":

    fire.Fire(main)
    print("Code Completed 🚀")


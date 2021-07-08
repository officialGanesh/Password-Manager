import fire, string, random, pymongo, hashlib
import pyinputplus as pyip
from getpass import getpass



def main(length=None):
    """ Main Script Function """

    MAIN_SECRET_CODE = 1234

    print(" ----- Advance Password Generator 🔒 -----")
    print("1. Generate new password")
    print("2. Find your password")

    user_action = pyip.inputNum("🔥Your action: ",min=1,max=2)

    if user_action == 1:

        print("Create your password by following simple steps 💦")
        hint = pyip.inputStr("Hint: ")
        if length == None:

            length = pyip.inputNum("Enter the length of a password: ",min=8,max=95)
        str_passcode = Generate_password(length)
        secret_hash(str_passcode)
    
        print("Password Generated 😄")

    else:
        
        print("Find Your Password 🔍")

        security_key = input("Enter Your Main password (Main secret code) (hidden for security purpose) ")
        
        if security_key == MAIN_SECRET_CODE:
            hint2 = input("Type password's hint: ")
            ...

            print("If You need your actuall password then type hint one more time 🔰")
            hint3 = input("Hint again: ")
            ...

        else:
            print("Sorry, wrong security key. 💢")


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


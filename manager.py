import fire, string, random, pymongo, hashlib
import pyinputplus as pyip
from getpass import getpass
from pymongo import collation


def main(length=None):
    """ Main Script Function """

    MAIN_SECRET_CODE = "you can use any security key in a string format (this ia a text not a part of code)"

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
        hash_passcode = secret_hash(str_passcode)

        data = database_connectivity()

        data.insert_one({"hint":hint,"hash":hash_passcode})
        
        print("Password is Added to the database😄")

    else:
        
        print("Find Your Password 🔍")

        security_key = getpass("Enter Your Main password (Main secret code) (hidden for security purpose) ")
        
        if security_key == MAIN_SECRET_CODE:
            hint2 = input("Type password's hint: ")

            data = database_connectivity()
            all_docs = data.find({"hint":hint2})

            found = 0

            for item in all_docs:
                print(" ----**----")
                print("item: ",item)
                print("Unique-id: ",item["_id"])
                print("Unique-hash: ",item["hash"],"\n")
                print(" ----**----")

                found += 1
            print(f"No of passwords having hint: {hint2} are {found}")
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

    return secret_code

def secret_hash(data):
    """ Making a hash of a secret code """

    passwords_hash = hashlib.md5(data.encode("UTF-8")).hexdigest()
    
    return passwords_hash

def database_connectivity():
    """ Connecting to the database """

    port = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(host=port)

    db = client["Password_Manager"]
    collection = db["Passwords"]

    return collection

if __name__ == "__main__":

    fire.Fire(main)
    
    print("Code Completed 🚀")


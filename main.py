import random

import string

print("Welcome to our Random password generator")

def main():

    length=int(input("Enter the length of password you want:"))

    lower=string.ascii_lowercase

    upper=string.ascii_uppercase

    digit=string.digits

    symbol=string.punctuation

    combine=lower+upper+digit+symbol

    x=random.sample(combine,length)

    password="".join(x)

    print(password)

    main()


main()


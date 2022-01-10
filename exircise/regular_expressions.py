import re

def tel_validation(tel):
    pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

    # match = re.search(pattern, tel)

    # if match:
    #     return True
    # else:
    #     return False

    return re.match(pattern, tel)

def main():
    tel = input("Enter a telephone number: ")

    if tel_validation(tel):
        print("Valid")
    else:
        print("Not Valid")


if __name__ == '__main__':
    main()



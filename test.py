

def main():
    string = str(input("YOU CAN'T USE KEYWORDS AS VARIABLE NAMES: "))
    i = 0
    for character in string:
        if(i % 2 == 0):
            print(character)

        i = i + 1


if __name__ == "__main__":
    main()
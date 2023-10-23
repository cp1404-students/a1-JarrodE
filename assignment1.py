"""
Name:
Date started: 21/10/2023
GitHub URL: https://github.com/cp1404-students/a1-JarrodE
"""

FILENAME = "songs.csv"
MENU = """Menu:
D - Display songs
A - Add new songs
C - Complete a song
Q - Quit"""

def main():
    """Program that allows the user to track songs that they wish to
    learn and songs they have completed learning"""
    print("Song List 1.0 - by Jarrod Eaton")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            read_file()
        elif choice == "A":
            print(f"")
        elif choice == "C":
            print()
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished")
    read_file()


def read_file():
    in_file = open(FILENAME)
    text = in_file.read()
    in_file.close()
    print(text)


if __name__ == '__main__':
    main()

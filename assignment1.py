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
            print("Enter details for a new song.")
            write_file()
        elif choice == "C":
            print()
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Make some music!")


def read_file():
    in_file = open(FILENAME, "r")
    text = in_file.read()
    in_file.close()
    print(text)


def write_file():
    out_file = open(FILENAME, "a")
    song_name = input("Title: : ")
    print(song_name, file=out_file)
    out_file.close()


if __name__ == '__main__':
    main()

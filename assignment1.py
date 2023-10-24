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
    file_songs = load_songs(FILENAME)
    print(f"{len(file_songs)} songs loaded.")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            print(file_songs)
        elif choice == "A":
            print("Enter details for a new song.")
            add_song_to_file()
        elif choice == "C":
            print()
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Make some music!")


def load_songs(filename):
    songs = []
    try:
        with open(filename, "r") as in_file:
            for line in in_file:
                parts = line.strip().split(",")
                songs.append(parts)
        in_file.close()
    except FileNotFoundError:
        pass
    return songs


def add_song_to_file():
    out_file = open(FILENAME, "a")
    title = input("Title: : ")
    artist = input("Artist: ")
    year = int(input("Year: "))
    print(f"{title} by {artist} ({year}) added to song list.", file=out_file)
    out_file.close()




if __name__ == '__main__':
    main()

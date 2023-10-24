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
    songs = read_file()
    print("Song List 1.0 - by Jarrod Eaton")
    print(f"{len(songs)} songs loaded")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            display_songs(songs)
        elif choice == "A":
            print("Enter details for a new song.")
            add_song_to_file()
        elif choice == "C":
            print()
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    write_file(songs)
    print("Make some music!")


def read_file():
    with open(FILENAME, "r") as in_file:
        songs = []
        for line in in_file:
            parts = line.strip().split(",")
            songs.append(parts)
        return songs


def write_file(songs):
    with open(FILENAME, "w") as out_file:
        for song in songs:
            print(",".join(song), file=out_file)


def add_song_to_file():
    out_file = open(FILENAME, "a")
    title = input("Title: : ")
    artist = input("Artist: ")
    year = int(input("Year: "))
    print(f"{title} by {artist} ({year}) added to song list.", file=out_file)
    out_file.close()


def display_songs(songs):
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song[0]} - {song[1]} ({song[2]})")


if __name__ == '__main__':
    main()

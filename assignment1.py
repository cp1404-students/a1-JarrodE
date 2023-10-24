"""
Name:
Date started: 21/10/2023
GitHub URL: https://github.com/cp1404-students/a1-JarrodE
"""

FILENAME = "songs.csv"
LEARNED = "l"
UNLEARNED = "u"
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
            add_new_song(songs)
        elif choice == "C":
            print("Enter the number of a song to mark as learned.")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    write_file(songs)
    print(f"{len(songs)} songs saved to {FILENAME}")
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


def add_new_song(songs):
    title = get_valid_input("Title: : ")
    artist = get_valid_input("Artist: ")
    year = get_valid_number("Year: ")
    songs.append([title.title(), artist.title(), str(year), UNLEARNED])
    print(f"{title.title()} by {artist.title()} ({year}) added to song list.")


def display_songs(songs):
    max_title_length = max(len(song[0]) for song in songs)
    max_artist_length = max(len(song[1]) for song in songs)
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song[0]:{max_title_length}} - {song[1]:{max_artist_length}} ({song[2]})")


def complete_song(songs):
    choice = input(">>> ")


def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Number must be > 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input.strip()
        else:
            print("Input can not be blank.")


if __name__ == '__main__':
    main()

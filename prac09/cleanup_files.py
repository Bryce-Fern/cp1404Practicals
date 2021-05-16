import os


def main():
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            song_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(song_name, new_name)
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()

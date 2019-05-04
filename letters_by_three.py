import string

file_name = "/Users/michaelarslangul/apps/python_projects/pyexercises/files" \
    "/letters_by_three.txt"
char_seq = [i for i in string.ascii_lowercase]


def create_file():
    return open(file_name, 'w+')


def write_char_to_file():
    fo = create_file()
    counter = 0
    for item in char_seq:
        if (counter > 1 and counter % 3 == 0):
            fo.write("\n")
        fo.write("{}".format(item))
        counter += 1
    fo.close()

import string


file_name = "/Users/michaelarslangul/apps/python_projects/pyexercises/files" \
    "/43.txt"
char_seq = [i for i in string.ascii_lowercase]


def create_file(file_name):
    return open(file_name, 'w+')


def write_char_to_file(file):
    fo = create_file(file)
    counter = 0
    for item in char_seq:
        if (counter > 1 and counter % 2 == 0):
            fo.write("\n")
        fo.write("{}".format(item))
        counter += 1
    fo.close()

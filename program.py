""" before you start your app
    1- create a directory to host the app
    2- Initiliaze a git repo
    3- create a readme file explaining what the app is about.
    4- create a file called program.py which has the code below
    5- add and commit to git
    6- start implementing the functions after each function is completed,
     commit your changes
    7- have for each stage a different version
"""
# Stage 1

import os


def main():
    print_header()
    path = get_folder_user()
    # TODO: ask the user to give you the path to the folder
    key = get_keyword_user()
    # TODO: ask the user to give you the keyword to find
    return_results(path, key)
    # TODO: return line_no, the line of every instance found


def print_header():
    print(" ===================================== ")
    print(" |            TEXT FINDER            | ")
    print(" ===================================== ")


def get_folder_user():
    path = input("Please enter the path to your folder: ")
    return path


def get_keyword_user():
    keyword = input("Please enter the word you want to find: ")
    return keyword


def return_results(path, keyword):
    file_no = 0
    for file in os.listdir(path):
        file_no += 1
        line_no = 0
        with open(path + "/" + file, "r") as openfile:
            for line in openfile:
                line_no += 1
                if str(keyword).lower() in line.lower():
                    print("File No: " + str(file_no) + " Line No: " + str(line_no))


if __name__ == '__main__':
    main()

# Stage 2
# once you finish the first stage, then we can move to add argparse
# so it can run as one command line

# Stage 3
# add logging capability to the app

# Stage 4
# add unit testing

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
import sys
import re
from collections import namedtuple

try:
    input = raw_input
except NameError:
    pass

myResults = namedtuple("myResults", 'file line')


def main():
    print_header()
    path = get_folder_user()
    key = get_keyword_user()
    rL, wC = return_results(path, key)
    writeResults(rL, wC, key)


def print_header():
    print(" ===================================== ")
    print(" |            WORD FINDER            | ")
    print(" ===================================== ")


def get_folder_user():
    path = input("Please enter the path to your folder: ").rstrip()
    if not os.path.isdir(path):
        print("Please enter a valid path!")
        sys.exit()
    else:
        return path


def get_keyword_user():
    keyword = input("Please enter the word you want to find: ").rstrip()
    if not keyword.strip():
        print("Please enter a word to search!")
        sys.exit()
    else:
        return keyword


# let's do this in two steps
# first if path is file then search
# if it is a directory just continue "ignore it"
# once we get it right then we can think about
# if it is a directory
# and since we are returning three item (file, line_no, text)
# let's create a data structure so we can manipulate them
# I will create a class or namedtuple to use
def return_results(path, keyword):
    resultList = []
    os.chdir(path)
    word_count = 0
    for file in os.listdir(path):
        if file != "Search_result.txt":
            with open(file, "r") as openfile:
                for num, line in enumerate(openfile):
                    if re.search(r'\b({})\b'
                                 .format(keyword.lower()), line.lower()):
                        word_count += 1
                        resultList.append(myResults(file, num+1))
                        print("File Name: {}, Line No: {}".format(file, num+1))
    return resultList, word_count


def writeResults(resultList, word_count, keyword):
    with open("Search_result.txt", "a") as results_file:
        results_file.write("Word: {}, Word Count: {}\n".format(
            keyword, str(word_count)))
        results_file.write("-------------------------\n")
        for item in resultList:
            results_file.writelines("File: {}, Line: {}\n"
                                    .format(item.file, item.line))
        results_file.write("=========================\n")


if __name__ == '__main__':
    main()

# Stage 2
# once you finish the first stage, then we can move to add argparse
# so it can run as one command line

# Stage 3
# add logging capability to the app

# Stage 4
# add unit testing

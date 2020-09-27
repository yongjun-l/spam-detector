'''
    File name: create_csv.py
    Author: Yongjun Lee
    Date created: 9/27/2020
    Python Version: 3.8.5
    Purpose: Pre-process raw email data into a csv format
             for email spam classifier.
'''

import os
import csv

def write_to_csv(file_dir):
    '''
    Goes through every subdirectories of a given directory,
    and writes every .txt file content to a csv file called "csv_dataset"
    Each .txt file is written as a single line in csv
    '''

    file_list = os.listdir(file_dir)

    for file in file_list:
        if file.endswith(".txt"):
            dir_file = os.path.join(file_dir, file)

            # reading raw email txt files
            with open(dir_file, "r", encoding="utf8", errors='ignore') as text:
                entry = text.read().replace("\n", " ").replace(","," ")
                if file.endswith("ham.txt"):
                    entry += ",ham"
                else:
                    entry += ",spam"

            # writing to csv
            with open("dataset.csv", 'a') as csv_dataset:
                csv_dataset.write(entry)
                csv_dataset.write('\n')

        else:
            write_to_csv(os.path.join(file_dir, file))

if __name__ == "__main__":
    dir_base = os.path.abspath("")
    dir_dataset = os.path.join(dir_base, "dataset")
    write_to_csv(dir_dataset)

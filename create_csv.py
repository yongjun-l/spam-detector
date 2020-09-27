import os
import csv

dir_base = os.path.abspath("")
dir_dataset = os.path.join(dir_base, "dataset")

def write_to_csv(file_dir):
    file_list = os.listdir(file_dir)

    for file in file_list:
        if file.endswith(".txt"):
            dir_file = os.path.join(file_dir, file)

            with open(dir_file, "r", encoding="utf8", errors='ignore') as text:
                if file.endswith("ham.txt"):
                    entry = "ham,"
                else:
                    entry = "spam,"
                entry += text.read().replace("\n", " ")

            with open("csv_dataset.csv", 'a') as csv_dataset:
                csv_dataset.write(entry)
                csv_dataset.write('\n')

        else:
            write_to_csv(os.path.join(file_dir, file))

write_to_csv(dir_dataset)

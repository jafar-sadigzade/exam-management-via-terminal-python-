import csv
import os


def csvtodict(file_path):
    listdict = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                listdict.append(row)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return listdict


# Usage
file_name = 'examform.csv'
filepath = os.path.join(os.getcwd(), file_name)
listdict = csvtodict(filepath)

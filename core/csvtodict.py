import csv
import os

file_name = 'examform.csv'  # Replace with your actual CSV file path
filepath = os.path.join(os.getcwd(), file_name)
listdict = []


def csvtodict(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            listdict.append(row)


csvtodict(filepath)

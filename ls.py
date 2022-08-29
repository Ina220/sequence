# Program that identifies a title based on the content of its sequence
import sys
import csv
import re
from datetime import date



def main():
    if len(sys.argv) != 3:
        print("Please use: python ls.py data.csv seq.txt")
        exit(1)


# Open CSV file and the given sequence, read contents into memory
csv_file = open(sys.argv[1], "r")
database = csv.DictReader(csv_file)
column_heads = list(database.fieldnames[1:])

# First try to open the second argument in the system argument vector and if file was given to read from,
#read and sav it into memory
try:
    text_file = open(sys.argv[2], "r")
    seq = text_file.read()


    # For each STR compute the longest run of consecutive repeats in the sequence
    # Save Str counts in a new dictionary
    new_dict = {}

    for header in column_heads:
        STR = re.findall(f'(?:{header})+', seq)
        most = max(map(len, STR), default=0) // len(header)
        new_dict[header] = most

    # Compare the STR counts against each row in the csv file
    # If it matches print the title
    for row in database:
        if all(new_dict[header] == int(row[header]) for header in new_dict):
            print(row["title"])
            exit()

    print("No match")

    csv_file.close()
    text_file.close()

# if entering the second argument when promted, raises error that the file doesn't exists, create a new text file 
#in the program directory and write the today's date
except FileNotFoundError:
    create = open(f"{sys.argv[2]}.text", "w")
    tddt = date.today()
    lg = create.write(f"Today: {tddt}")
    create.close()

if __name__ == '__main__':
     main() 
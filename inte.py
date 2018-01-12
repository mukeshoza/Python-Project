import csv
import sys

#input number you want to search
number = input('Enter number to find:\n')

#read csv, and split on "," the line
csv_file = csv.reader(open('sample.csv', 'rb', encoding='ascii'), delimiter=',')

#loop through csv list
for row in csv_file:
    # if current rows 2nd value is equal to input, print that row
    if number == row[1]:
        print(number)
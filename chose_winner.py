"""Script to read the csv file, chose random value between 0 and 122928
and pick the winner.
"""
import csv
import random

csv_file = open('tweets.csv', 'r')
csv_reader = csv.reader(csv_file, delimiter=',')

# hardcode rows_count value won't change
# not sure why it doesn't like len(list(csv_reader))
rows_count = 122928
print(f"number of rows : {rows_count}")

# we generate a random value between 0 and rows_count (122928)
random_value = random.randint(0, 122928)
print(f"random value : {random_value}")


for i, row in enumerate(csv_reader):
    if i == random_value:
        print(f"\ndate     : {row[0]}")
        print(f"username : {row[1]}")
        print(f"tweet    : {row[2]}")


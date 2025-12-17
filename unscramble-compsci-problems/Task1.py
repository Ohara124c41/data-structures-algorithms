"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers = set()
for sender, receiver, _, _ in calls:
    numbers.add(sender)
    numbers.add(receiver)
for sender, receiver, _ in texts:
    numbers.add(sender)
    numbers.add(receiver)
print(f"There are {len(numbers)} different telephone numbers in the records.")

"""
Expected output:
There are 570 different telephone numbers in the records.
"""

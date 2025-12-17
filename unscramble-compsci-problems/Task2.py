"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
time_spent = {}
for caller, receiver, _, duration in calls:
    d = int(duration)
    time_spent[caller] = time_spent.get(caller, 0) + d
    time_spent[receiver] = time_spent.get(receiver, 0) + d
max_number = max(time_spent, key=lambda k: time_spent[k])
print(f"{max_number} spent the longest time, {time_spent[max_number]} seconds, on the phone during September 2016.")

"""
Expected output:
(080)33251027 spent the longest time, 90456 seconds, on the phone during September 2016.
"""

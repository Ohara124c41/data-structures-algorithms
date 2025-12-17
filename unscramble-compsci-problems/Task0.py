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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_text = texts[0]
last_call = calls[-1]
print(f"First record of texts, {first_text[0]} texts {first_text[1]} at time {first_text[2]}")
print(f"Last record of calls, {last_call[0]} calls {last_call[1]} at time {last_call[2]}, lasting {last_call[3]} seconds")

"""
Expected output:
First record of texts, 97424 22395 texts 90365 06212 at time 01-09-2016 06:03:22
Last record of calls, 98447 62998 calls (080)46304537 at time 30-09-2016 23:57:15, lasting 2151 seconds
"""

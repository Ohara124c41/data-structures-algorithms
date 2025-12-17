## Task0
Read CSVs into lists and print first text and last call. Reading dominates time O(n_text + n_call); lookups are O(1). Space O(n_text + n_call) to hold rows.

## Task1
Iterate through all call/text rows, insert numbers into a set, and report its size. Time O(n_text + n_call) set operations are O(1) average. Space O(u) for unique numbers.

## Task2
Traverse all calls, accumulate durations in a dict for both caller and receiver, then take max. Time O(n_call); dict ops O(1) average. Space O(u) for per-number totals.

## Task3
Single pass over calls to collect codes for Bangalore callers and count Bangalore-to-Bangalore calls; then sort the code set. Time O(n_call + k log k) where k is distinct codes; space O(k) for codes and O(1) counters.

## Task4
Build sets for outgoing calls, incoming calls, and all text participants, then compute set difference and sort results. Time O(n_call + n_text + t log t) where t is candidate count; space O(u) for the sets.

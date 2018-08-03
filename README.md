# Most Proftable Instance

Hi, this repository include the following exercise:

You will be supplied with two data files in CSV format: "first-exercise-input-1.txt" 
and "first-exercise-input-2.txt". The first file contains statistics about various 
instances in AWS. The second file contains additional data.

Given the following formula:
 cost_benefit = (((MEMORY / m) + VCPU)/COST)
 Where m = 3.75 1/GiB (memory unit factor)

Write a program to read in the data files from disk, it must then print the names
of only the HVM instance types from a better cost benefit to the lowest. 
Do not print any other information.

I made it using Python 3 and the 2 files mentioned above

To run the script, just go to the terminal and type:
`python3 most_profit_instance.py first-exercise-input-1.txt first-exercise-input-2.txt`

Carefull with project dependencies, i just use 2 modules:
`import sys` --> Read the files from the script input

`import re` --> Make the "grep" thing 😝
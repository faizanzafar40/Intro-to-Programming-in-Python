"""
here I am
using 'in' operator to check whether user provide
gmail, yahoo, hotmail or rwth-aachen email
"""

email = input("Please enter your email:")

if('gmail' in email):
    print("Logging into gmail account...")
elif('yahoo' in email):
    print("Logging into yahoo account...")
elif('rwth-aachen' in email):
    print("Logging into RWTH Aachen account...")
elif('hotmail' in email):
    print("Logging into hotmail account...")
else:
    print("Unknown email provided!!")
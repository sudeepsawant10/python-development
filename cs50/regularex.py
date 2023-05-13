# powerful feature
# We can define patterns to user inputs
import re
s = input("Do you aggree? ")

if re.search("^y(es)?$", s, re.IGNORECASE):
    print("Agreed")
elif re.search("n(o)?", s, re.IGNORECASE):
    print("Not agreed!")

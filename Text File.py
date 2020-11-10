'''
import sys
sys.stdout.write("Enter 1st no. : ")
a = int(sys.stdin.readline())

sys.stdout.write("Enter 2nd no. : ")
b = int(sys.stdin.readline())

if b ==0:
    sys.stderr.write("Cannot divide any no by zero : ")
else:
    sys.stdout.write("Division possible.")'''

# Data Handeling concept

import sys
sys.stdout.write("Enter file name : ")
file = sys.stdin.readline()
f = open(file.strip(),"r")
while True :
    ch = f.read(1)
    if ch == "":
        sys.stderr.write("\nEnd of File reached...")
        break
    else:
        print(ch, end = "")
f.close()
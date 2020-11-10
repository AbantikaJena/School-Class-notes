import csv
file = input("Enter csv file name : ")
def Wirte():
    f = open(file, "w", newline="")
    s_writer = csv.writer(f, delimiter = ";")
    s_writer.writerow(["RollNo","Name","Marks"])
    rec = []
    while True:
        r = int(input("Enter roll no. : "))
        n = input("Enter Name : ")
        m = float(input("Enter marks : "))
        lst = [r,n,m]
        rec.append(lst)
        ch = input("Do you want to enter more records?(y/f) : ")
        if ch in "Nn":
            break
    for i in rec:
        s_writer.writerow(i)  # writerow

    # s_writer.writerows(s)  # writerows

    f.close()

def Read():
    f = open(file, "r") # if not mentioned any delimiter in wriet then write {f = open(file, "r", newline = '\r\n')}
    s_reader = csv.reader(f)
    for i in s_reader:
        print(i)

Wirte()
Read()
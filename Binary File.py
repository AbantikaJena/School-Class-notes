file = input("Enter file name : ")


def MainMenu():
    print("-" * 30)
    print("1. Write Data in a Binary File...")
    print("2. Read Data from a file...")
    print("3. Append Data in A File...")
    print("4. Search Operation in a File...")
    print("5. Update Data in a File...")
    print("6. Delete Operation in a File...")
    print("7. Exit")
    print("-" * 30)


import pickle

def Write():
    f = open(file,"wb")
    record = []
    while True:
        rno = int(input("Enter Roll no. : "))
        name = input("Name :")
        marks = float(input("Marks: "))
        data = [rno, name, marks]
        record.append(data)
        ch_w = input("More(Y/N) ? ")
        if ch_w in "Nn":
            break
    pickle.dump(record,f)
    print("Recorded Added...")
    f.close()


def Read():
    print("Contents in a file...")
    f = open(file,"rb")
    try:
        while True:
            s = pickle.load(f)
            for i in s:
                print(i)
    except Exception:
        f.close()


def Append():
    f = open(file, "rb+")
    print("Append Data in a file...")
    Rec = pickle.load(f)
    while True:
        rno = int(input("Enter Roll no. : "))
        name = input("Name :")
        marks = float(input("Marks: "))
        data = [rno, name, marks]
        Rec.append(data)
        ch_w = input("More(Y/N) ? ")
        if ch_w in "Nn":
            break
    f.seek(0)
    pickle.dump(Rec, f)
    print("Recorded Append...")
    f.close()


def Search():
    f = open(file,"rb")
    r = int(input("Enter roll no to be searched: "))
    found = 0
    try:
        while True:
            s = pickle.load(f)
            for i in s:
                if i[0] == r:
                    print(i)
                    found = 1
                    break
    except Exception:
        f.close()
    if found==0:
        print("Sorry! no Record Found...")


def Update():
    f = open(file, "rb+")
    r = int(input("Enter roll no whose details to be updated : "))
    f.seek(0)
    try:
        while True:
            rpos = f.tell()
            s= pickle.load(f)
            for i in s:
                if i[0] == r:
                    i[1] = input("New Name : ")
                    i[2] = float(input("Update Marks : "))
                    f.seek(rpos)
                    pickle.dump(s,f)
    except Exception:
        f.close()


def Delete():
    f = open(file, "rb+")
    s = pickle.load(f)
    f.close()

    r = int(input("Enter roll no whose details to be deleted : "))
    f = open(file, "wb")
    reclst = []
    for i in s:
        if i[0] == r:
            continue
        reclst.append(i)
    pickle.dump(reclst,f)
    f.close()

while True:
    MainMenu()
    ch = int(input("Enter your choice :  "))
    if ch == 1:
        Write()
    elif ch == 2:
        Read()
    elif ch == 3:
        Append()
    elif ch == 4:
        Search()
    elif ch == 5:
        Update()
    elif ch == 6:
        Delete()
    elif ch == 7:
        print("Thank You!\nTask Done!")
        break
    else:
        print("No more choice...")

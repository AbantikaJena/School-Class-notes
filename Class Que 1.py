# Class Que 1

# WAP which accept an integer array and exchange the values of first half element with the 2nd half element of the array.

def Swap_half_list(L):
    l = len(L)
    n = int(l / 2)
    if l % 2 == 0:
        L1 = [i for i in L[n:]]
        L2 = [i for i in L[:n]]
        L1.extend(L2)
    else:
        L1 = [i for i in L[n+1:]]
        Lm = L[n]
        L2 = [i for i in L[:n]]
        L1.append(Lm)
        L1.extend(L2)
    print("Swaped List : ", L1)
L = eval(input("Enter an array : "))
Swap_half_list(L)

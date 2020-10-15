# WAP which accept an integer array and exchange the values of first half element with the 2nd half element of the array.
'''
def Swap_half_list(L):
    l = len(L)
    n = int(l/2)
    if l%2==0 :
        L[:n], L[n:] = L[n:], L[:n]
    else:
        L[:n], L[n], L[n+1:] = L[n+1:], L[n], L[:n]
    print("Swaped List : ",L)

L = eval(input("Enter an array : "))
Swap_half_list(L)'''

def Swap_half_list(L):
    l = len(L)
    n = int(l / 2)
    L = ( L[n:]+L[:n] if l%2==0 else L[(n+1):]+L[n]+L[:n])
    print("Swaped List : ", L,l)
L = eval(input("Enter an array : "))
Swap_half_list(L)
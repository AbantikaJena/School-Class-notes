# WAP to display sum of odd and even values separately from the list of values.

def sum_of_odd_even(L):
    ol = ( i for i in L if i%2!=0 )
    el = ( i for i in L if i%2== 0 )
    o,e=0,0
    for i in ol:
     o+=i
    for i in el:
     e+=i
    print("Sum of Odd no. : ",o,"  Sum of Even no. : ",e)
L = eval(input("Enter an array : "))
sum_of_odd_even(L)
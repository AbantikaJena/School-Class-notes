# WAP to find and display the count of all those numbers which are between 1 and N, which are either divisible by 3 or by 7.
n = 0
N = int(input("Enter no of numbers to be checked : "))
x = [ n for i in range(1,N+1) if i%3==0 or i%7==0 ]
print("Count : ",len(x))

def binarysearch(thearray,searchval):
    low = 0
    pos =0
    high= len(thearray)-1
    ctr=pos=0
    while low<=high:
        mid=(high+low)//2
        if thearray[mid]==search
n = 5
def silnia(n):  
    if n<2: 
        return 1
    else:
        for i in range(2,n):
            n*=i
        return print(n)

silnia(n)



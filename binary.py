def dtob(n):
    if n==0:
        return ''
    else:
        return dtob(n//2) + str(n%2)
         
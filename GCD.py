def GCD(m,n):
    if n == 0:
        return m
    else:
        r = (m%n)
        return GCD(n,r)

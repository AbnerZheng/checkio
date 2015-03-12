def f(a,b,c,d,e,f,n):
    for i in range(n):
        a,b,c=b,c,d*c+e*b+f*a
    return a

def fibgolf(t, n):
    a = t[0]
    if a=='f':return f(0,1,1,1,1,0,n)
    if a=='t':return f(0,1,1,1,1,1,n)
    if a=='l':return f(2,1,3,1,1,0,n)
    if a=='j':return f(0,1,1,1,2,0,n)
    if t=='padovan':return f(0,1,1,0,1,1,n)
    if t=="pell":return f(0,1,2,2,1,0,n)
    return f(3,0,2,0,1,1,n)

# * amalisiz kopaytish
def kopaytr(a: int, b: int, c: int):
    if b-1 > 0:
        kopaytr(a+c,b-1,c)
    else: 
        print(a)    
a, b= int(input()), int(input())
kopaytr(a,b,a)
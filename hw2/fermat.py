"""Created on Sun Feb 2 2014
@author: Dimitar Dimitrov (dimitdim)"""

def check_fermat(a,b,c,n):
    if a**n+b**n==c**n and n>2:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def prompt():
    a=int(raw_input("a: "))
    b=int(raw_input("b: "))
    c=int(raw_input("c: "))
    n=int(raw_input("n: "))
    check_fermat(a,b,c,n)


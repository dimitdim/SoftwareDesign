"""Created on Wed Feb 12 2014
@author: Dimitar Dimitrov (dimitdim)"""

def grid(r,c,w,h):
    for m in range(r):
        for i in range(c):
            print '+','-'*w,
        print '+'
        for n in range(h):
            for i in range(c):
                print '|',' '*w,
            print '|'
    for i in range(c):
        print '+','-'*w,
    print '+'

def first_grid():
    grid(2,2,4,4)

def second_grid():
    grid(4,4,4,4)

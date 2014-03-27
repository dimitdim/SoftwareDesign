def my_regular_polygon(x,y,s,n):
    "Input: (int x-coor,int y-coor, side length, # sides)"
    world=TurtleWorld()
    dim=Turtle()
    dim.x=x
    dim.y=y
    dim.delay=.01
    for i in range(n):
        fd(dim,s)
        lt(dim, angle=(float(360)/n))
    wait_for_user()

def my_circle(x,y,r):
    "Input: (cntr x-coor, cntr y-coor, radius)"
    from math import sqrt,pi
    x=x
    y=y-r
    n=100
    s=2*pi*r/n
    my_regular_polygon(x,y,s,n)

def snow_flake_side(dim, l, level):
    if level>0:
        snow_flake_side(dim, l/3,level-1)
        rt(dim, angle=60)
        snow_flake_side(dim, l/3,level-1)
        lt(dim, angle=120)
        snow_flake_side(dim, l/3,level-1)
        rt(dim, angle=60)
        snow_flake_side(dim, l/3,level-1)
    elif level==0:
        fd(dim,l)

def snow_flake(x, y, l, level):
    from math import sqrt,pi
    world=TurtleWorld()
    dim=Turtle()
    dim.x=x#-(sqrt(2)*l)
    dim.y=y#-(sqrt(2)*l)
    dim.heading=0
    dim.delay=.01
    for i in range(6):
        snow_flake_side(dim, l, level)
        lt(dim, angle=60)
    wait_for_user()

if __name__=='__main__':
    from swampy.TurtleWorld import *

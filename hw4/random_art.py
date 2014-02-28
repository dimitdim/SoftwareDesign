# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

from random import randint
from math import cos, sin, pi
import Image

## SS: You did not include a remap_interval() method, as specified by the hw assignment

## SS: Your build_random_function outputs functions like: ['x', 'in_1', 'in_2']
##     The assignment wanted functions like: ["prod",["x"],["y"]]
##     ['x', 'in_1', 'in_2'] I believe should be represented simply as ["x"], I don't understand
##     why you used in_1 and in_2
def build_random_function(min_depth, max_depth):
    "Input: minimum and maximum depths; Ouput: random function made up of products, sines, cosines, cubes and averages of two variables in list form"

    funclst = ['prod','cos_pi','sin_pi','cube','average','x','y']
    varlst = ['in_1','in_2']
    lvl = randint(min_depth,max_depth)
    def new_func(level):
        if level>1:
            return([funclst[randint(0,len(funclst)-1)],new_func(level-1),new_func(level-1)])
        else:
            return(varlst[randint(0,len(varlst)-1)])
    return(new_func(lvl))

def evaluate_random_function(f, x, y):
    "Input: random function generated by builid_random_function and two input variablee; Output: evaulated function at those variables"

    if type(f)==str:
        if f=='in_1':
            return x
        if f=='in_2':
            return y
        else: print 'Invalid input'
    elif type(f)==float or type(f)==int:
        return f
    elif type(f)==list:
        if f[0]=='prod':
            return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
        if f[0]=='cos_pi':
            return cos(pi*evaluate_random_function(f[1],x,y))
        if f[0]=='sin_pi':
            return sin(pi*evaluate_random_function(f[1],x,y))
        if f[0]=='cube':
            return evaluate_random_function(f[1],x,y)**3
        if f[0]=='average':
            return .5*(evaluate_random_function(f[1],x,y)+evaluate_random_function(f[2],x,y))
        if f[0]=='x':
            return evaluate_random_function(f[1],x,y)
        if f[0]=='y':
            return evaluate_random_function(f[2],x,y)
        else: print 'Invalid function'
    else: print 'Invalid type'

## SS: It doesn't look like you made your conversions correctly, because I was seeing (R,B,G) tuples
##     looking like: (254, 143, -13911), (255, 147, 15382), (254, 149, -1124), which threw an error
##     once when I ran it and the G value exceeded the expected bounds

l=400
w=400
red=build_random_function(10,10)
blue=build_random_function(10,10)
green=build_random_function(10,10)
art=Image.new("RGB",(l,w))
pix=art.load()
for x in range(l):
    for y in range(w):
        x0=2*float(x)/255-1
        y0=2*float(y)/255-1
        r = int(255*.5*(1+evaluate_random_function(red, x0, y0)))
        b = int(255*.5*(1+evaluate_random_function(blue, x0, y0)))
        g = int(255*.5*(1+evaluate_random_function(green, x0, y0)))
        pix[x,y]=(r,b,g)
art.save('art.jpg')
print (red,green,blue)

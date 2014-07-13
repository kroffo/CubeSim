from visual import *
from itertools import product
from math import pi

cubies = [
        box(pos=(i,j,k),length=0.9,height=0.9,width=0.9,color=color.white)
        for i,j,k in product(range(0,3),repeat=3)
        if (i,j,k) != (1,1,1) ]

def main():

    moves = {"r":('x',2,1), "r'":('x',2,-1), "r2":('x',2,2),
             "l":('x',0,-1), "l'":('x',0,1), "l2":('x',0,2),
             "m":('x',1,1), "m'":('x',1,-1), "m2":('x',1,2),
             "u":('y',2,1), "u'":('y',2,-1), "u2":('y',2,2),
             "d":('y',0,-1), "d'":('y',0,1), "d2":('y',0,2),
             "e":('y',1,1), "e'":('y',1,-1), "e2":('y',1,2),
             "b":('z',2,-1), "b'":('z',2,1), "b2":('z',2,2),
             "f":('z',0,1), "f'":('z',0,-1), "f2":('z',0,2),
             "s":('z',1,1), "s'":('z',1,-1), "s2":('z',1,2),
             "x":('x',0,1,True), "x'":('x',0,-1,True), "x2":('x',0,2,True),
             "y":('y',0,1,True), "y'":('y',0,-1,True), "y2":('y',0,2,True),
             "z":('z',0,1,True), "z'":('z',0,-1,True), "z2":('z',0,2,True)
             }

    while True:
        command = raw_input("Enter a move: ").lower().split()
        for move in command:
            params = moves.get(move)
            print "Invalid move" if params == None else turn(*params)


def turn(axis,row,degree,rotation=False):
    turning = []
    if not rotation:
        if axis == 'x':
            for cubie in cubies:
                if cubie.x == row:
                    turning.append(cubie)
        elif axis == 'y':
            for cubie in cubies:
                if cubie.y == row:
                    turning.append(cubie)
        elif axis == 'z':
            for cubie in cubies:
                if cubie.y == row:
                    turning.append(cubie)
        animateTurn(turning)
    else:
        #Rotate the entire cube along this axis            

def animateTurn(affected):
    #Write function to animate the turns

if __name__ == '__main__':
    exit(main())
    
    

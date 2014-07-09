from visual import *
from itertools import product

cubee = [
    box(pos=(i,j,k),length=0.9,height=0.9,width=0.9,color=color.white)
    for i,j,k in product(range(-1,2),repeat=3)
    if (i,j,k) != (0,0,0) ]
